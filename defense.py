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
import logging

logging.basicConfig(level=logging.INFO)

# Liste de motifs typiques d'injection SQL
sql_patterns = [
    r"(?i)\bUNION\s+SELECT\b",
    r"(?i)\bSELECT\s+.*\bFROM\b",
    r"(?i)\bOR\s+1=1\b",
    r"(?i)\bDROP\s+TABLE\b",
    r"(?i)\bINSERT\s+INTO\b",
    r"(?i)\bUPDATE\s+\w+\s+SET\b",
    r"(?i)\bDELETE\s+FROM\b",
    r"(?i)SLEEP\(\d+\)",
    r"(?i)BENCHMARK\(",
    r"--",
    r";--",
    r"' OR",
    r"\" OR",
]


def is_safe_input(user_input: str) -> bool:
    """Vérifie si l'entrée utilisateur contient des tentatives d'injection SQL."""
    if not isinstance(user_input, str):
        return False

    # On nettoie les espaces et caractères invisibles
    clean_input = user_input.strip()

    # Si l'entrée est vide, on considère que ce n'est pas dangereux
    if not clean_input:
        return True

    # Vérifie la présence d'un motif SQL suspect
    for pattern in sql_patterns:
        if re.search(pattern, clean_input):
            logging.warning(f"Caractères non autorisés détectés : {user_input}")
            return False

    # Si aucun motif suspect trouvé, l'entrée est considérée comme sûre
    return True