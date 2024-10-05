from pydantic import BaseModel, ConfigDict, Field


class EmbeddingRequest(BaseModel):
    texts: str | list[str] = Field(
        example=["This is my first sentence.", "This is my second sentence."]
    )


class EmbeddingResponse(BaseModel):
    embeddings: list[float] | list[list[float]]


class ModelChangeRequest(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    model_id: str = Field(example="sentence-transformers/all-MiniLM-L6-v2")
