# Analyzer Fitness Data

Python project for generating and analyzing synthetic fitness data.

The project simulates users and their trainings, exports data to CSV files,
loads it into a SQLite database, and prepares it for further SQL analysis.

---

## Current status

The project currently supports:

- generates synthetic users and trainings data (with reproducible random seed)
- exports data to CSV files
- creates a SQLite database schema from SQL scripts
- loads CSV data into the database
- runs analytical SQL queries
- exports reports to CSV
- generates basic charts using matplotlib

---

## Project workflow

1. Generate synthetic data
2. Create database schema
3. Load data into SQLite
4. Run analytical queries
5. Export reports and charts

---

## Generated files

After running the generator:

- `data/users.csv`
- `data/trainings.csv`

After loading data into database:

- `fitness.db`

---

## Example outputs

Charts are saved in the `output/` directory.
- Total calories by activity
- Daily calories trend
- Top 5 users by total calories

---

## Database schema

Tables:

### users
- `user_id` (PRIMARY KEY)
- `age`
- `gender`

### trainings
- `training_id` (PRIMARY KEY)
- `user_id` (FOREIGN KEY → users.user_id)
- `activity_type`
- `duration_minutes`
- `calories`
- `date`

Foreign keys and basic constraints are enabled.

---

## Tech stack

- Python 3
- pandas
- SQLite
- matplotlib
- standard library (datetime, random, pathlib, sqlite3)

---

## How to run

### Generate CSV data

```bash
python src/generate_data.py
```

### Load data into SQLite

```bash
python src/load_data.py
```

This will create: `fitness.db`

### Run analysis

```bash
python src/analysis.py
```

Reports and charts will be saved in: `output/`

## Why I built this

The goal was to practice:
- building small data pipelines
- working with SQL from Python
- structuring a project beyond a single script
- exporting results and visualizing them
