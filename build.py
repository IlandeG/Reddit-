#!/usr/bin/env python3
"""Build a single self-contained index.html infographic from data/master.csv.

The CSV is the MASTER ("Raw Data") tab of the analytics spreadsheet in long
format: brand, platform, period, period_type, scope, metric, value, ...
The BRAND and DEMOGRAPHICS views are recomputed in the browser from this data,
so this one CSV drives the whole infographic.

Usage:
    python3 build.py            # reads data/master.csv -> writes index.html

To refresh the data, re-export the spreadsheet's first tab as CSV into
data/master.csv and run this script again.
"""

import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "data", "master.csv")
TEMPLATE_PATH = os.path.join(HERE, "template.html")
OUT_PATH = os.path.join(HERE, "index.html")


def load_records(path):
    records = []
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            raw = (row.get("value") or "").strip()
            if raw == "":
                continue
            try:
                value = float(raw)
            except ValueError:
                continue
            records.append({
                "b": (row.get("brand") or "").strip(),
                "p": (row.get("platform") or "").strip(),
                "t": (row.get("period") or "").strip(),
                "s": (row.get("scope") or "").strip(),
                "m": (row.get("metric") or "").strip(),
                "v": value,
            })
    return records


def main():
    records = load_records(CSV_PATH)
    brands = sorted({r["b"] for r in records if r["b"]})
    platforms = sorted({r["p"] for r in records if r["p"]})
    periods = sorted({r["t"] for r in records if r["t"]})
    metrics = sorted({r["m"] for r in records if r["m"]})

    meta = {
        "brands": brands,
        "platforms": platforms,
        "periods": periods,
        "metrics": metrics,
        "rowCount": len(records),
    }

    payload = {"meta": meta, "records": records}

    with open(TEMPLATE_PATH, encoding="utf-8") as fh:
        template = fh.read()

    html = template.replace(
        "/*__DATA__*/null",
        json.dumps(payload, separators=(",", ":"), ensure_ascii=False),
    )

    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(html)

    print(f"Wrote {OUT_PATH}")
    print(f"  records : {len(records)}")
    print(f"  brands  : {len(brands)}")
    print(f"  platforms: {len(platforms)}")
    print(f"  periods : {len(periods)} ({periods[0]} .. {periods[-1]})")
    print(f"  metrics : {len(metrics)}")


if __name__ == "__main__":
    main()
