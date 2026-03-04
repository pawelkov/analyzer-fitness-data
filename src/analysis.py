from pathlib import Path
from sql_utils import get_connection
from sql_utils import read_sql_query
import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR/"output"


def plotting(df_activity, df_daily, df_top_users):

    plt.figure()
    plt.bar(df_activity["activity_type"], df_activity["total_calories"])
    plt.title("Total calories by activity")
    plt.xlabel("Activity")
    plt.ylabel("Total calories")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "total_calories_by_activity.png")
    plt.show()

    df_daily["date"] = pd.to_datetime(df_daily["date"])
    plt.figure()
    plt.plot(df_daily["date"], df_daily["total_calories"], marker="o")
    plt.title("Daily calories trend")
    plt.xlabel("Date")
    plt.ylabel("Total calories")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "daily_calories_trend.png")
    plt.show()

    plt.figure()
    plt.bar(df_top_users["user_id"].astype(str), df_top_users["total_calories"])
    plt.title("Top 5 users by total calories")
    plt.xlabel("User ID")
    plt.ylabel("Total calories")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "top_users_total_calories.png")
    plt.show()


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    conn = get_connection()
    df_activity = read_sql_query(conn, "activity.sql")
    df_daily = read_sql_query(conn, "daily.sql")
    df_top_users = read_sql_query(conn, "top_users.sql")

    df_activity.to_csv(OUTPUT_DIR / "activity_report.csv", index=False)
    df_daily.to_csv(OUTPUT_DIR / "daily_report.csv", index=False)
    df_top_users.to_csv(OUTPUT_DIR / "top_users_report.csv", index=False)

    plotting(df_activity, df_daily, df_top_users)


if __name__ == "__main__":
    main()
