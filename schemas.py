from pydantic import BaseModel, Field


class EmbeddingRequest(BaseModel):
    texts: str | list[str] = Field(
        example=["This is my first sentence.", "This is my second sentence."]
    )


class EmbeddingResponse(BaseModel):
    embeddings: list[float] | list[list[float]]
