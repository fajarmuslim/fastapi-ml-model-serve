from typing import List
from pydantic import BaseModel

class IrisSingleRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width:float


class IrisBatchRequest(BaseModel):
    features: List[IrisSingleRequest]


class IrisSingleResponse(BaseModel):
    result: int


class IrisBatchResponse(BaseModel):
    result: List[int]
