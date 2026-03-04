from pathlib import Path
import pandas as pd
import sqlite3

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR/"data"
SQL_DIR = BASE_DIR/"sql"
DB_PATH = BASE_DIR/"fitness.db"


def run_sql_file(conn, filename):
    sql_path = SQL_DIR/filename
    sql_text = sql_path.read_text(encoding="utf-8")
    conn.executescript(sql_text)
    conn.commit()


def main():
    users = pd.read_csv(DATA_DIR/"users.csv")
    trainings = pd.read_csv(DATA_DIR/"trainings.csv")

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")

    run_sql_file(conn, "create_tables.sql")

    users.to_sql("users", conn, if_exists="append", index=False)
    trainings.to_sql("trainings", conn, if_exists="append", index=False)


if __name__ == "__main__":
    main()
