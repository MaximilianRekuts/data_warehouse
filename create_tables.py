import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    this function iterates over the drop table queries and executes
    inputs:
    - cur the cursor variable of the database
    - conn the connection variable of the database
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    this function iterates over the create table queries and executes
    inputs:
    - cur the cursor variable to the database
    - conn the connection variable to the database
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    this function connects to the database using the credentials in the config file and then drops and recreates the required tables.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
