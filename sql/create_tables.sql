DROP TABLE IF EXISTS trainings;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL CHECK (gender IN ('M', 'F'))
);

CREATE TABLE trainings (
    training_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    activity_type TEXT NOT NULL,
    duration_minutes INTEGER NOT NULL CHECK (duration_minutes > 0),
    calories INTEGER NOT NULL CHECK (calories >= 0),
    date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
