# Analyzer Fitness Data

Work-in-progress Python project for generating and analyzing synthetic fitness data.

The project simulates users and their trainings, exports data to CSV files,
loads it into a SQLite database, and prepares it for further SQL analysis.

---

## Current status

The project currently supports:

- generating synthetic users and trainings data
- reproducible results using random seeds
- exporting data to CSV files
- loading CSV data into a SQLite database
- creating database schema using SQL scripts

---

## Project workflow

1. Generate synthetic data (CSV)
2. Create database schema
3. Load CSV files into SQLite
4. Run analytical SQL queries (planned)

---

## Generated files

After running the generator:

- `data/users.csv`
- `data/trainings.csv`

After loading data into database:

- `fitness.db`

---

## Database schema

Tables:

### users
- user_id (PK)
- age
- gender

### trainings
- training_id (PK)
- user_id (FK → users.user_id)
- activity_type
- duration_minutes
- calories
- date

Foreign keys and basic constraints are enabled.

---

## Tech stack

- Python 3
- pandas
- SQLite
- standard library (datetime, random, pathlib, sqlite3)

---

## How to run

### Generate CSV data

```bash
python src/generate_data.py
python src/load_data.py
```

Database file will be created in the project root:
`fitness.db`
