from pathlib import Path
from sql_utils import get_connection
from sql_utils import read_sql_query

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR/"fitness.db"
SQL_DIR = BASE_DIR/"sql"
OUTPUT_DIR = BASE_DIR/"output"


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    conn = get_connection()
    df_activity = read_sql_query(conn, "activity.sql")
    df_daily = read_sql_query(conn, "daily.sql")

    df_activity.to_csv(OUTPUT_DIR / "activity_report.csv", index=False)
    df_daily.to_csv(OUTPUT_DIR / "daily_report.csv", index=False)


if __name__ == "__main__":
    main()
