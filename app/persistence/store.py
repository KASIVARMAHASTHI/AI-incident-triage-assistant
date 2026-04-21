import json
from pathlib import Path


class IncidentStore:
    def __init__(self, file_path="data/incidents.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self.file_path.write_text("[]")

    def save(self, record):
        data = json.loads(self.file_path.read_text())
        data.append(record)
        self.file_path.write_text(json.dumps(data, indent=2))
        return record

    def get(self, correlation_id):
        data = json.loads(self.file_path.read_text())
        for item in data:
            if item.get("correlation_id") == correlation_id:
                return item
        return {"status": "not_found"}
