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
        help="Path to input .csv directory.")
    parser.add_argument("-out", "--output_dir", type=str, default=OUTPUT_PATH,
        help="Path to use for sqlite database.")
    parser.add_argument("-delete", "--delete_db", type=bool, default=True,
        help="If the db already exists in the output path, delete and rebuild it.")
    args = parser.parse_args()
    return vars(args)

#==================
# DB funcs
#==================
def create_connection(db):
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


#==================
# Main script
#==================
def main():
    #------------------
    # Arguments
    #------------------

    #------------------
    # Logger
    #------------------
    LOGGER = logging.getLogger('db_creator')
    LOGGER.setLevel(logging.DEBUG)
    LOGGER_OUTPUT = os.path.join(output_dir, DATE_TIME + '.log')
    init_logger(LOGGER, LOGGER_OUTPUT)

    LOGGER.info('Initialised logger')
