import json

import mysql.connector
from mysql.connector import errorcode
from config import dbconfig
from schemas import create_tables, add_data, shape_data

cnx = mysql.connector.connect(**dbconfig)
cursor = cnx.cursor()

# cursor.execute("DROP TABLE IF EXISTS deals")
# cursor.execute("DROP TABLE IF EXISTS companies")

for f in ("companies", "deals"):
    datafile = "../data/challenge_" + f + ".json"
    print(f"{datafile}: Begin loading.")

    # create tables
    try:
        print(f"{f}: Creating table")
        cursor.execute(create_tables[f])
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print(f"{f}: already exists.")
        else:
            raise Exception(err.msg)
    else:
        print(f"{f}: table created.")

    # load data from json files
    data = {}
    try:
        print(f"{f}: Loading data file.")
        with open(datafile) as fp:
            data = json.load(fp)
    except Exception as e:
        print(f"{f}: See ERROR log below")
        raise e
    else:
        print(f"{f}: Data loaded.")

    # insert data to the tables
    try:
        print(f"{f}: Inserting data into table.")
        for k, v in data.items():
            # print(k, shape_data[f](v))
            try:
                cursor.execute(add_data[f], shape_data[f](k, v))
                cnx.commit()
            except mysql.connector.IntegrityError as err:
                # skip loaded entries if we ran this before
                print(f"{f}: skipping entry {k}, already loaded.")
                continue

    except Exception as e:
        print(f"{f}: See ERROR log below")
        raise e
    else:
        print(f"{f}: Data inserted.")

    print(f"{datafile}: loading ended.")

cnx.close()
