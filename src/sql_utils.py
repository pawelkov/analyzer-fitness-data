import sqlite3
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR/"fitness.db"
SQL_DIR = BASE_DIR/"sql"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def run_sql_file(conn, filename):
    sql_path = SQL_DIR/filename
    sql_text = sql_path.read_text(encoding="utf-8")
    conn.executescript(sql_text)
    conn.commit()


def read_sql_query(conn, filename):
    sql_path = SQL_DIR/filename
    sql_text = sql_path.read_text(encoding="utf-8")
    return pd.read_sql_query(sql_text, conn)
