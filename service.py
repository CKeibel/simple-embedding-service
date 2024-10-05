import torch

from models.factory import VectorizerFactory


class SingeltonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class VectorService(metaclass=SingeltonMeta):
    def __init__(self, model_id: str) -> None:
        self.model_id = model_id
        self.model = VectorizerFactory.get_model(self.model_id)

    def vectorize(self, inputs: str | list[str]) -> list[list[float]]:
        return self.model.vectorize(inputs)

    def change_model(self, model_id: str) -> None:
        self.model_id = model_id
        del self.model
        torch.cuda.empty_cache()
        self.model = VectorizerFactory.get_model(self.model_id)

    @classmethod
    def create_service(cls, model_id: str):
        return cls(model_id)
