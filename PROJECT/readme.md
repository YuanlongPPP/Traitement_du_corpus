# outils_de_traitement_de_corpus  
  

## Description du projet  

lien : https://huggingface.co/HuggingFaceH4/starchat2-15b-v0.1  

### Abirate/french_book_reviews  

### Tâche :  

La tâche principale pour ce dataset est la classification de texte multi-label. Cela consiste à classifier les critiques de livres selon leur valeur de label, déterminée par le sentiment exprimé dans la critique (positif, neutre, négatif).  

### Corpus :  

Le corpus comprend un grand nombre de critiques de lecteurs sur des livres français, provenant de deux sites français : Babelio et Critiques Libres. Ce corpus est enrichi en continu avec les critiques les plus récentes.  


### à quel type de prédiction peut servir ce corpus  
Ce corpus peut servir à des prédictions de sentiment analysis (analyse de sentiment), où le but est d'évaluer si une critique est positive, neutre ou négative. Ce type de prédiction est crucial pour des applications telles que l'amélioration des systèmes de recommandation, l'analyse de la réception de produits culturels, et la modélisation de préférences utilisateurs.  

### à quel modèle il a servi  
Bien que la description ne spécifie pas explicitement quels modèles ont déjà utilisé ce corpus, il est idéalement adapté pour entraîner des modèles de traitement automatique du langage naturel (TALN) spécialisés dans la classification de texte. Les modèles tels que BERT, RoBERTa ou d'autres architectures basées sur les transformateurs pourraient être utilisés pour traiter ce corpus et effectuer des tâches de classification de sentiment.  

## Explication de démarche de traitement du corpus (incluant des explications de différents scripts utilisés)  


### 1. Mise en place du dépôt github et créer la structure de dépôté demandée.  
Nous avons d'abord créé un dépôt nommé "outils_de_traitement_de_corpus". Cependant, à cause du problème de clé ssh, nous n'avons pas eu de solution pour régler le problème et nous avons décidé de créé un autre dépôt nommé "Traitement_du_corpus" pour notre travail.  
Après la création du dépôt, nous avons utilisé des lignes de commande pour élaborer les différents fichiers en suivant les consignes proposés dans le script création_fichier.py (nous avons ajouté le fichier .gitkeep dans chaque dossier créé afin de les rendre visible sur le git).  
En utilisant la commande tree PROJECT, nous pouvons visualiser la structure en arbre :  
PROJECT  
├── LICENSE  
├── Makefile  
├── README.md  
├── bin  
├── data  
│   ├── clean  
│   └── raw  
├── figures  
├── scripts  
│   ├── plot  
│   └── process  
└── src  
    ├── model1  
    ├── model2  
    └── model3  


### 2. Extraction des données, nettoyage et convertir vers le csv :  
2.1. nous avons utilisé le script "extraire_donnée" pour extraire les commentaires sur le site ： 
(a). Importation des bibliothèques : Par exemple, request pour effectuer des requêtes HTTP, "BeautifulSoup" pour parser les documents HTML.  

(b). Fonction de récupérer les données : Cette fonction envoie une requête à l'URL donnée et retourne le  contenu HTML de la page. Si la requête n'est pas réussi, elle renvoie 'None'.  

(c). Fonction pour parser les données : Cette fonction permet d'analyser le contenu et la structure HTML pour extraire le titre du livre, l'auteur, les critiques, et les évaluations. Si l'information de l'évaluation est manquante, on ne prend pas de commentaires. D'ailleurs, il convient de noter que si certaines informations ne sont pas présentes, des valeurs de défaut sont utilisées. Les données sont stockées dans une liste.  
Cela correspond aux éléments qui est requise à extraire si on s'appuie sur le projet de référence.  
{   
    "book_title": "La belle histoire des maths",  
    "author": "Michel Rousselet",  
    "reader_review": "C’est un livre impressionnant, qui inspire le respect   
    par la qualité de sa reliure et son contenu. Je le feuillette et je découvre  
    à chaque tour de page un thème distinct magnifiquement illustré. Très beau livre !",  
    "rating": 4.0,  
    "label": 1  
}  

(d). Fonction pour attribuer les labels : Cette fonction sert à assigner un label basé sur la note: 1 pour les commentaires positifs; 0 pour les commentaires neutres et -1 pour les commentaires négatifs.  

(f). Fonction pour sauvegarder les données : Cette fonction sauvegarde les données collectées dans un fichier JSON dans le répertoire indiqué. S'il n'exsite pas, il est créé.  

(g). Fonction principale : cette fonction permet de récupérer les données des URL qu'on a sélectionné, analyser les pages pour extraire les informations requises, puis sauvegarder des données dns le fichier JSON.  

2.2. Nous avons utilisé ensuite le script clean_data.py pour nettoyer le corpus :  

(a). Importation de bibliothèque : on a importé json, os, re et html.  

(b). Charger les données brutes : ces lignes de commandes permettent de charger les données brutes à partir d'un fichier json produit par le 2.1. et les stoken dans la variable "data".  

(c). Définition de la fonction de nettoyage : cette fonction sert à d'abord prendre un texte en entrée et effectue différentes étapes d'opérations de nettoyage :  

Remplacement des HTML  
Correction des problème d'espace (trop d'espace ou manque d'espace).  
Uniformation de certaines ponctuations mal formulées.  
Suppression des barres obliques inverses (\\)  Remarque: je trouve ces symbôles dans le texte brut et je déduit qu'il s'agit de l'hyperlien. Mais il semble qu'au final, il n'a pas été supprimé avec ce script.  

(d). Néttoyage des données : la fonction parcourt chaque partie dans les données brutes, applique la fonction de nettoyage au texte des commentaires, et ne conserve que les critiques qui ont une note. Ces commentaires nettoyées sont concservés dans la liste "donnees_nettoyees".  

(e). Enregistrement des données nettoyées : cette fonction permet d'enregistrer les données néttoyées dans un fichier JSON.  

2.3. Nous avons utilisé le script "csv_fichier" pour convertir le fichier JSON, ainsi on peut avoir un fichier Excel comprenant les colonnes "book_title", "author", "read_review", "rating" et "label".  

Difficultés rencontrées :  
Il convient de remarquer que sur le site, la page contenant les métadonnées sur le livre ainsi que quelques commentaires (très peu) et la page contenant les critiques plus détaillés (et d'alleurs, les critiques détaillées sont présents dans différentes pages) sont séparés. De plus, parmi les commentaires présents dans la même page que ces métadonnées, on trouve très peu de commentaires négatif ou neutre, autrement dit, la majorité de commentaires sont évalués comme positifs. C'est ainsi que nous avons essayé de créer le script "extraire_donnée_V2 qui permet d'extraire les données en tournant la page et en tenant compte l'équilibre des nombres de type de commentaires (50 pour chaque catégorie).  
Cependant, le script ne marche pas. Nous avons essayé de comprendre pourquoi et nous avons déduit que cela est dû au fait que les pages des critiques ne sont pas exploitables parce qu'on a eu ce message d'erreur : Error fetching robots.txt from https://www.babelio.com/robots.txt: HTTPSConnectionPool(host='www.babelio.com', port=443): Max retries exceeded with url: /robots.txt (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7fabd87436d0>: Failed to establish a new connection: [Errno 60] Operation timed out'))  
Fetching https://www.babelio.com/livres/Rousselet-La-belle-histoire-des-maths/121795/critiques?a=a&pageN=1 is not allowed by robots.txt  
Error fetching robots.txt from https://www.babelio.com/robots.txt: HTTPSConnectionPool(host='www.babelio.com', port=443): Max retries exceeded with url: /robots.txt (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7fabca007640>: Failed to establish a new connection: [Errno 60] Operation timed out'))  
...  
Nous n'avons donc pas trouvé d'autres solutions qui permettent de réaliser ce but de manière automatique, nous avons donc décidé d'extraire les données manuellement (c'est à dire de rajouter des commentaires notamment négatifs et neutres et supprimer ceux qui sont positifs dans le fichier excel converti par ce fichier csv qu'on a élaboré à travers ce script là.), de nettoyage ces données collectés et de convertir le fichier excel en fichier csv. Cela a pour objectif de ne pas empêcher les étapes suivantes bien que nous ne suivions pas exactement les consignes sur le traitement automatique (on y a réussi partiellement).  

### 3. Analyse morphosyntaxique : 
Nous avons utilisé le script "analyse_morphosyntaxe.py" pour faire des analyse sur des données :  

(a). Importation des bibliothèques : importer des bibliothèques nécessaires pour le traitement de données (pandas), l'analyse linguistique ("spacy"), la visualisation ("matplotlib", "seaborn"), et le comptage ("Counter").  

(b). Lecture et conversion des données : cette fonction permet de lire un fichier Excel contenant les informations requises (celui qu'on a modifié à la main), le convertir en fichier CSV, puis charger ce fichier CSV dans un DataFrame "panda".  

(c). Analyse morphosyntaxique :  cette partie charge le modèle linguistique français de Spacy, définit une fonction pour analyser la morphosyntaxe de textes et associe cette fonction à chaque commentaire dans le DataFrame pour extraire les tokens et leurs POS.  

(d). Répartition des étiquettes de POS : ces lignes de commandes permet de compter les occurrences de chaque étiquette POS dans tous les commentaires, les convertir en un DataFrame et créer le graphique pour la visualisation.  

(f). Distribution des étiquette POS par la polarité de sentiment exprimé par le commentaire : cette fonction permet de tracer la distribution des étiquettes POS pour un label de polarité de sentiment exprimé (positif, négatif et neutre) et utilise cette fonction pour créer des graphique pour chaque catégorie de polarité.  VUE ENSEMBLE (chaque graphique montre la distribution de tous les POS dans chaque polarité)

(g). Distribution des étiquettes POS par label dans un DataFrame :  cette fonction est aussi d'illustrer la distribution de POS par label indiqué. Ce qui est différent, c'est qu'il observe la distribution de chaque POS dans chaque catégorie de polarité sélectionné.  

(h). Obtenir les mots les plus fréquents pour chaque étiquette de POS sélectionné : cette fonction permet de définir une fonction pour obtenir les mots les plus fréquents pour une étiquette POS et un label de sentiment spécifiques, puis utilise cette fonction pour obtenir les adjectifs, adverbes, verbes les plus fréquents pour chaque catégorie de polarité. On peut avoir les résultats et les graphiques correspondantes. 
Remarques : nous n'avons pas trouvé grande chose à partir de ces graphiques (autrement dit, on n'a pas trouvé la régularité sur ces distributions). On suppose que cela est dû au fait qu'on n'a pas effectué des traitements plus profondes sur le corpus. Par exemple, on pourrait supprimer les mots qui sont les plus fréquents, les moins fréquents et les stop words. Nous pourrions le prendre en compte dans l'étape suivante, lors qu'on effectue la recherche sur les mots les plus fréquentes ou faire de sac de mots.  

### 4. statistique et mesure  

Nous avons utilisé le script "statistique_et_mesure" pour proposer des analyses statistiques et faire la visualisation des données. Nous illustrons et expliquons le script comme suit :  

1. La première partie consiste à calculer la longueur de chaque critique et affiche un histogramme de la distribution des longueurs des critiques, avec le nombre de critique sur l'axe des ordonnées et la longueur des critiques sur l'axe des abscisses.  

2. Cette partie est conçu pour tracer un graphique de dispersion entre la longueur des commentaires et les notes.  

3. Cette partie est pour créer le graphique de Zipf pour le corpus en tout.  

4. Cette partie est créée pour le graphique de Zipf pour chaque catégiorie de polarité : positif, négatif et neutre.  

5. Cette partie a pour objectif de calculer la fréquence de mots et afficher les 10 mots les plus fréquents.  

6. Cette partie sert à obtenir les mots les plus fréquents pour chaque étiquette (positif, neutre et négatif) et les affiche.  

7. Cette partie permet de calculer les longueurs des phrases et enfin la longueur moyenne des phrases.  

8. Cette partie permet de calculer la longueur moyenne des phrases par catégorie (label).  

9. Les parties suivantes sont pour voir si le calcul est couteau. Et nous pensons que non après avoir vérifié avec le script. Nous avons donc créé le script permettant l'utilisation de la fonction réutilisable.  

### 5. Evaluation  

Nous avons d'abord essayé d'évaluer la corrélation entre la longueur de commentaires et la note et le p-value est 0. Nous avons donc voir la distribution de mots les plus fréquents. Cependant, nous avons remarquer qu'il faut supprimer les mots qui ont la fréquence la plus haute et la plus basse, nous avons procédé donc au score TF-IDF en supprimant les stopwords et les ponctuations afin de voir les mots les plus fréquents.  

Par la suite, nous avons sélectionné "bien" et voir la corrélation entre son nombre d'occurrences et la classification de critiques.  Et ensuite, nous avons essayé d'augmenter le P-value en supprimant les données abérantes et augmentant les données.  

Finalement, nous avons utilisé différentes métriques (métriques génériques, métriques adaptés à la tâche) tout en proposant une métrique à mon corpus.  

### Docker  

Tous les dossiers et fichiers nécessaires et concernés sont conservés dans le dossier Docker->process->script.  

### La structure de la version finale pourrait être :  

├── PROJECT  
│   ├── LICENSE  
│   ├── Makefile  
│   ├── README.md  
│   ├── bin  
│   ├── data  
│   │   ├── clean  
│   │   │   ├── clean_data  
│   │   │   │   └── cleaned_reviews.json  
│   │   │   └── fichier_csv  
│   │   │       ├── book_reviews.csv  
│   │   │       └── version modifiée  
│   │   │           ├── book_review_2.0.csv  
│   │   │           └── book_review_2.0.xlsx  
│   │   └── raw  
│   │       └── reviews_with_ratings.json  
│   ├── dataset_projet.yaml  
│   ├── figures  
│   ├── scripts  
│   │   ├── plot  
│   │   └── process  
│   │       ├── Docker  
│   │       │   ├── Dockerfile  
│   │       │   ├── book_review_2.0.xlsx  
│   │       │   ├── entrypoint.sh  
│   │       │   ├── explication_docker.py  
│   │       │   └── insert_data.py  
│   │       ├── analyse_morphosyntaxe.ipynb  
│   │       ├── clean_data.ipynb  
│   │       ├── csv_fichier.ipynb  
│   │       ├── évaluation.ipynb  
│   │       ├── extraire_donnée.ipynb  
│   │       ├── extraire_donnée_V2.ipynb  
│   │       ├── résultat_évaluation  
│   │       │   ├── dev_data.csv  
│   │       │   ├── test_data.csv  
│   │       │   └── train_data.csv  
│   │       ├── résultats_statistique_et_mesure  
│   │       │   └── text_statistics.json  
│   │       └── statistique_et_mesure.ipynb  
│   └── src  
│       ├── model1  
│       ├── model2  
│       └── model3  
└── création_fichier.py  

### Limite de travail :  
En observant les résultats qu'on a obtenus, nous avons trouvé que la performance n'est pas de bonne qualité, nous essayons de déduire les raisons qui conduisent à cela en plusieurs aspects :  

(1).  Les données ne sont pas de grandes quantités. c'est ainsi qu'on arrive pas à trouver les mots représentatifs et caratérisés pour chaque catégorie de polarité de sentiment. Nous trouvons aussi que les lecteurs des livres ont proposé différentes expressions d'exprimer leurs sentiments (les vocabulaires sont assez riches et variées.).  Il est aussi essentiel de considérer la diversité linguistique et les variations dans les expressions de sentiment selon les groupes démographiques. La manière dont les sentiments sont exprimés peut varier en fonction de l’âge, du contexte culturel, ou même de milieu social des individus.  
-> perspectives : augmenter le volume du corpus et diviser le corpus en vue d'entrainement en groupes.  

(2). La méthode de division du corpus peuvent être améliorée.  
 -> perspective : on pourrait utiliser la validation croisée.  
  