import sqlite3

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
