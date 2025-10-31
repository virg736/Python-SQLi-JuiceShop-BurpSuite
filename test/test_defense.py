import sqlite3
import defense

def setup_module(module):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        name TEXT
    )""")
    c.execute("INSERT OR IGNORE INTO users (email, name) VALUES (?, ?)", ("test@example.com", "Test User"))
    conn.commit()
    conn.close()

def test_valid_email():
    assert defense.is_safe_input("test@example.com") is True

def test_invalid_payload():
    assert defense.is_safe_input("' OR 1=1--") is False
