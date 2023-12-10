![](RackMultipart20231209-1-ccg9g8_html_23718ad54a0b27b6.png) **Réalisé par :**![](RackMultipart20231209-1-ccg9g8_html_a102b3588f890b1a.gif)

*OKACHA Najia, ASSOUMA Roukéya, ABOUELKHIR Mohamed*

*Projet 1 :* Création d'un Dashboard pour la visualisation en temps réel des données météorologiques en utilisant Kafka, Spark, Hive, Tableau et Apache Airflow.

# *Table des matières*

[I. Objectif du projet 2](#_Toc153039606)

[II. Prérequis pour le projet - Installation et Configuration 2](#_Toc153039607)

[1. Environnement de Développement 2](#_Toc153039608)

[2. Configuration de l'Environnement Dockerisé 2](#_Toc153039609)

[a. Création des Conteneurs 2](#_Toc153039610)

[b. Exécution des conteneurs 6](#_Toc153039611)

[c. Exécution d'un conteneur spécifique 7](#_Toc153039612)

[3. Installation et Configuration de Tableau 7](#_Toc153039613)

[a. Téléchargement de Tableau Desktop : 7](#_Toc153039614)

[b. Activation de Tableau : 8](#_Toc153039615)

[c. Connexion à Hive depuis Tableau : 8](#_Toc153039616)

[d. Sélectionner la Table ou la Vue Hive : 10](#_Toc153039617)

[e. Configuration des Connexions de Données : 10](#_Toc153039618)

[III. Création du Dashboard pour la visualisation 11](#_Toc153039619)

[1. Obtention de la clé d'API OpenWeatherMap 11](#_Toc153039620)

[2. Collecte des Données Météorologiques depuis l'api vers un topic Kafka 12](#_Toc153039621)

[3. Traitement et Stockage des Données avec Spark et Hive 14](#_Toc153039622)

[4. Visualisation des Résultats avec Tableau 17](#_Toc153039623)

[a. Importation des Données 17](#_Toc153039624)

[b. Création des Visualisations 17](#_Toc153039625)

[c. Création de Tableaux de Bord (Dashboard) 19](#_Toc153039626)

[5. Orchestration avec Apache Airflow 20](#_Toc153039627)

[a. Interface utilisateur 20](#_Toc153039628)

[b. Création et exécution du dag 21](#_Toc153039629)

# I. Objectif du projet

Ce projet vise à mettre en place un système intégré pour le traitement et la visualisation en temps réel des données météorologiques en utilisant diverses technologies. Il débute par la collecte de données depuis l'API OpenWeatherMap. Ces données transitent ensuite par Kafka pour un traitement en temps réel via Spark Streaming. Les résultats obtenus sont stockés dans Hive, une base de données d'entrepôt dédiée. Enfin, ces données sont exploitées visuellement grâce à Tableau. L'intégralité de ce processus est déployée dans un environnement Dockerisé, simplifiant la gestion et le déploiement de l'infrastructure essentielle à cette chaîne de traitement des données météorologiques.

# II. Prérequis pour le projet - Installation et Configuration

Ce projet nécessite l'installation et la configuration préalable de plusieurs outils et environnements. Suivez attentivement ces étapes pour garantir un déroulement sans accroc du projet.

## 1. Environnement de Développement

1. Système d'Exploitation : Vérifiez que vous disposez d'un système d'exploitation compatible avec les outils nécessaires (Exemple : Ici, on utilise Windows).
2. RAM : Assurez-vous d'avoir une mémoire RAM supérieure à 13 Go.
3. Docker :
  - Téléchargez et installez Docker en suivant les instructions spécifiques à votre système d'exploitation : [lien vers Docker](https://docs.docker.com/get-docker/)
  - Vérifiez l'installation avec la commande : docker –version
4. Docker Compose :
  - Téléchargez et installez Docker Compose en suivant les instructions spécifiques à votre système d'exploitation : [lien vers Docker Compose](https://docs.docker.com/compose/install/)
  - Vérifiez l'installation avec la commande : docker-compose --version

## 2. Configuration de l'Environnement Dockerisé

1.
### Création des *Conteneurs*

- Élaborez un fichier docker-compose.yml décrivant les services nécessaires pour cette application.Se referer au fichier docker-compose.yml dans le dossier du projet.
![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/96ed2526-f2bb-4988-b759-d00f11cf6880)
![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/7c4fb362-8c49-44f6-b387-7e50b4dad659)
![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/5b386087-15c4-484b-b522-418137294c95)
![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/e0ee99b0-938e-4c41-b298-c28417f4e397)
![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/9b7775e7-3bc5-47c0-bffb-e16aa0f40d6b)
![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/c5230c47-8f57-417c-ab2e-078bbd92a2bc)
![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/84206c12-a02c-416e-94bc-d83d10f7dfd8)


        Figure 1.1 Code du fichier docker-compose pour la création des conteneurs docker

1.
### Exécution des conteneurs

Pour démarrer les conteneurs définis dans votre fichier *docker-compose.yml* et les exécuter en arrière-plan, utilisez la commande suivante : docker-compose up -d

Une fois les conteneurs lancés, vous pouvez lister les identifiants des conteneurs en cours d'exécution et leurs ports associés en utilisant la commande : docker ps

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/d70aa62d-910a-4f03-b7f2-8aa232dfb7fa)


Figure 1.2 Affichage de la liste des conteneurs

Pour accéder aux services dans un navigateur web, utilisez les URL suivantes :

- Zeppelin : [http://localhost:8082](http://localhost:8080/)
- Confluent : [http://localhost:9021](http://localhost:9021/)
- Spark : [http://localhost:8080](http://localhost:8080/)
- Airflow : [http://localhost:3000](http://localhost:3000/)
- Namenode : [http://localhost:9870](http://localhost:5432/)

Assurez-vous que les services sont correctement démarrés et que les ports spécifiés dans votre fichier *docker-compose.yml* ne sont pas utilisés par d'autres applications sur votre système.

1.
### Exécution d'un conteneur spécifique

Pour accéder au shell d'un conteneur spécifique en mode bash, utilisez la commande suivante, en remplaçant *id\_container* par l'identifiant du conteneur souhaité :

docker exec -it id\_container /bin/bash

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/996face2-d95b-4bc2-b9f9-d73bbe61fc28)


Figure 1.3 Exécution d'un conteneur spécifique

## 3. Installation et Configuration de Tableau

Dans le cadre de ce projet, nous utilisons Tableau Desktop. Suivez ces étapes pour installer et configurer Tableau Desktop sur votre machine.

1.
### Téléchargement de Tableau Desktop :

- Rendez-vous sur le site officiel de Tableau : [Tableau Download](https://www.tableau.com/products/desktop/download)

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/71e4b71d-601a-41b7-a4da-4f5c231026ae)


Figure 1.4 Site de téléchargement de tableau desktop

- Téléchargez la version appropriée de Tableau Desktop pour votre système d'exploitation (Windows ou Mac).
- Installez Tableau en suivant les instructions fournies lors du processus d'installation.

1.
### Activation de Tableau :

- Lors du premier lancement, Tableau Desktop vous demandera d'activer le produit. Entrez votre clé de licence si vous en avez une, ou choisissez la version d'essai.

1.
### Connexion à Hive depuis Tableau :

Pour connecter Tableau à Hive, vous pouvez utiliser le pilote ODBC (Open Database Connectivity) pour Hive. Suivez ces étapes générales pour effectuer cette connexion.

- Téléchargez et installez un pilote ODBC compatible avec Hive sur votre machine. Un exemple courant est le pilote Apache Hive ODBC Driver, que vous pouvez trouver sur le site de CDATA : [CDATA Hive ODBC Driver](https://www.cdata.com/drivers/hive/odbc/).

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/08e5815b-3be5-4fe0-ae78-342e580bf4cb)


Figure 1.5 Site de téléchargement de ODBC pour Hive

- Après l'installation du pilote ODBC, configurez-le en fournissant les détails de connexion à votre cluster Hive, tels que l'adresse du serveur Hive, le port, le nom d'utilisateur, le mot de passe, etc.

- Dans Tableau Desktop, sous l'onglet "Données", choisissez "ODBC" comme type de connexion.

- Sélectionnez le pilote ODBC pour Hive que vous avez installé.

- Entrez les informations de connexion nécessaires, telles que le nom du serveur Hive, le port, le nom d'utilisateur et le mot de passe.

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/eeb033d3-fd67-48ab-a844-b1b83fa5c171)


Figure 1.6 Etablissement de la connexion entre Hive et Tableau

- En fonction du pilote que vous utilisez, il peut y avoir des options supplémentaires à configurer. Consultez la documentation du pilote pour plus de détails.

- Après avoir configuré les paramètres de connexion, cliquez sur le bouton "Connecter" pour établir la connexion entre Tableau et Hive.

*Note :* Par défaut, aucun utilisateur n'est configuré sur Hive. Vous devez définir ici un utilisateur et un mot de passe que vous utiliserez à chaque fois que vous établirez la connexion.

1.
### Sélectionner la Table ou la Vue Hive :

Une fois connecté, vous pourrez voir les bases de données Hive disponibles. Sélectionnez la base de données, puis choisissez la table ou la vue Hive que vous souhaitez analyser dans Tableau. Pour le moment vous il n'y a aucune table dans la base de données par défaut de hive.

1.
### Configuration des Connexions de Données :

Vous pouvez configurer les connexions de données pour qu'elles soient dynamiques et mises à jour automatiquement en fonction des changements dans vos sources de données.

# III. Création du Dashboard pour la visualisation

1.
## Obtention de la clé d'API OpenWeatherMap

- Accédez au site web d'OpenWeatherMap: [OpenWeatherMap](https://openweathermap.org/api).

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/ebaf78aa-6787-47f2-bc61-85225fef1ec3)


Figure 3.1 Site de OpenWeather

- Cliquez sur "Sign Up" (S'inscrire) pour créer un nouveau compte.
- Connectez-vous à votre compte OpenWeatherMap en utilisant les identifiants que vous avez créés.
- Une fois connecté, recherchez la section "My API keys" (clés API) dans votre espace utilisateur.

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/d296b590-cd3a-4e51-b7b5-c1385211a525)


Figure 3.2 Obtention de la clé d'api

- Une fois la clé générée, copiez-la. Cette clé sera utilisée dans vos requêtes API pour identifier votre compte et autoriser l'accès aux données météorologiques.

1.
## Collecte des Données Météorologiques depuis l'api vers un topic Kafka

Pour collecter des données météorologiques depuis l'API OpenWeatherMap et les publier sur un topic Kafka en utilisant Python, vous pouvez utiliser la bibliothèque requests pour effectuer la requête API et la bibliothèque kafka-python pour publier les données sur Kafka. Assurez-vous d'installer ces bibliothèques en utilisant la commande suivante si elles ne sont pas déjà installées.

- Créer un notebook python sur zeppelin et coller le code de collecte des données depuis l'api. Vous trouverez le code dans le fichier kafka\_stream dans le dossier du projet.
- Assurer vous de remplacer la clé d'api par la vôtre.
- Installer le package kafka-python avec le code suivant :

| import subprocess
# Replace 'kafka-python' with the package you want to installpackage\_to\_install = 'kafka-python'
# Use subprocess to run the pip install commandsubprocess.call(['pip', 'install', package\_to\_install]) |
| --- |

- Assurez-vous que Kafka est en cours d'exécution et accessible depuis Zeppelin.

Note : en fonction de votre api : gratuit ou payant vous pouvez avoir accès à différents types de données. Assurer vous donc d'adapter le code en fonction de la structure des données météorologiques que vous souhaitez collecter.

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/54b5758d-7941-4247-952b-b698cd53fb18)


Figure 3.3 Code de collecte des données depuis l'api vers un topic Kafka

Les données /les messages peuvent etre visualiser au niveau du control center à l'adresse ([*http://localhost:*** 90*](http://localhost:9021/)**21*)

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/3597923f-690a-40de-bd68-2b9a6972d5fe)

Figure 3.4 Visualisation des données du topic Kafka sur le control center

1.
## Traitement et Stockage des Données avec Spark et Hive

Pour effectuer le traitement et le stockage des données avec Spark et Hive en utilisant PySpark dans Zeppelin, vous pouvez suivre ces étapes.

Assurez-vous que votre environnement est correctement configuré pour utiliser PySpark avec Zeppelin et que tout fonctionne correctement.

Le code à la Figure 3.5 orchestre la réception de données depuis le topic Kafka, lesquelles sont soumises à des opérations de traitement en temps réel à l'aide de Spark Streaming. Une fois ces traitements effectués, les résultats obtenus sont consignés et enregistrés dans Hive, permettant ainsi une structuration et une conservation optimales de ces données traitées au sein de la base de données Hive.

- Créer un nouveau notebook PySpark sur zeppelin et coller le code à exécuter. Vous trouverez le code dans le ficher spark\_stream dans le dossier du projet.

- Avant de lancer l'exécution de votre code (spark\_stream) créer une table weather\_data dans Hive, qui va contenir les données. Par défaut cette table sera enregistré dans la base de données default: Ci-dessous le script de création de la table.

| CREATE TABLE IF NOT EXISTS weather\_data (weather\_main STRING,weather\_description STRING,temp DOUBLE,temp\_min DOUBLE,temp\_max DOUBLE,pressure INT,humidity INT,visibility INT,wind\_speed DOUBLE,dt STRING,country STRING,sunrise STRING,sunset STRING,timezone INT,name STRING); |
| --- |

Par la suite lancer l'exécution de votre code.

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/09312238-efba-477d-9795-c47279d77263)


Figure 3.5 Code pour récupérer les données du topic et les envoyer vers Hive

Pour vérifier que les données ont été correctement stockées dans Hive, accéder à l'interface de Hadoop.

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/ef93a023-265f-4548-9ad1-fcdb28ebb494)


Figure 3.6 Vérification au niveau du namenode de l'ajout des données sur Hive

Par la suite vous pouvez vérifier dans la base de données pour s'assurer que les données ont bien été enregistré :

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/cea62da7-c8ec-4ec2-8d3a-c2fa32f8b7c4)


Figure 3.7 Vérification au niveau de Hive

1.
## Visualisation des Résultats avec Tableau

La visualisation des résultats avec Tableau nécessite que les données météorologiques collectées soient stockées dans un format compatible avec Tableau, tel que dans une base de données Hive. Assurez-vous d'avoir suivi les étapes précédentes, notamment la configuration de Tableau pour se connecter à Hive.

Voici comment vous pouvez visualiser les données dans Tableau après avoir suivi les étapes du projet.

1.
### Importation des Données

- Connecter vous à nouveau à Hive si nécessaire

- Une fois connecté à Hive, vous verrez les bases de données disponibles. Sélectionnez la base de données où vous avez stocké les données météorologiques.

- Choisissez la table ou la vue qui contient les données météorologiques.

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/10045213-5945-4bc3-9470-326f9d27ca10)

Figure 3.8 Importation des données de Hive sur tableau

1.
### Création des Visualisations

- Allez dans l'onglet "Feuille" pour commencer à créer vos visualisations.

- Sur la gauche, vous verrez une liste de dimensions et de mesures (valeurs numériques). Faites glisser les dimensions et les mesures souhaitées vers les étagères "Colonnes" et "Lignes".

- En fonction des données que vous avez, choisissez le type de visualisation adapté. Par exemple, utilisez un diagramme linéaire pour suivre une tendance temporelle, ou une carte pour afficher des données géographiques.

- Ajoutez des filtres pour permettre aux utilisateurs de sélectionner des plages de dates, des villes ou d'autres critères spécifiques.

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/8ad55e07-71b1-4876-af55-fa602087552b)


Figure 3.9 Visualisation de la pression par date pour chaque ville

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/2b42b6b2-a99a-4ab0-b970-627eef72548e)

Figure 3.10 Visualisation des températures à chaque date pour chaque ville

1.
### Création de Tableaux de Bord (Dashboard)

Allez dans l'onglet "Tableau de Bord" pour créer une vue d'ensemble qui combine plusieurs visualisations.

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/6bb82f6a-27ba-43ea-a729-efb979eda156)

Figure 3.11 Tableau de bord représentant l'ensemble des visualisations

1.
## Orchestration avec Apache Airflow

Airflow est une plateforme qui vous permet de créer et d'exécuter des flux de travail. Un flux de travail est représenté sous la forme d'un [DAG](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html) (un graphe acyclique dirigé) et contient des éléments de travail individuels appelés [Tâches](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html) , organisés avec des dépendances et des flux de données pris en compte.

Un DAG spécifie les dépendances entre les tâches et l'ordre dans lequel les exécuter et exécuter les nouvelles tentatives.

Les tâches elles-mêmes décrivent ce qu'il faut faire, qu'il s'agisse de récupérer des données, d'exécuter une analyse, de déclencher d'autres systèmes, ou plus encore.

1.
### Interface utilisateur

Airflow est livré avec une interface utilisateur qui vous permet de voir ce que font les DAG et leurs tâches, de déclencher des exécutions de DAG, d'afficher les journaux et d'effectuer un débogage et une résolution limités des problèmes avec vos DAG.

Pour se connecter à l'interface utilisez les identifiants suivants :

- Nom d'utilisateur : admin
- Mot de passe : admin

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/8d1d2203-9b1b-4ec1-93ec-43231c83c659)

Figure 3.12 Interface utilisateur de Airflow

1.
### Création et exécution du dag

- Utilisez votre éditeur de code préféré (comme VSCode, PyCharm, etc.).

- Créez un nouveau dossier appelé "dags" à l'emplacement où vous souhaitez stocker vos DAGs.

- À l'intérieur du dossier "dags", créez un fichier Python pour votre DAG, par exemple, "dag.py".

- Dans ce fichier, écrivez le code décrivant les différentes étapes du processus.

Vous trouverez le code dans le fichier dag.py dans le dossier du projet, copier et coller le code dans votre fichier et faites les installations nécessaires.

- Faites toutes les installations de packages nécessaires avec pip ou si vous utiliser PyCharm à partir de l'interpréteur.

- Dans le code du dag modifier les adresses des notebooks selon les id

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/eed5453e-46b6-48e5-bee7-4afcd7f319aa)
![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/5f20a79c-57eb-4465-a7d3-4ab489b5d60e)
![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/c1c8b8c1-ed51-414b-bfa7-f0f42f1d5f97)
![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/7d9d1f98-d912-450f-b550-0a8b09ae8495)

Figure 3.13 Code du dag du projet

- Assurez-vous qu'Airflow est en cours d'exécution et lancer l'exécution de votre dag.

- Airflow va automatiquement détecter et charger votre DAG.

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/a7c5d701-ea4d-49ff-8b70-586555b46aaa)

Figure 3.14 Vérification de l'ajout du nouveau dag à la liste des dags

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/100485014/3fad141b-9d5a-444e-b1c0-8063bce1acdc)

Figure 3.15 Visualisation de l'exécution du dag créer

Si vous avez planifié le processus de collecte, de traitement et de stockage des données à intervalles réguliers avec Apache Airflow, vous pouvez configurer Tableau pour actualiser automatiquement les données à partir de Hive.
