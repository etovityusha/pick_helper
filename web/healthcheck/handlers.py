
from fastapi import APIRouter
from .schemas import HealthcheckResponse

router = APIRouter(prefix="/healthcheck", dependencies=[], tags=["healthcheck"])


@router.get("/")
async def healthcheck() -> HealthcheckResponse:
    return HealthcheckResponse(is_ok=True)
