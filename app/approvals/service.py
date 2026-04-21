class ApprovalService:
    def requires_approval(self, triage: dict) -> bool:
        return triage.get("severity") == "high"
