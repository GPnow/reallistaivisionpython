from app.schemas import ExtractResponse, ExtractTablesRequest


async def extract_tables(payload: ExtractTablesRequest) -> ExtractResponse:
    evidences = []
    for index, document in enumerate(payload.documents, start=1):
        evidences.append(
            {
                "evidenceType": "row",
                "confidence": 0.6,
                "raw": {
                    "document": document.model_dump(),
                    "index": index,
                },
                "normalized": {
                    "label": document.file_name or f"document-{index}",
                    "source_type": "table_stub",
                },
            }
        )

    return ExtractResponse(
        status="review_pending",
        evidences=evidences,
        summary={"document_count": len(payload.documents)},
        resultMeta={"profile": "table_stub"},
    )
