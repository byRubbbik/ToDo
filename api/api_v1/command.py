from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta

from core.models import db_helper
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.commands,
    tags=["Users"]
)


@router.post("/create")
async def create(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    ...


@router.post("/add")
async def add(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    ...