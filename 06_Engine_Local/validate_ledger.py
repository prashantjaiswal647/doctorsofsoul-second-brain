"""Ledger check for the vault. The single source of truth is the repo ledger
(marketing/creative-performance.csv, Option A, 2026-10-27); this only runs the repo's tested report.
Set DOS_REPO if the repo is not the sibling folder 'doctorsofsoul'."""
import os
import subprocess
import sys
from pathlib import Path

repo = Path(os.environ.get("DOS_REPO") or Path(__file__).resolve().parents[2] / "doctorsofsoul")
tool = repo / "deploy" / "devtools" / "creative_report.py"
if not tool.exists():
    sys.exit(f"[ERROR] {tool} not found; set DOS_REPO to the doctorsofsoul checkout")
sys.exit(subprocess.run([sys.executable, str(tool), *sys.argv[1:]], cwd=repo).returncode)
