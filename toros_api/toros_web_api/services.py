from sqlalchemy.orm import Session
from . import models


def get_companies(db=Session, skip: int = 0, limit: int = 10):
    companies = db.query(models.Company).offset(skip).limit(limit).all()
    return companies


def get_companies_by_id(db=Session, company_id: int = 0):
    companies = (
        db.query(models.Company).filter(models.Company.company_id == company_id).all()
    )
    return companies


def get_deals_by_company_id(db=Session, company_id: int = 0):
    deals = db.query(models.Deal).filter(models.Deal.company_id == company_id).all()
    return deals


def get_deals(db=Session, skip: int = 0, limit: int = 10):
    deals = db.query(models.Deal).offset(skip).limit(limit).all()
    return deals
