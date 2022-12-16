from .utils.db import Base

# from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey


# "  `company_id` INT(11) AUTO_INCREMENT,"
#         "  `founding_date` DATE,"
#         "  `name` VARCHAR(255),"
#         "  `description` TEXT,"
#         "  `country` VARCHAR(50),"
#         " PRIMARY KEY (`company_id`)"
class Company(Base):
    __tablename__ = "companies"
    company_id = Column(Integer, primary_key=True, index=True)
    founding_date = Column(DateTime)
    name = Column(String)
    description = Column(Text)
    country = Column(String)

    # deals = relationship("Deal", back_populates="dealer")


# "  `deal_id` INT(11) AUTO_INCREMENT,"
# "  `date` date NOT NULL,"
# "  `company_id` INT(11) NOT NULL,"
# "  `funding_amount` DECIMAL(11,2),"
# "  `funding_round` VARCHAR(100),"
# "  PRIMARY KEY (`deal_id`),"
# "  CONSTRAINT `deals_ibfk_1` FOREIGN KEY (`company_id`) "
# "     REFERENCES `companies` (`company_id`) ON DELETE CASCADE"
class Deal(Base):
    __tablename__ = "deals"
    deal_id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    company_id = Column(Integer, ForeignKey("companies.id"))
    funding_amount = Column(Float)
    funding_round = Column(String)

    # dealer = relationship("Company", back_populates="deals")
