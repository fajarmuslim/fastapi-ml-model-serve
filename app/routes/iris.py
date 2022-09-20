from fastapi import APIRouter
from app.schemas.iris import IrisSingleRequest, IrisSingleResponse, IrisBatchRequest, IrisBatchResponse
from app.services.iris import IrisPredictor

router = APIRouter(prefix="/iris", tags=["Iris"])
iris_predictor = IrisPredictor()


@router.post(
    "/single",
    response_model=IrisSingleResponse,
    name="POST single iris",
)
def single_iris_prediction(request: IrisSingleRequest):
    return iris_predictor.get_single_prediction(feature=request)


@router.post(
    "/batch",
    response_model=IrisBatchResponse,
    name="POST batch iris",
)
def batch_iris_prediction(request: IrisBatchRequest):
    return iris_predictor.get_batch_prediction(features=request.features)
