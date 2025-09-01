import requests
from datetime import datetime, timezone
from app.models.fireball_model import FireballRecord, FireballRecords
from app.models.cad_model import CADRecord, CADRecords

class FireballAPI:
    URL = 'https://ssd-api.jpl.nasa.gov/fireball.api'

    def fetch_data(self) -> FireballRecords:
        headers = {'Content-type': 'application/json'}
        response = requests.post(self.URL, headers=headers)
        response.raise_for_status()
        data = response.json()

        valid_records = []
        for item in data.get('data', []):
            record_dict = dict(zip(data['fields'], item))
            try:
                record = FireballRecord(**record_dict)
                valid_records.append(record)
            except Exception as e:
                print(f"Validation error for record {record_dict}: {e}")

        return FireballRecords(data=valid_records, metadata=datetime.now(timezone.utc).isoformat())

class CADAPI:
    URL = 'https://ssd-api.jpl.nasa.gov/cad.api'

    def fetch_data(self) -> CADRecords:
        headers = {'Content-type': 'application/json'}
        params = {
            "body": "ALL",
            "diameter": "true"
        }
        response = requests.post(self.URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        valid_records = []
        for item in data.get('data', []):
            record_dict = dict(zip(data['fields'], item))
            try:
                record = CADRecord(**record_dict)
                valid_records.append(record)
            except Exception as e:
                print(f"Validation error for record {record_dict}: {e}")

        return CADRecords(data=valid_records, metadata=datetime.now(timezone.utc).isoformat())
