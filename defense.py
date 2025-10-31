#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de défense contre les injections SQL - Projet 2
Analyse et filtre les entrées utilisateur pour détecter les tentatives d'injection SQL.
Utilise des requêtes paramétrées pour protéger la base de données.
Copyright (c) 2025 Virginie Lechene
License: MIT License
"""

import re
import sqlite3
import unicodedata
import urllib.parse
import logging

logging.basicConfig(level=logging.INFO)

# Liste de motifs suspects pour détection d'injection SQL
sql_patterns = [
    r"union\s+select",
    r"or\s+\d+\s*=\s*\d+",
    r"or\s+1\s*=\s*1",
    r"(--|;--|/\*)",
    r"drop\s+table",
    r"insert\s+into",
    r"update\s+\w+\s+set",
    r"delete\s+from",
    r"sleep\s*\(",
    r"benchmark\s*\(",
]

compiled_patterns = [re.compile(p, re.IGNORECASE) for p in sql_patterns]
whitelist_re = re.compile(r'^[\w\s@\.\-\_\,\(\)\:\/]+$')

def normalize_input(s: str) -> str:
    """Normalise et nettoie l'entrée utilisateur"""
    s = urllib.parse.unquote_plus(s)
    s = unicodedata.normalize("NFKC", s)
    return s.strip()

def is_safe_input(user_input: str) -> bool:
    """Vérifie si l'entrée utilisateur semble sûre"""
    s = normalize_input(user_input)
    if not whitelist_re.match(s):
        logging.warning("Caractères non autorisés détectés : %r", user_input)
        return False
    for patt in compiled_patterns:
        if patt.search(s):
            logging.warning("Tentative d'injection SQL détectée : %r", user_input)
            return False
    return True

def safe_query_example(user_email: str):
    """Exécute une requête SQL sécurisée avec paramètres"""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    user_email = normalize_input(user_email)
    if not is_safe_input(user_email):
        print("Entrée invalide — risque potentiel détecté.")
        return

    cursor.execute("SELECT * FROM users WHERE email = ?", (user_email,))
    results = cursor.fetchall()

    if results:
        print("Utilisateur trouvé :", results)
    else:
        print("Aucun utilisateur trouvé.")

    conn.close()

if __name__ == "__main__":
    print("=== Test de protection contre les injections SQL ===")
    email = input("Entrez une adresse e-mail : ")
    safe_query_example(email)
