import sys, os
import sqlite3
import pytest

# Ajout du dossier parent au chemin d'import pour accéder à defense.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import defense  # Import du module principal à tester


def setup_module(module):
    """Prépare un environnement de test minimal avec une base SQLite."""
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            name TEXT
        )
    """)
    c.execute(
        "INSERT OR IGNORE INTO users (email, name) VALUES (?, ?)",
        ("test@example.com", "Test User")
    )
    conn.commit()
    conn.close()


def test_valid_email():
    """Teste une entrée valide (aucun motif suspect)."""
    assert defense.is_safe_input("test@example.com") is True


def test_invalid_payload():
    """Teste une entrée contenant un motif SQL suspect."""
    assert defense.is_safe_input("' OR 1=1--") is False


def test_sql_keywords():
    """Teste la détection de mots-clés SQL interdits."""
    assert defense.is_safe_input("SELECT * FROM users") is False


def test_normal_text():
    """Teste un texte normal sans risque d'injection."""
    assert defense.is_safe_input("Bonjour tout le monde !") is True