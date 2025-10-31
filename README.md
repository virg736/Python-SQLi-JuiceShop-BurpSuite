# 💻 Projet GitHub n°2 – Injection SQL sur OWASP Juice Shop

## 📚 Sommaire

1. [🎯 Objectif du projet](#-objectif-du-projet)  
2. [🧱 Environnement de test](#-environnement-de-test)  
3. [🛠️ Outils utilisés](#️-outils-utilisés)  
4. [🔌 Étape 1 – Connexion des machines](#-étape-1--connexion-des-machines)  
5. [🚀 Étape 2 – Lancement de Juice Shop](#-étape-2--lancement-de-juice-shop)  
6. [🔓 Étape 3 – Connexion à Juice Shop](#-étape-3--connexion-à-juice-shop)  
7. [🩻 Étape 4 – Injection SQL simple](#-étape-4--injection-sql-simple)  
8. [👁️ Étape 5 – Injection SQL avancée (Blind SQLi)](#-étape-5--injection-sql-avancée-blind-sqli)  
9. [🧪 Attaque via Burp Suite](#-attaque-via-burp-suite)  
10. [🧠 Vocabulaire utile](#-vocabulaire-utile)  
11. [🛡️ Sécurité & Légalité](#️-sécurité--légalité)  
12. [📈 Suivi des projets GitHub](#-suivi-des-projets-github)  

---

## 🎯 Objectif du projet

Simuler une attaque **SQL Injection** dans un environnement sécurisé et local, via l’application volontairement vulnérable **OWASP Juice Shop**, afin de comprendre les risques liés à l'injection de requêtes SQL.

---

## 🧱 Environnement de test

| Machine       | OS/Distro         | Rôle        | Adresse IP        |
|---------------|-------------------|-------------|-------------------|
| Parrot OS     | Parrot Security   | Attaquant   | `192.168.100.10`  |
| Debian        | Debian 11         | Victime     | `192.168.100.20`  |

➡️ Les deux machines tournent sur **VirtualBox** en **réseau local (bridge)**.

---

## 🛠️ Outils utilisés

| Outil             | Fonction                                           |
|-------------------|----------------------------------------------------|
| Docker            | Déploiement de Juice Shop sur Debian               |
| OWASP Juice Shop  | Application vulnérable à tester                    |
| Firefox           | Navigateur web                                     |
| Burp Suite        | Interception et analyse des requêtes HTTP          |
| Terminal Linux    | Commandes réseau (ping, docker...)                 |

---

## 🔌 Étape 1 – Connexion des machines

```bash
# Depuis Parrot :
ping 192.168.100.20

# Depuis Debian :
ping 192.168.100.10
