from fastapi import APIRouter

from core.config import settings
from .api_v1.users import router as user_router
from .api_v1.command import router as command_router

router = APIRouter(
    prefix=settings.api.v1.prefix
)

router.include_router(
    user_router,
)

router.include_router(
    command_router,
)