import json
import os
from typing import Dict, Any

EDA_REPORTS: Dict[str, Dict[str, Any]] = {}
REPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "eda_reports")

for fname in os.listdir(REPORTS_DIR):
    if fname.endswith(".json"):
        pid = fname[:-5]
        with open(os.path.join(REPORTS_DIR, fname), encoding="utf-8") as f:
            EDA_REPORTS[pid] = json.load(f)
