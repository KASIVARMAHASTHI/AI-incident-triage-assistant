class LLMTriage:
    def analyze(self, incident: dict) -> dict:
        return {
            "severity": "high",
            "root_cause": "Possible database latency",
            "confidence": 0.82
        }