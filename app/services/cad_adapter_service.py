from app.schemas import ExtractCadRequest, ExtractResponse


async def extract_cad_canonical(payload: ExtractCadRequest) -> ExtractResponse:
    evidences = []
    for index, document in enumerate(payload.documents, start=1):
        evidences.append(
            {
                "evidenceType": "cad_group",
                "confidence": 0.5,
                "raw": {
                    "document": document.model_dump(),
                    "adapter": payload.adapter,
                    "index": index,
                },
                "normalized": {
                    "label": document.file_name or f"cad-{index}",
                    "source_type": "cad_stub",
                    "adapter": payload.adapter,
                },
            }
        )

    return ExtractResponse(
        status="review_pending",
        evidences=evidences,
        summary={"document_count": len(payload.documents), "adapter": payload.adapter},
        resultMeta={"adapter": payload.adapter},
    )
