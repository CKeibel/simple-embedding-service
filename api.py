from dynaconf import settings
from fastapi import APIRouter, Depends

from schemas import EmbeddingRequest, EmbeddingResponse
from service import VectorService

router = APIRouter()


@router.post("/embeddings", response_model=EmbeddingResponse)
def embed(
    inputs: EmbeddingRequest,
    service: VectorService = Depends(
        lambda: VectorService.create_service(settings.MODEL_ID)
    ),
):
    embeddings = service.vectorize(inputs.texts)
    return EmbeddingResponse(embeddings=embeddings)
