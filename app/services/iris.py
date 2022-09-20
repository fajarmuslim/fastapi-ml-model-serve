from typing import Dict, List
from joblib import load
from app.schemas.iris import IrisSingleRequest
from app.utils.constant import MODEL_PATH


class IrisPredictor:
    def __init__(self):
        self.model = load(MODEL_PATH)


    def get_single_prediction(self, feature: IrisSingleRequest) -> Dict[str, List[int]]:
        formatted_features = [[feature.sepal_length,feature.sepal_width,feature.petal_length,feature.petal_width]]
        result = self.model.predict(formatted_features)
        print({"result": result.tolist()[0]})
        return {"result": result.tolist()[0]}


    def get_batch_prediction(self, features: List[IrisSingleRequest]) -> Dict[str, List[int]]:
        formatted_features = [[item.sepal_length,item.sepal_width,item.petal_length,item.petal_width] for item in features]
        result = self.model.predict(formatted_features)

        return {"result": result.tolist()}
