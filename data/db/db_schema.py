import sqlite3
from db_insertion import create_connection

def create_table(conn, sql_create_table):
    """ Creates database table from to SQL statement
    :param conn: db connection object
    :param sql_create_table: CREATE TABLE SQL statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Exception as e:
        print(e)

def main():
    database = "./data/db/lego_db_test.db"

    sets_table = """CREATE TABLE sets (
        set_num TEXT PRIMARY KEY,
        name TEXT,
        year INTEGER,
        theme_id INTEGER REFERENCES themes(id),
        num_parts INTEGER
    );"""

    themes_table = """CREATE TABLE themes (
        id INTEGER PRIMARY KEY,
        name TEXT,
        parent_id INTEGER
    );"""

    inventories_table = """CREATE TABLE inventories (
        id INTEGER PRIMARY KEY,
        version INTEGER,
        set_num INTEGER REFERENCES sets(set_num)
    );"""

    parts_table = """CREATE TABLE parts (
        part_num TEXT PRIMARY KEY,
        part_name TEXT,
        part_cat_id INTEGER REFERENCES part_categories(id)
    );"""

    categories_table = """CREATE TABLE part_categories (
        id INTEGER PRIMARY KEY,
        name TEXT
    );"""

    colors_table = """CREATE TABLE colors (
        id INTEGER PRIMARY KEY,
        name TEXT,
        rgb TEXT,
        is_trans BOOLEAN
    );"""

    invpart_table = """CREATE TABLE inventory_parts (
        inventory_id INTEGER PRIMARY KEY REFERENCES inventories(id),
        part_num TEXT REFERENCES parts(part_num),
        color_id INTEGER REFERENCES colors(id),
        quantity INTEGER,
        is_spare BOOLEAN
    );"""

    invsets_table = """CREATE TABLE inventory_sets (
        inventory_id INTEGER PRIMARY KEY REFERENCES inventories(id),
        set_num TEXT REFERENCES sets(set_num),
        quantity INTEGER
    );"""

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sets_table)
        create_table(conn, themes_table)
        create_table(conn, inventories_table)
        create_table(conn, parts_table)
        create_table(conn, categories_table)
        create_table(conn, colors_table)
        create_table(conn, invpart_table)
        create_table(conn, invsets_table)
    else:
        print("Cannot create the database connection")


if __name__ == '__main__':
    main()
