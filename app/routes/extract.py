from fastapi import APIRouter

from app.schemas import (
    ExtractCadRequest,
    ExtractResponse,
    ExtractTablesRequest,
    ExtractVisionRequest,
)
from app.services.cad_adapter_service import extract_cad_canonical
from app.services.table_extract_service import extract_tables
from app.services.vision_extract_service import extract_vision


router = APIRouter()


@router.post("/extract/tables", response_model=ExtractResponse)
async def extract_tables_route(payload: ExtractTablesRequest) -> ExtractResponse:
    return await extract_tables(payload)


@router.post("/extract/vision", response_model=ExtractResponse)
async def extract_vision_route(payload: ExtractVisionRequest) -> ExtractResponse:
    return await extract_vision(payload)


@router.post("/extract/cad", response_model=ExtractResponse)
async def extract_cad_route(payload: ExtractCadRequest) -> ExtractResponse:
    return await extract_cad_canonical(payload)
