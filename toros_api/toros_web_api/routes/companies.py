from typing import List
from fastapi import APIRouter, Depends
from ..utils.db import get_db
from sqlalchemy.orm import Session
from .. import schemas, services

router = APIRouter()


@router.get("/companies", response_model=List[schemas.Company])
async def get_companies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    companies = services.get_companies(db=db, skip=skip, limit=limit)
    return companies


@router.get("/company_deals/{company_id}", response_model=List[schemas.Company])
async def get_companies(company_id: int, db: Session = Depends(get_db)):
    companies = services.get_companies_by_id(db=db, company_id=company_id)
    return companies
