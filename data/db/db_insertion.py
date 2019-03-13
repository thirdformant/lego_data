import sqlite3
import pandas as pd


def create_connection(db):
    """ Creates connection to specified database file
    :param db: location of db file
    :return: DB connection object or none
    """
    try:
        conn = sqlite3.connect(db)
        print("hmm")
        return conn
    except Exception as e:
        print(e)


def main():
    database = "./data/db/lego_db_test.db"
    PATH = "./data/"

    conn = create_connection(database)
    if conn is not None:
        # Read all data from csv files
        print(f"Reading in raw data from {PATH}...")

        sets_csv = pd.read_csv(f"{PATH}raw/sets.csv")
        themes_csv = pd.read_csv(f"{PATH}raw/themes.csv")
        inventories_csv = pd.read_csv(f"{PATH}raw/inventories.csv")
        parts_csv = pd.read_csv(f"{PATH}raw/parts.csv")
        colors_csv = pd.read_csv(f"{PATH}raw/colors.csv")
        inventory_sets_csv = pd.read_csv(f"{PATH}raw/inventory_sets.csv")
        inventory_parts_csv = pd.read_csv(f"{PATH}raw/inventory_parts.csv")

        # Insert data into db
        print("Inserting data into db...")

        sets_csv.to_sql("sets", conn, if_exists='replace', index=False)
        themes_csv.to_sql("themes", conn, if_exists='replace', index=False)
        inventories_csv.to_sql("inventories", conn, if_exists="replace", index=False)
        parts_csv.to_sql("parts", conn, if_exists="replace", index=False)
        colors_csv.to_sql("colors", conn, if_exists="replace", index=False)
        inventory_sets_csv.to_sql("inventory_sets", conn, if_exists="replace", index=False)
        inventory_parts_csv.to_sql("inventory_parts", conn, if_exists="replace", index=False)

    else:
        print("Cannot create the database connection")


if __name__ == '__main__':
    main()
