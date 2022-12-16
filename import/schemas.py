from helpers import *

# company
# "0": {
#   "name":"Mayer and Sons",
#   "country":"Sweden",
#   "founding_date":"2021-06-11T02:09:34Z",
#   "description":"Secured scalable standardization",
#   "company_id":1
# }

# deals
# "0":{
#   "date":1640907534000,
#   "funding_amount":1692194.0,
#   "funding_round":"Series A",
#   "company_id":104
# }

create_tables = {
    "companies": (
        "CREATE TABLE `companies` ("
        "  `company_id` INT(11) AUTO_INCREMENT,"
        "  `founding_date` DATETIME,"
        "  `name` VARCHAR(255),"
        "  `description` TEXT,"
        "  `country` VARCHAR(50),"
        " PRIMARY KEY (`company_id`)"
        ") ENGINE=InnoDB"
    ),
    "deals": (
        "CREATE TABLE `deals` ("
        "  `deal_id` INT(11) AUTO_INCREMENT,"
        "  `date` DATETIME NOT NULL,"
        "  `company_id` INT(11) NOT NULL,"
        "  `funding_amount` DECIMAL(11,2),"
        "  `funding_round` VARCHAR(100),"
        "  PRIMARY KEY (`deal_id`),"
        "  CONSTRAINT `deals_ibfk_1` FOREIGN KEY (`company_id`) "
        "     REFERENCES `companies` (`company_id`) ON DELETE CASCADE"
        ") ENGINE=InnoDB"
    ),
}

add_data = {
    "companies": (
        "INSERT INTO companies "
        "(company_id, founding_date, name, description, country) "
        "VALUES (%s, %s, %s, %s, %s)"
    ),
    "deals": (
        "INSERT INTO deals "
        "(deal_id, date, company_id, funding_amount, funding_round) "
        "VALUES (%s, %s, %s, %s, %s)"
    ),
}

shape_data = {
    # skip companies index input but keep the same signature
    "companies": lambda _, v: (
        v["company_id"],
        datefromiso(v["founding_date"]),
        v["name"],
        v["description"],
        v["country"],
    ),
    "deals": lambda i, v: (
        i,  # the deal id
        datefromtimestamp(v["date"]),
        v["company_id"],
        v["funding_amount"],
        v["funding_round"],
    ),
}
