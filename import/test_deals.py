from config import dbconfig
from helpers import iso
import mysql.connector
import datetime
import random


def get_company_name_by_id(company_id, cursor):
    try:
        q = """SELECT name FROM `companies` WHERE company_id = %s"""
        cursor.execute(q, (company_id,))
        return cursor.fetchone()[0]
    except Exception as e:
        print("ERROR", e)


def show_deals(start, stop, cnx):
    cursor = cnx.cursor(buffered=True)
    date_start = iso(start)
    date_stop = iso(stop)
    print(f"Show deals from {date_start} to {date_stop}:\n")

    query = (
        "SELECT company_id, funding_amount, date FROM deals "
        "WHERE date BETWEEN %s and %s"
    )
    cursor.execute((query), (date_start, date_stop))

    for (company_id, funding_amount, date) in cursor:
        name = get_company_name_by_id(company_id, cursor)
        print(f"{name} made a deal of ${funding_amount} on {date}")

    cursor.close()
    print("-" * 20)


cnx = mysql.connector.connect(**dbconfig)

sm, em = random.randint(1, 6), random.randint(1, 6)
show_deals(datetime.date(2021, sm, 1), datetime.date(2021, em + sm, 1), cnx)

cnx.close()
