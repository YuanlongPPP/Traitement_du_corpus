# outils_de_traitement_de_corpus  
  

## description du projet  

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


1. Mise en place du dépôt github et créer la structure de dépôté demandée.  
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


2. Extraction des données, nettoyage et convertir vers le csv :  
2.1.  