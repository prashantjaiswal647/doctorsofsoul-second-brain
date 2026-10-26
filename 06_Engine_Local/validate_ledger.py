"""
Ad Spend Ledger Validator
Doctors of Soul - Obsidian Second Brain Engine
Zero-dependency CSV validator and unit-economics analyzer.
"""

import csv
import sys
from pathlib import Path

# Fix Windows console encoding for UTF-8 currency symbols
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

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

def format_currency(val: float) -> str:
    try:
        return f"₹{val:,.2f}"
    except Exception:
        return f"INR {val:,.2f}"

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

    angle_stats = {}

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

                # Aggregate by angle
                angle = row["angle"]
                if angle not in angle_stats:
                    angle_stats[angle] = {"spend": 0.0, "clicks": 0, "bookings": 0, "revenue": 0.0}
                angle_stats[angle]["spend"] += spend
                angle_stats[angle]["clicks"] += clicks
                angle_stats[angle]["bookings"] += bookings
                angle_stats[angle]["revenue"] += revenue

            except ValueError as ve:
                errors.append(f"Line {line_num}: Type conversion error ({ve})")

    print("\n" + "=" * 60)
    print("DOCTORS OF SOUL - AD SPEND LEDGER SUMMARY")
    print("=" * 60)
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

        print("-" * 60)
        print(f"Total Spend      : {format_currency(total_spend)}")
        print(f"Total Clicks     : {total_clicks:,}")
        print(f"Total Bookings   : {total_bookings:,} sales")
        print(f"Total Revenue    : {format_currency(total_revenue)}")
        print(f"Blended CPC      : {format_currency(avg_cpc)}")
        print(f"Blended CAC      : {format_currency(avg_cac)}" if total_bookings > 0 else "Blended CAC      : N/A (0 bookings)")
        print(f"Front-End ROAS   : {overall_roas:.2f}x")
        print("-" * 60)
        print("PERFORMANCE BY CREATIVE ANGLE:")
        for angle, data in angle_stats.items():
            a_cac = (data["spend"] / data["bookings"]) if data["bookings"] > 0 else 0.0
            a_cpc = (data["spend"] / data["clicks"]) if data["clicks"] > 0 else 0.0
            a_roas = (data["revenue"] / data["spend"]) if data["spend"] > 0 else 0.0
            print(f"\n* Angle: {angle}")
            print(f"  - Spend: {format_currency(data['spend'])} | Sales: {data['bookings']} | Revenue: {format_currency(data['revenue'])}")
            print(f"  - CPC: {format_currency(a_cpc)} | CAC: {format_currency(a_cac)} | ROAS: {a_roas:.2f}x")
    else:
        print("\nLedger is currently empty (ready for intake data logging).")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    default_csv = Path(__file__).resolve().parent.parent / "02_Budget_Finances" / "ad_spend_logs.csv"
    validate_and_analyze(default_csv)
