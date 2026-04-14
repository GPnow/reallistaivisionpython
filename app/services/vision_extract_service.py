from app.schemas import ExtractResponse, ExtractVisionRequest


async def extract_vision(payload: ExtractVisionRequest) -> ExtractResponse:
    evidences = []
    for index, document in enumerate(payload.documents, start=1):
        evidences.append(
            {
                "evidenceType": "measurement",
                "confidence": 0.55,
                "raw": {
                    "document": document.model_dump(),
                    "index": index,
                    "profile": payload.profile,
                },
                "normalized": {
                    "label": document.file_name or f"vision-{index}",
                    "source_type": "vision_stub",
                    "profile": payload.profile,
                },
            }
        )

    return ExtractResponse(
        status="review_pending",
        evidences=evidences,
        summary={"document_count": len(payload.documents), "profile": payload.profile},
        resultMeta={"profile": payload.profile},
    )
