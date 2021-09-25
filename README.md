# Ironhack_projet1
PROJET 1- TRI PAR FUSION

Le but de se projet est de "divisera pour régner" c'est-à-dire de faire appel à la Tri fusion.
La tri fusion implique de trier dans l'ordre croissant une liste de nombres en la divisant, pour ensuite la faire fusionner.
LES FONCTIONS

Deux fonctions sont utilisées pour obtenir un tri fusion.

-fonction itérative avec "while" et comparative avec les éléments de la liste gauche et d la liste droite.
        Chaque élément de chaque liste est comparé et append dans une nouvelle liste (final_list).

-fonction merge sort() :
Fonction recursive qui va permettre par là suite la fusion de listes
     Cette fonction contient les conditions adéquates pour obtenir une listé triée, ce qui implique :
-tous les cas à exclure
       -si la liste est une liste vide( raise ValueError) , si la liste ne contient qu'un élément (Return list), si la liste contient 2 éléments (tri de ces 2 éléments sans faire appel à la tri fusion)
-Le tri de chaque élément
-la division des sous-listes 
-l'appel récursif de la première fonction (merge) afin d'avoir chaque élément de chaque liste trié

Pour ce projet différentes listes sont utilisees afin de tester les fonctions de la tri fusion.

Nous avons ensuite rajouté une fonction reversed boolean:
- si reversed = False, qui est la condition par défaut, la fonction renverra la liste des éléments classés par ordre croissant
- si au contraire reversed = True, la fonction renverra la liste des éléments classés par ordre décroissant
