import json
import csv
from typing import List, Dict, Any


def read_json(file_path: str) -> Any:
    with open(file_path, "r") as f:
        return json.load(f)


def write_json(file_path: str, data: Any):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)


def read_csv(file_path: str) -> List[Dict]:
    with open(file_path, "r") as f:
        return list(csv.DictReader(f))


def write_csv(file_path: str, data: List[Dict], fieldnames: List[str] = None):
    if not data:
        return
    fieldnames = fieldnames or list(data[0].keys())
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
