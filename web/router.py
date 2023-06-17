from fastapi import APIRouter
from web.healthcheck.handlers import router as healthcheck_router

router = APIRouter(prefix="/api")
router.include_router(healthcheck_router)
