import os
import datetime
import logging
import sqlite3
import argparse
from pathlib import Path

from db_config import *


#==================
# Logging
#==================
def init_logger(logger:logging.Logger, output:str,
                verbose:bool=False):
    stream_handler = logging.StreamHandler()
    if verbose:
        stream_handler.setLevel(logging.DEBUG)
    else:
        stream_handler.setLevel(logging.INFO)
    ch_formatter = logging.Formatter('%(levelname)s:%(message)s')
    stream_handler.setFormatter(ch_formatter)

    file_handler = logging.FileHandler(output)
    fh_formatter = logging.Formatter('%(asctime)s: %(levelname)s - %(message)s')
    file_handler.setFormatter(fh_formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)


#==================
# Arguments
#==================
def parse_arguments()->dict:

    parser = argparse.ArgumentParser(description="Create an sqlite database for the Lego dataset with the provided schema.")
    parser.add_argument("-in", "--input_dir", type=str, default=INPUT_PATH,
        dest="input_dir", help="Path to input .csv directory.")
    parser.add_argument("-out", "--output_db", type=str, default=OUTPUT_FILE,
        dest="output_db", help="Filename to use for sqlite database.")
    parser.add_argument("-delete", "--delete_db", type=bool, default=True,
        dest="del_db", help="If the db already exists in the output path, delete and rebuild it.")
    args = parser.parse_args()
    return vars(args)

#==================
# DB funcs
#==================
def create_connection(db:str)->sqlite3.connect:
    """ Creates connection to specified database file
    :param db: location of db file
    :return: DB connection object or none
    """
    try:
        conn = sqlite3.connect(db)
        LOGGER.debug("Connected to the database")
        return conn
    except Exception as e:
        LOGGER.exception(e)


def create_table(conn, sql_create_table:str):
    """ Creates database table from to SQL statement
    :param conn: db connection object
    :param sql_create_table: CREATE TABLE SQL statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Exception as e:
        LOGGER.exception(e)


def make_database(output_path:Path, output:str):
    database = output_path / output

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
    create_table(conn, sets_table)
    create_table(conn, themes_table)
    create_table(conn, inventories_table)
    create_table(conn, parts_table)
    create_table(conn, categories_table)
    create_table(conn, colors_table)
    create_table(conn, invpart_table)
    create_table(conn, invsets_table)


#==================
# Main script
#==================
def main():
    DATE_TIME = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_dir = Path("data/db")

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    #------------------
    # Arguments
    #------------------
    args = parse_arguments()
    input_dir = args['input_dir']
    output_db = args['output_db']
    del_db = args['del_db']

    #------------------
    # Logger
    #------------------
    LOGGER = logging.getLogger('db_creator')
    LOGGER.setLevel(logging.DEBUG)
    LOGGER_OUTPUT = os.path.join(output_dir, DATE_TIME + '.log')
    init_logger(LOGGER, LOGGER_OUTPUT)
    LOGGER.info('Initialised logger')


if __name__ == '__main__':
    main()
