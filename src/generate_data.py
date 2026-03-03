from pathlib import Path
#import argparse
import datetime as dt
import random
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

ACTIVITIES = ["RUNNING", "WALKING", "CYCLING", "STRENGHT", "SWIMMING"]


def generate_users(users, seed):
    random.seed(seed)
    
    rows = []
    for user_id in range(1, users+1):
        age = random.randint(18, 65)
        gender = random.choice(["M", "F"])
        rows.append((user_id, age, gender))

    return pd.DataFrame(rows, columns=["user_id", "age", "gender"])


def generate_trainings(trainings, users, start_date, days, seed):
    random.seed(seed+1)

    rows = []
    for training_id in range(1, trainings+1):
        user_id = random.randint(1, users)
        activity_type = random.choices(ACTIVITIES, weights=[0.3, 0.2, 0.2, 0.1, 0.1])[0]

        duration_minutes = random.randint(10, 120)
        calories = random.randint(1, 500)
        date = start_date + dt.timedelta(days=random.randint(0, days))

        rows.append((training_id, user_id, activity_type, duration_minutes, calories, date))

    return pd.DataFrame(rows, columns=["training_id", "user_id", "activity_type", "duration_minutes", "calories", "date"])


def main():
    DATA_DIR.mkdir(exist_ok=True)

    #args = parse_args()

    users = 10
    trainings = 30
    start_date = dt.date.fromisoformat("2026-01-01")
    days = 60
    seed = 17

    users_data = generate_users(users, seed)
    trainings_data = generate_trainings(trainings, users, start_date, days, seed)

    users_data.to_csv(DATA_DIR/"users.csv", index=False)
    trainings_data.to_csv(DATA_DIR/"trainings.csv", index=False)


if __name__ == "__main__":
    main()
