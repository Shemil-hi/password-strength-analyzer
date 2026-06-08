import sqlite3
import hashlib


def init_db():
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS password_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password_hash TEXT
    )
    """)

    conn.commit()
    conn.close()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def check_reuse(password):
    hashed = hash_password(password)

    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM password_history WHERE password_hash=?",
        (hashed,)
    )

    result = cur.fetchone()

    conn.close()

    return result is not None


def save_password(password):

    hashed = hash_password(password)

    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO password_history(password_hash) VALUES(?)",
        (hashed,)
    )

    conn.commit()
    conn.close()
