from typing import Any

from pydantic import BaseModel, Field


class ExtractionDocumentRef(BaseModel):
    id: str | None = None
    file_name: str = Field(default="", alias="fileName")
    file_ref: str | None = Field(default=None, alias="fileRef")
    doc_ref: str | None = Field(default=None, alias="docRef")
    metadata: dict[str, Any] = Field(default_factory=dict)

    model_config = {
        "populate_by_name": True,
    }


class ExtractTablesRequest(BaseModel):
    session_id: str
    documents: list[ExtractionDocumentRef] = Field(default_factory=list)
    config: dict[str, Any] = Field(default_factory=dict)


class ExtractVisionRequest(ExtractTablesRequest):
    profile: str = "boq_extract"


class ExtractCadRequest(ExtractTablesRequest):
    adapter: str = "default"


class ExtractEvidence(BaseModel):
    evidenceType: str
    confidence: float | None = None
    raw: dict[str, Any] = Field(default_factory=dict)
    normalized: dict[str, Any] = Field(default_factory=dict)


class ExtractResponse(BaseModel):
    status: str = "review_pending"
    evidences: list[ExtractEvidence] = Field(default_factory=list)
    summary: dict[str, Any] = Field(default_factory=dict)
    resultMeta: dict[str, Any] = Field(default_factory=dict)
    error: str | None = None
