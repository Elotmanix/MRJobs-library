# TP sur la Librairie MRJobs

Ce projet consiste en la réalisation de deux exercices utilisant la librairie `MRJob` pour des traitements MapReduce. Les travaux doivent être effectués en local sur vos machines personnelles.

---

## Exercice 1 : Questionner un Fichier de Ventes

### Objectif
Analyser un fichier volumineux contenant des résultats de ventes afin de recueillir des informations et calculer des statistiques.

### Préparation
1. Créez un répertoire sur votre disque dur.
2. Placez-y le fichier de ventes à analyser :
   - `purchases.txt` : contient plus de 4 000 000 lignes.
   - `purchases_10000.txt` : une extraction de 10 000 lignes pour des tests rapides.

### Format du Fichier
Le fichier est organisé en 6 colonnes, séparées par des tabulations (`\t`) :
1. **Date** (format `YYYY-MM-DD`)
2. **Heure** (format `hh:mm`)
3. **Ville d’achat**
4. **Catégorie de l’achat** (par exemple : `Book`, `Men’s Clothing`, `DVDs`, etc.)
5. **Somme dépensée par le client**
6. **Moyen de paiement** (par exemple : `Amex`, `Cash`, `MasterCard`, etc.)

### Questions à Résoudre
Pour chaque question, créez un script Python distinct utilisant la librairie `MRJob` :
1. **Nombre d’achats effectués par catégorie d’achat.**
2. **Somme totale dépensée par catégorie d’achat.**
3. **Somme dépensée dans la ville de San Francisco selon chaque moyen de paiement.**
4. **Ville générant le plus d’argent en espèces (Cash) pour la catégorie `Women’s Clothing`.**
5. **Requête originale et complexe (nombre d'étapes > 1) de votre choix.**

### Instructions
- Testez vos programmes en mode `-r local` pour vérifier leur fonctionnement en local.
- Assurez-vous que vos scripts fonctionnent bien dans un contexte de traitement parallèle.

---

## Exercice 2 : Détection d’Anagrammes

### Objectif
Écrire un script MapReduce pour détecter les mots ayant **exactement** les mêmes lettres (dans un ordre différent) dans un fichier donné.

### Exemple
Pour un fichier contenant les mots :
melon, barre, deviner, lemon, arbre, fiable, fable, vendre, devenir, faible, barbe

Le script doit produire :
faible, fiable arbre, barre devenir, deviner lemon, melon


### Contraintes
- Les réponses doivent contenir au moins **2 mots**.
- Ne pas tenir compte des voyelles accentuées.

### Fichiers de Test
Pour des tests intensifs, vous pouvez utiliser :
- **Dictionnaire anglais** : `words_alpha`
- **Dictionnaire français** : `Liste-de-mots-francais-Gutenberg`

---

## Notes
- Utilisez la documentation officielle de [MRJob](https://mrjob.readthedocs.io/en/latest/) pour vous guider.
- Pensez à bien commenter votre code et à structurer vos scripts pour une meilleure compréhension.

Bon travail !
