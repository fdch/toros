from typing import List
from fastapi import APIRouter, Depends
from ..utils.db import get_db
from sqlalchemy.orm import Session
from .. import schemas, services

router = APIRouter()


@router.get("/deals", response_model=List[schemas.Deal])
async def get_deals(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    deals = services.get_deals(db=db, skip=skip, limit=limit)
    return deals


@router.get("/deals_by_company/{company_id}", response_model=List[schemas.Deal])
async def get_deals_by_company_id(company_id: int, db: Session = Depends(get_db)):
    companies = services.get_deals_by_company_id(db=db, company_id=company_id)
    return companies
