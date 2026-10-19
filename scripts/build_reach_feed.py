"""Create compact, verifiable public REACH data feeds for REACH Scout.

Run from the root of the PART-WPO/reach-dashboard repository:
    python scripts/build_reach_feed.py

Reads the existing public CSV but NEVER edits it. Generates agent-data/ only.
Requires Python 3.10+; no third-party dependencies.
"""

import csv
import hashlib
import io
import json
import shutil
from pathlib import Path

SOURCE = Path("Open Science Report (GitHub) - Open Science Report (1).csv")
DEST = Path("agent-data")
MAX_BYTES = 48 * 1024  # Target: no generated CSV shard exceeds 48 KiB.

INDEX_COLUMNS = [
    "Record ID",
    "REACH UID",
    "Output Type",
    "Award Number(s)",
    "Title",
    "Link to Output",
    "Funded By",
    "Sheet Name",
    "Principal Investigators",
    "Journal Pub Date",
    "Detail File",
]
REQUIRED_SOURCE_COLUMNS = {
    "REACH UID",
    "Output Type",
    "Award Number(s)",
    "Title",
    "Link to Output",
}


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def csv_line(values):
    """Serialize one CSV record, respecting quotes and embedded newlines."""
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(values)
    return buffer.getvalue().encode("utf-8")


def split_csv(rows, columns, folder, prefix):
    """Write byte-limited CSV shards, returning manifest entries and row paths."""
    folder.mkdir(parents=True, exist_ok=True)
    header = csv_line(columns)
    shards, record_paths = [], {}
    pending = []
    pending_bytes = len(header)
    shard_number = 1

    def flush():
        nonlocal pending, pending_bytes, shard_number
        if not pending:
            return
        filename = f"{prefix}-{shard_number:03d}.csv"
        path = folder / filename
        contents = header + b"".join(blob for _, blob in pending)
        assert len(contents) <= MAX_BYTES, f"Oversize shard: {path}"
        path.write_bytes(contents)
        relative = path.as_posix()
        for record_id, _ in pending:
            record_paths[record_id] = relative
        shards.append({
            "path": relative,
            "rows": len(pending),
            "bytes": len(contents),
            "sha256": sha256_bytes(contents),
        })
        pending = []
        pending_bytes = len(header)
        shard_number += 1

    for row in rows:
        blob = csv_line([row.get(col, "") or "" for col in columns])
        if len(header) + len(blob) > MAX_BYTES:
            raise ValueError(f"Individual record {row['Record ID']} exceeds shard limit")
        if pending and pending_bytes + len(blob) > MAX_BYTES:
            flush()
        pending.append((row["Record ID"], blob))
        pending_bytes += len(blob)

    flush()
    return shards, record_paths


def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Source CSV not found: {SOURCE}")
    source_bytes = SOURCE.read_bytes()

    with SOURCE.open("r", newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        source_columns = reader.fieldnames or []
        missing = REQUIRED_SOURCE_COLUMNS - set(source_columns)
        if missing:
            raise ValueError(f"Source CSV missing required columns: {sorted(missing)}")
        records = list(reader)

    if not records:
        raise ValueError("Source CSV is empty; refusing to overwrite current feed")

        # Validate permanent REACH UIDs.
    uids = [
        (row.get("REACH UID") or "").strip()
        for row in records
    ]

    if any(not uid for uid in uids):
        raise ValueError("One or more records are missing REACH UID")

    if len(uids) != len(set(uids)):
        raise ValueError("Duplicate REACH UIDs detected")

    if any(not uid.startswith("reachuid-v1-") for uid in uids):
        raise ValueError("Unexpected REACH UID format")

    print(f"Validated {len(uids):,} unique REACH UIDs")

    detailed_rows = []
    for i, row in enumerate(records, start=1):
        detailed_rows.append({"Record ID": f"reach-{i:06d}", **row})

    # This directory contains only generated output; source CSV is unaffected.
    for subfolder in (DEST / "index", DEST / "details"):
        if subfolder.exists():
            shutil.rmtree(subfolder)

    detail_columns = ["Record ID"] + source_columns
    detail_files, detail_paths = split_csv(
        detailed_rows, detail_columns, DEST / "details", "part"
    )
    index_rows = []
    for row in detailed_rows:
        index_row = {col: row.get(col, "") for col in INDEX_COLUMNS}
        index_row["Detail File"] = detail_paths[row["Record ID"]]
        index_rows.append(index_row)

    index_files, _ = split_csv(index_rows, INDEX_COLUMNS, DEST / "index", "part")
    assert sum(item["rows"] for item in detail_files) == len(records)
    assert sum(item["rows"] for item in index_files) == len(records)
    assert len(detail_paths) == len(records)

    manifest = {
        "feed": "reach-agent-feed",
        "schema_version": 1,
        "source": {
            "path": SOURCE.as_posix(),
            "bytes": len(source_bytes),
            "sha256": sha256_bytes(source_bytes),
            "rows": len(records),
        },
        "index": {"columns": INDEX_COLUMNS, "files": index_files},
        "details": {"columns": detail_columns, "files": detail_files},
        "record_id_note": (
    "Record ID is snapshot-specific. "
    "REACH UID is the permanent record identifier."
),
        "retrieval_note": "Read every index shard for global duplicate checks; follow Detail File only for candidates needing full fields.",
    }
    manifest_path = DEST / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"REACH feed created from {len(records):,} source records")
    print(f"Index files: {len(index_files)}; detail files: {len(detail_files)}")
    print(f"All shards <= {MAX_BYTES:,} bytes; original CSV unchanged")
    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
