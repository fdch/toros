from config import dbconfig
import mysql.connector

import random


def show_companies(number, cnx):
    cursor = cnx.cursor()

    print(f"Show {number} companies:\n")

    query = (
        "SELECT name, company_id FROM companies " "WHERE company_id BETWEEN %s AND %s"
    )

    limit = random.randint(number // 2, 1000 - number // 2)  # type: ignore

    cursor.execute((query), (limit - number // 2, limit + number // 2))

    for (name, company_id) in cursor:
        print(f"name: {name}, id: {company_id}")
    cursor.close()
    print("-" * 20)


cnx = mysql.connector.connect(**dbconfig)

show_companies(10, cnx)

cnx.close()
