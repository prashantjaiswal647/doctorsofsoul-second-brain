"""
Ad Spend Ledger Validator
Doctors of Soul - Obsidian Second Brain Engine
Zero-dependency CSV validator and unit-economics analyzer.
"""

import csv
import sys
from pathlib import Path

REQUIRED_HEADERS = [
    "date",
    "campaign_name",
    "angle",
    "spend_inr",
    "clicks",
    "cpc_inr",
    "bookings",
    "revenue_inr",
    "roas",
]

def validate_and_analyze(csv_path: Path):
    if not csv_path.exists():
        print(f"[ERROR] Ledger file not found at: {csv_path}")
        sys.exit(1)

    total_spend = 0.0
    total_clicks = 0
    total_bookings = 0
    total_revenue = 0.0
    row_count = 0
    errors = []

    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        # Verify schema
        if reader.fieldnames != REQUIRED_HEADERS:
            missing = [h for h in REQUIRED_HEADERS if h not in (reader.fieldnames or [])]
            extra = [h for h in (reader.fieldnames or []) if h not in REQUIRED_HEADERS]
            if missing or extra:
                print(f"[SCHEMA ERROR] Invalid headers in {csv_path.name}")
                if missing:
                    print(f"  Missing: {missing}")
                if extra:
                    print(f"  Unexpected: {extra}")
                sys.exit(1)

        for line_num, row in enumerate(reader, start=2):
            row_count += 1
            try:
                spend = float(row["spend_inr"]) if row["spend_inr"] else 0.0
                clicks = int(row["clicks"]) if row["clicks"] else 0
                cpc = float(row["cpc_inr"]) if row["cpc_inr"] else 0.0
                bookings = int(row["bookings"]) if row["bookings"] else 0
                revenue = float(row["revenue_inr"]) if row["revenue_inr"] else 0.0
                roas = float(row["roas"]) if row["roas"] else 0.0

                if spend < 0 or clicks < 0 or bookings < 0 or revenue < 0:
                    errors.append(f"Line {line_num}: Negative values detected.")

                total_spend += spend
                total_clicks += clicks
                total_bookings += bookings
                total_revenue += revenue

            except ValueError as ve:
                errors.append(f"Line {line_num}: Type conversion error ({ve})")

    print("\n" + "=" * 50)
    print("DOCTORS OF SOUL - AD SPEND LEDGER SUMMARY")
    print("=" * 50)
    print(f"File Path        : {csv_path.resolve()}")
    print(f"Total Rows Logged: {row_count}")

    if errors:
        print("\n[VALIDATION WARNINGS / ERRORS]:")
        for err in errors:
            print(f"  - {err}")
    else:
        print("Schema Integrity : OK (100% Valid)")

    if row_count > 0:
        avg_cac = (total_spend / total_bookings) if total_bookings > 0 else 0.0
        avg_cpc = (total_spend / total_clicks) if total_clicks > 0 else 0.0
        overall_roas = (total_revenue / total_spend) if total_spend > 0 else 0.0

        print("-" * 50)
        print(f"Total Spend      : ₹{total_spend:,.2f}")
        print(f"Total Clicks     : {total_clicks:,}")
        print(f"Total Bookings   : {total_bookings:,}")
        print(f"Total Revenue    : ₹{total_revenue:,.2f}")
        print(f"Average CPC      : ₹{avg_cpc:,.2f}")
        print(f"Effective CAC    : ₹{avg_cac:,.2f}" if total_bookings > 0 else "Effective CAC    : N/A (0 bookings)")
        print(f"Aggregate ROAS   : {overall_roas:.2f}x")
    else:
        print("\nLedger is currently empty (ready for intake data logging).")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    default_csv = Path(__file__).resolve().parent.parent / "02_Budget_Finances" / "ad_spend_logs.csv"
    validate_and_analyze(default_csv)
