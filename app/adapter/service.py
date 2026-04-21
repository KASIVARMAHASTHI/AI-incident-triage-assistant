class IncidentAdapter:
    def normalize(self, payload: dict) -> dict:
        return {
            "incident": payload,
            "status": "normalized"
        }