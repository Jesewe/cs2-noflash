<div align="center">
   <img src="src/img/icon.png" alt="CS2 NoFlash" width="200" height="200">
   <h1>🌟 CS2 NoFlash 🌟</h1>
   <p>Votre outil ultime anti-flash pour Counter-Strike 2</p>
   <a href="#fonctionnalités"><strong>Fonctionnalités</strong></a> •
   <a href="#installation"><strong>Installation</strong></a> •
   <a href="#utilisation"><strong>Utilisation</strong></a> •
   <a href="#personnalisation"><strong>Personnalisation</strong></a> •
   <a href="#résolution-des-problèmes"><strong>Résolution des problèmes</strong></a> •
   <a href="#contribuer"><strong>Contribuer</strong></a>
   <br><br>
   <p><strong>🌍 Traductions :</strong></p>
   <a href="README.ru.md"><img src="https://img.shields.io/badge/lang-Russian-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.fr.md"><img src="https://img.shields.io/badge/lang-French-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.es.md"><img src="https://img.shields.io/badge/lang-Spanish-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.uk-UA.md"><img src="https://img.shields.io/badge/lang-Ukrainian-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.pl.md"><img src="https://img.shields.io/badge/lang-Polish-purple?style=for-the-badge&logo=googletranslate"></a>
</div>

---

# Vue d'ensemble
CS2 NoFlash est un outil automatisé conçu pour Counter-Strike 2 qui empêche le joueur d'être complètement flashé en ajustant automatiquement les valeurs alpha des flashbangs dans le jeu.

## Fonctionnalités
- **Protection Anti-Flash :** Régle automatiquement la valeur alpha du flashbang à 0, empêchant le joueur d'être complètement aveuglé.
- **Attachement au Processus :** S'attache au processus cs2.exe et lit les valeurs mémoire pour appliquer des changements en temps réel.
- **Vérificateur de Mises à Jour :** Vérifie automatiquement la dernière version et notifie l'utilisateur si une mise à jour est disponible.
- **Journalisation des Erreurs :** Enregistre les erreurs et les événements importants dans un fichier log pour des fins de débogage.

## Installation
1. **Cloner le Dépôt :**
   
bash
   git clone https://github.com/Jesewe/cs2-noflash.git
   cd cs2-noflash


2. **Installer les Dépendances :**
   
bash
   pip install -r requirements.txt


3. **Exécuter le Script :**
   
bash
   python main.py


## Utilisation
1. Assurez-vous que Counter-Strike 2 est en cours d'exécution.
2. Exécutez le script en utilisant la commande ci-dessus.
3. Le script vérifiera automatiquement les mises à jour et récupérera les offsets nécessaires à partir des sources fournies.
4. La protection NoFlash démarrera automatiquement, réduisant l'effet du flashbang au minimum.

## Personnalisation
- **Répertoire de Log :** Les fichiers de log sont enregistrés par défaut dans le répertoire %LOCALAPPDATA%\Requests\ItsJesewe\crashes. Vous pouvez changer cela en modifiant la variable LOG_DIRECTORY dans le script.

## Résolution des problèmes
- **Échec de la Récupération des Offsets :** Assurez-vous d'avoir une connexion Internet active et que les URL sources sont accessibles.
- **Impossible d'Ouvrir `cs2.exe` :** Assurez-vous que le jeu est en cours d'exécution et que vous avez les permissions nécessaires.
- **Erreurs Inattendues :** Consultez le fichier log situé dans le répertoire de log pour plus de détails.

## Contribuer
Les contributions sont les bienvenues ! Veuillez ouvrir un problème ou soumettre une pull request sur le [répertoire GitHub](https://github.com/Jesewe/cs2-noflash).

## Avertissement
Ce script est à des fins éducatives uniquement. L'utilisation de cheats ou de hacks dans les jeux en ligne est contraire aux conditions de service de la plupart des jeux et peut entraîner des bannissements ou d'autres sanctions. Utilisez ce script à vos propres risques.

## Licence
Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.