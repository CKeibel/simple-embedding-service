from abc import ABC, abstractmethod

import torch
from sentence_transformers import SentenceTransformer


class VectorizerBase(ABC):
    @abstractmethod
    def vectorize(self, inputs: str | list[str]) -> list[list[float]]:
        pass


class SentenceTransformerWrapper(VectorizerBase):
    def __init__(self, model_id: str):
        self.model_id = model_id
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer(model_id, trust_remote_code=True).to(
            self.device
        )

    def vectorize(self, inputs: str | list[str]) -> list[list[float]]:
        return self.model.encode(inputs).tolist()


class OpenAIWrapper(VectorizerBase):
    pass
