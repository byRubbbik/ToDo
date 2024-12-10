from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta

from core.models import db_helper
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"]
)


@router.post("/register")
async def register(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    ...


@router.post("/auth")
async def auth(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    ...