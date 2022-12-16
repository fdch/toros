import os
from dotenv import load_dotenv

# grab db settings from environment files into dbconfig object
load_dotenv("../toros_api/config/.env")
load_dotenv("../toros_api/config/config.toml")

print("DOTENV CONFIG")

dbconfig = {
    "user": os.getenv("user"),
    "password": os.getenv("DB_PASS"),
    "host": "localhost",
    "port": 3306,
    "database": os.getenv("db_name"),
}

print(dbconfig)

print("END CONFIG")
