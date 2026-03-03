# Analyzer Fitness Data

Work-in-progress Python project for generating and analyzing synthetic fitness data.

The project will simulate users and their trainings, load data into a SQL database,
and run analytical queries.

## Current status

At the moment the project supports:

- generating synthetic users and trainings data
- reproducible results using random seeds
- exporting data to CSV files

Generated files:
- users.csv
- trainings.csv

## Planned features

- command line arguments support
- loading CSV files into SQLite database
- basic statistical analysis with pandas

## Tech stack

- Python 3
- pandas
- SQLite (planned)
- standard library (datetime, random, pathlib)

## How to run

```bash
python src/generate_data.py
```

Generated CSV files will be saved in the data/ directory.
