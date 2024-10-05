from models.vectorizer import SentenceTransformerWrapper, VectorizerBase


class VectorizerFactory:
    @staticmethod
    def get_model(model_id: str) -> VectorizerBase:
        models: dict[str, VectorizerBase] = {}

        model = models.get(model_id)
        if model is None:
            model = SentenceTransformerWrapper(model_id)
            return model
        else:
            return model(model_id)
