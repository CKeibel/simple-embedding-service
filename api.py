from dynaconf import settings
from fastapi import APIRouter, Depends

from schemas import EmbeddingRequest, EmbeddingResponse, ModelChangeRequest
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


@router.post("/change_model")
def change_model(
    request: ModelChangeRequest,
    service: VectorService = Depends(
        lambda: VectorService.create_service(settings.MODEL_ID)
    ),
) -> dict[str, str]:
    service.change_model(request.model_id)
    return {"message": "Model changed successfully!"}


@router.get("/loaded_model")
def loaded_model(
    service: VectorService = Depends(
        lambda: VectorService.create_service(settings.MODEL_ID)
    ),
) -> dict[str, str]:
    return {"model_id": service.model_id}


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
