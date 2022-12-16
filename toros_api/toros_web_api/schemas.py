from datetime import datetime
from typing import Optional

# from typing import List

from pydantic import BaseModel

# __tablename__ = "deals"
# deal_id = Column(Integer, primary_key=True, index=True)
# date = Column(DateTime)
# company_id = Column(Integer, ForeignKey("companies.id"))
# funding_amount = Column(Float)
# funding_round = Column(String)

# dealer = relationship("Company", back_populates="deals")


class DealBase(BaseModel):
    deal_id: int
    date: datetime
    company_id: int
    funding_amount: Optional[float]
    funding_round: str


class DealCreate(DealBase):
    pass


class Deal(DealBase):

    # dealer: int

    class Config:
        orm_mode = True


#  __tablename__ = "companies"
#     company_id = Column(Integer, primary_key=True, index=True)
#     founding_date = Column(DateTime)
#     name = Column(String)
#     description = Column(Text)
#     country = Column(String)

#     deals = relationship("Deal", back_populates="dealer")


class CompanyBase(BaseModel):
    company_id: int
    founding_date: Optional[datetime]
    name: str
    description: Optional[str]
    country: Optional[str]


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    # deals: List[Deal] = []

    class Config:
        orm_mode = True
