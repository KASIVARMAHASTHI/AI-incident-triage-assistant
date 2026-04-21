from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class IncidentAlert(BaseModel):
    incident_id: str = Field(..., description="Unique incident identifier")
    title: str = Field(..., description="Short incident title")
    description: str = Field(..., description="Detailed incident description")
    source: str = Field(..., description="Originating system or monitoring source")
    signals: List[str] = Field(default_factory=list, description="List of related alert or log signals")
    metrics: Dict[str, Any] = Field(default_factory=dict, description="Associated incident metrics")
    severity: Optional[str] = Field(default="medium", description="Severity level")


class IncidentRequest(BaseModel):
    tenant_id: Optional[str] = Field(default=None, description="Optional tenant identifier")
    correlation_id: str = Field(..., description="Correlation identifier for workflow tracking")
    alert: IncidentAlert
