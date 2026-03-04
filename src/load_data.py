from pathlib import Path
import pandas as pd
from sql_utils import get_connection
from sql_utils import run_sql_file

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR/"data"


def main():
    users = pd.read_csv(DATA_DIR/"users.csv")
    trainings = pd.read_csv(DATA_DIR/"trainings.csv")

    conn = get_connection()
    run_sql_file(conn, "create_tables.sql")

    users.to_sql("users", conn, if_exists="append", index=False)
    trainings.to_sql("trainings", conn, if_exists="append", index=False)


if __name__ == "__main__":
    main()
