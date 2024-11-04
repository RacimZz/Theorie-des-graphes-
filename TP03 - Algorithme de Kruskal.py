###############################################
### TP3 - Arbres couvrants de poids minimum ###
###############################################

import copy
import time
from lib.graphe      import Graphe
from lib.tasbinomial import TasBinomial

"""
La documentation des fonctions contient des exemples, qui servent aussi de 
tests unitaires si le fichier est exécuté.

Comment faire les TP :
Vous pouvez au choix
    (a) utiliser un environnement pour python (Idle, PYZO...)
    (b) utiliser l'environnement Visual Studio, avec l'extension VPLClient pour Caséine

* (a) (Idle, PYZO...)
    Téléchargez le TP et décompressez son archive dans le dossier créé à cet effet.
    Ouvrez le fichier « tp.py » dans votre environnement de codage favori.
  (b) (VScode)
    Créez un dossier vide pour ce TP.
    Lancez Visual Studio Code, et installez l'extension "VPL Client " si elle n'est pas encore installée.
    Dans Visual Studio Code, ouvrez le dossier vide ("Open Folder...") que vous avez créé pour ce TP,
    cliquez sur l'onglet de l'extension VPL (la bouteille de lait) et initialisez le VPL avec le lien que vous trouverez :
        (1) en ouvrant le TP dans votre navigateur, onglet Description
        (2) puis Webservices en bas 
        (3) puis Webservice VPL global -> URL complète -> cliquez sur le bouton Copier
    Revenir sur l'onglet "Explorer les fichiers" puis sélectionner le fichier tp.py
* Complétez une par une les fonctions entre les lignes  ### A COMPLETER DEBUT 
et ### A COMPLETER FIN 
* Lorsque vous pensez avoir terminé une fonction, exécutez le fichier sur votre
machine et vérifiez que les tests unitaires passent. Si ce n'est pas le cas,
corrigez votre fonction.
* Lorsque les tests unitaires passent pour une fonction: 
    (a) (Idle, PYZO...)
        Faites un copier-coller du fichier complet sur Caseine dans l'onglet "Edit", sauvegardez
        et vérifiez que cela fonctionne sur Caseine avec le bouton "Evaluate".
    (b) (VSCode)
        Dans l'extension VPL (Bouteille de lait), cliquez sur l'icône Evaluate (tick), attendez la réponse du serveur Caseine
        et lisez le rapport de test.


Attention : les tests fournis ne peuvent être exhaustifs. Qu'une fonction passe
tous les tests ne garantit pas qu'elle soit correcte. Gardez cela en tête
lorsque vous réutilisez vos fonctions dans d'autres fonctions.

---

Dans ce TP, les graphes sont des graphes avec des poids sur les arêtes.
Pensez à regarder les documentations et exemples de la classe Graphe,
notamment pour les méthodes __init__, ajouter_arete et voisins_avec_poids.
"""



def graphe_1():
    """Retourne le graphe (Graphe) G1.


                2
               /|
              / |
             /  |
          2 /   | 3          G1
           /    |
          /     |
         /      |
        0-------1-------3
            1       4

        :Examples:

        >>> graphe_1()
        {4: 0-1-1 0-2-2 1-3-2 1-4-3}

    """

    ### À COMPLÉTER DÉBUT 
    G1 =Graphe( 4, [(0, 1, 1), (0, 2, 2), (1, 2, 3), (1, 3, 4)])
    return G1
    ### À COMPLÉTER FIN

def graphe_2():
    """Retourne le graphe (Graphe) G2.

            11
        0--------1
        |\      /|
        | \10 9/ |
        |  \  /  |
        |   \/   |
        |1  /\  4|            G2
        |  /  \  |
        | /    \ |
        |/      \|
        2--------3
            3

        :Examples:

        >>> graphe_2()
        {4: 0-11-1 0-1-2 0-10-3 1-9-2 1-4-3 2-3-3}

    """
    G2 = Graphe(4, [(0, 1, 11), (0, 2, 1) ,(0,3,10) , (1, 2, 9), (1, 3, 4), (2, 3, 3)])
    return G2

def graphe_3(n):
    """Retourne un graphe à n sommet, tel qu'il existe une arête entre i et j si
    et seulement si |j-i| <= 2 et le poids de l'arête (ij) est i+j.

                4
            1-------3-----
           / \     / \
         1/  3\  5/  7\       etc        G3
         /     \ /     \ /
        0-------2-------4
            2       6

        :param n: Nombre de sommets, entier naturel supérieur ou égal à 3

        :Examples:

        >>> graphe_3(3)
        {3: 0-1-1 0-2-2 1-3-2}
        >>> graphe_3(4)
        {4: 0-1-1 0-2-2 1-3-2 1-4-3 2-5-3}
        >>> graphe_3(5)
        {5: 0-1-1 0-2-2 1-3-2 1-4-3 2-5-3 2-6-4 3-7-4}

    """

    G3 = []
    for i in range(n):
        if i + 1 < n:
            G3.append((i, i + 1, i + (i + 1)))
        if i + 2 < n:
            G3.append((i,i + 2,  i + (i + 2)))
    return Graphe(n, G3)

def aretes_triees(g):
    """Retourne la liste des arêtes de g triées par poids croissant.

        Les arêtes (uv) sont tel que u < v.

        :Examples:

        >>> aretes_triees(graphe_1())
        [(0, 1, 1), (0, 2, 2), (1, 2, 3), (1, 3, 4)]
        >>> aretes_triees(graphe_2())
        [(0, 2, 1), (2, 3, 3), (1, 3, 4), (1, 2, 9), (0, 3, 10), (0, 1, 11)]


    """

    # Pour trier une liste l de tuples selon leur ieme composante :
    # >>> l.sort(key=lambda t: t[i])
    # la syntaxe lambda t: t[i] correspond à la fonction qui, à t associe t[i]
    # Ici on l'utilise pour évaluer la valeur du tuple t et donc pour comparer deux tuples

    ### À COMPLÉTER DÉBUT
    l = []
    for i in range(g.nombre_sommets()):
        for v, poids in g.voisins_avec_poids(i):
            if i < v :
                l.append((i, v, poids))  # Ajoute les arêtes sous forme de tuple (sommet1, sommet2, poids)

    # Tri des arêtes par poids croissant
    aretes = sorted(l, key=lambda t: t[2])  # Utilisation de sorted pour trier l par poids (t[2] est le poids)

    return aretes

    ### À COMPLÉTER FIN



#############################
### Algorithme de Kruskal ###
#############################

########################################################
### Union-Find : Implémentation utilisant un tableau ###
########################################################

# Dans ce TP, nous allons voir deux implémentations de la structure
# de données UNION-FIND, qui est utile pour l'algorithme de Kruskal.
# Pour la première implémentation de la structure UNION-FIND, nous allons
# utiliser un tableau T (une liste en Python) tel que T[i] est l'indice de la
# composante connexe à laquelle le sommet i appartient.
# Cette première version est plus simple à implémenter mais moins efficace.
# La deuxième implémentation se fera avec des forêts (comme dans le cours),
# version plus élaborée mais plus efficace.
# Le principe du UNION-FIND est le suivant :
# On numérote les composantes connexes de la forêt courante. Au début de
# l'algorithme, comme il n'y a pas encore d'arête, chaque sommet est seul dans
# sa composante connexe. Si lorsque l'on examine l'arête (uv), u et v
# appartiennent à la même composante connexe, alors on n'ajoute pas l'arête,
# sinon on l'ajoute et on met à jour notre structure pour fusionner les
# composantes connexes de u et de v.


def ufl_creer(n):
    """Retourne la structure UNION-FIND initialisée.

        :param n: Nombre de sommets, entier naturel

        :Examples:

        >>> ufl_creer(2)
        [0, 1]
        >>> ufl_creer(5)
        [0, 1, 2, 3, 4]

    """

    ### À COMPLÉTER DÉBUT (Complexité O(n), environ 1 ligne)
    return [i for i in range(n)]
    ### À COMPLÉTER FIN

def ufl_find(l, v):
    """Retourne l'indice de la composante connexe du sommet i dans la structure
    UNION-FIND l.

        :param v: Un indice d'un sommet, entier naturel compris entre 0 et n-1.

        :Examples:

        >>> l = [0, 0, 1, 0, 2, 3, 4]
        >>> ufl_find(l, 1)
        0
        >>> ufl_find(l, 6)
        4

    """

    ### À COMPLÉTER DÉBUT (Complexité O(1), environ 1 ligne)
    return l[v]
    ### À COMPLÉTER FIN

def ufl_union(l, i, j):
    """Fusionne les composantes connexes d'indice i et j dans la structure
    UNION-FIND l.

        L'indice de la nouvelle composante connexe est min(i,j).

        :param i: Un indice d'une composante connexe, i in l
        :param j: Un indice d'une composante connexe, j in l, j != i

        :Examples:

        >>> l = [0, 0, 1, 0, 2, 4, 4]
        >>> ufl_union(l, 1, 0)
        >>> l
        [0, 0, 0, 0, 2, 4, 4]
        >>> ufl_union(l, 4, 2)
        >>> l
        [0, 0, 0, 0, 2, 2, 2]

    """

    ### À COMPLÉTER DÉBUT (Complexité O(n), environ 3 lignes)
    minimum = min(i, j)
    maximum = max(i, j)
    for k in range(len(l)):
        if l[k] == maximum:
            l[k] = minimum

    ### À COMPLÉTER FIN

def kruskal_ufl(g):
    """Retourne un arbre couvrant de poids minimum du graphe g en utilisant
    l'algorithme de Kruskal avec la structure UNION-FIND utilisant un tableau.

        :param g: un graphe (Graphe) connexe
        :return: un couple (t, l) où
        * t est un arbre (Graphe) couvrant de poids minimum de g
        * l est la liste telle que l[i] est l'arête ajoutée à l'itération i
        (None si aucune arête n'est ajoutée)

        :Examples:

        >>> kruskal_ufl(graphe_1())
        ({4: 0-1-1 0-2-2 1-4-3}, [(0, 1), (0, 2), None, (1, 3)])
        >>> kruskal_ufl(graphe_2())
        ({4: 0-1-2 1-4-3 2-3-3}, [(0, 2), (2, 3), (1, 3)])
        >>> kruskal_ufl(graphe_3(4))
        ({4: 0-1-1 0-2-2 1-4-3}, [(0, 1), (0, 2), None, (1, 3)])
        >>> kruskal_ufl(graphe_3(5))
        ({5: 0-1-1 0-2-2 1-4-3 2-6-4}, [(0, 1), (0, 2), None, (1, 3), None, (2, 4)])

    """

    n = g.nombre_sommets()
    t = Graphe(n)
    uf = ufl_creer(n)
    l = []

    ### À COMPLÉTER DÉBUT (Complexité O(n^2), environ 15 lignes)
    aretes = aretes_triees(g)
    cmp = 0
    for (i, j, poids) in aretes:

        # Vérifie si l'ajout de l'arête crée un cycle
        if ufl_find(uf, i) != ufl_find(uf, j):
            # Ajoute l'arête à l'arbre couvrant et à la liste des arêtes ajoutées
            t.ajouter_arete(i, j, poids)
            l.append((i, j))  # Ajoute l'arête à la liste
            # Fusionne les composantes connexes dans Union-Find
            ufl_union(uf, ufl_find(uf, i), ufl_find(uf, j))
            cmp+=1
        else:
            # Ajoute None si l'arête n'est pas ajoutée pour éviter les cycles
            l.append(None)

        if cmp == n - 1:
            break


    ### À COMPLÉTER FIN

    return (t, l)



########################################################
### Union-Find : Implémentation utilisant une forêt ###
########################################################

# Essayons de lancer l'algorithme écrit précédemment sur un graphe avec un
# nombre élevé de sommets.
# Décommentez les lignes suivantes et exécutez votre programme :

"""
t0 = time.time()

kruskal_ufl(graphe_3(4096)) # 0.62s sur ma machine (Intel Core i5)
t1 = time.time()
print("KRUSKAL_UFL: ", round(t1-t0, 2), "s", sep="")

quit()
"""

# Pour implémenter la version efficace de l'algorithme de Kruskal, nous allons
# maintenant implementer une structure UNION-FIND avec des forêts (comme dans le cours).
# Chaque composante connexe a un représentant, qui est la racine d'un arbre
# dans la forêt UNION-FIND. Au début de l'algorithme, comme il n'y a pas encore 
# d'arête, chaque sommet est seul dans sa composante connexe.
# Si lorsque l'on examine l'arête (uv), u et v appartiennent à la même composante 
# connexe (ont le même représentant), alors on n'ajoute pas l'arête,
# sinon on l'ajoute et on met à jour notre structure pour fusionner les
# composantes connexes de u et de v.
# Dans l'implémentation avec forêt, les opérations de find et union ne
# demandent que O(log(n)) opérations.
# Pour les détails, lisez l'article consacré sur Wikipédia :
# https://fr.wikipedia.org/wiki/Union-find#Impl%C3%A9mentation_utilisant_des_for%C3%AAts
# Nous utilisons le rang pour l'union, mais nous n'implémentons pas la 
# compression de chemin pour le find.

def uff_creer(n):
    """Retourne la structure UNION-FIND initialisée.

        La structure est une liste de n couples tel que le premier élément du
        couple i indique le parent de l'élément i (ou i si l'élément est la
        racine), et le second élément indique le rang de i.

        :param n: Nombre de sommets, entier naturel

        :Examples:

        >>> uff_creer(2)
        [[0, 0], [1, 0]]
        >>> uff_creer(5)
        [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]

    """

    ### À COMPLÉTER DÉBUT (Complexité O(n))
    return [[i,0] for i in range(n)]

    ### À COMPLÉTER FIN

def uff_find(l, v):
    """Retourne le représentant (racine) de la composante connexe du sommet i dans 
    la structure UNION-FIND l.

        :param v: Un indice d'un sommet, entier naturel compris entre 0 et n-1.

         :Examples:

                 0(3)
               / | \
              /  |  \
             /   |   \
            1(0) 2(1) 4(2)
                 |    | \
                 |    |  \
                 |    |   \
                 3(0) 5(0) 6(1)
                           |
                           |
                           |
                           7(0)

        >>> l = [[0, 3], [0, 0], [0, 1], [2, 0], [0, 2], [4, 0], [4, 1], [6, 0]]
        >>> uff_find(l, 0)
        0
        >>> l # non modifiée
        [[0, 3], [0, 0], [0, 1], [2, 0], [0, 2], [4, 0], [4, 1], [6, 0]]

        >>> uff_find(l, 1)
        0
        >>> l # non modifiée
        [[0, 3], [0, 0], [0, 1], [2, 0], [0, 2], [4, 0], [4, 1], [6, 0]]

        >>> uff_find(l, 4)
        0
        >>> l # non modifiée
        [[0, 3], [0, 0], [0, 1], [2, 0], [0, 2], [4, 0], [4, 1], [6, 0]]

        >>> uff_find(l, 3)
        0
        >>> l # non modifiée
        [[0, 3], [0, 0], [0, 1], [2, 0], [0, 2], [4, 0], [4, 1], [6, 0]]

                    0(3)
                    .
                    .
                    .
            1(0) 2(1) 3(0) 4(2)
                           | \
                           |  \
                           |   \
                           5(0) 6(1)
                                |
                                |
                                |
                                7(0)

        >>> uff_find(l, 7)
        0
        >>> l # non-modifiée
        [[0, 3], [0, 0], [0, 1], [2, 0], [0, 2], [4, 0], [4, 1], [6, 0]]
    """

    ### À COMPLÉTER DÉBUT (Complexité O(h) où h est la hauteur de l'arbre)
    while l[v][0] != v:
        v = l[v][0]  # On remonte vers le parent
    return v
    ### À COMPLÉTER FIN

def uff_union(l, i, j):
    """Fusionne les composantes connexes comprenant i et j dans la structure
    UNION-FIND l.

        Si les représentants de i et j ont même rang, alors la racine
        de l'union est la racine de i.

        :param i: Un sommet i, i in l
        :param j: Un sommet j, j in l, j != i

        :Examples:

            rang du représentant de i != rang de représentant de j

            1(1)  2(0)                   1(1)
            |                ->         / \
            |                          /   \
            0(0)                      0(1)  2(0)

        >>> l = [[1, 0], [1, 1], [2, 0]]
        >>> uff_union(l, 1, 2)
        >>> l
        [[1, 0], [1, 1], [1, 0]]

            2(1)  1(0)                   2(1)
            |                ->         / \
            |                          /   \
            0(0)                      0(1)  1(0)

        >>> l = [[2, 0], [1, 0], [2, 1]]
        >>> uff_union(l, 1, 2)
        >>> l
        [[2, 0], [2, 0], [2, 1]]

             rang du représentant de i = rang de représentant de j

            1(1)  2(1)   uff_union(1, 2)   1(2)
            |     |           ->          / \
            |     |                      /   \
            0(0)  3(0)                  0(0)  2(1)
                                              |
                                              |
                                              3(0)

        >>> l = [[1, 0], [1, 1], [2, 1], [2, 0]]
        >>> uff_union(l, 1, 2)
        >>> l
        [[1, 0], [1, 2], [1, 1], [2, 0]]

            1(1)  2(1)   uff_union(2, 1)   2(2)
            |     |           ->          / \
            |     |                      /   \
            0(0)  3(0)                  3(0)  1(1)
                                              |
                                              |
                                              0(0)

        >>> l = [[1, 0], [1, 1], [2, 1], [2, 0]]
        >>> uff_union(l, 2, 1)
        >>> l
        [[1, 0], [2, 1], [2, 2], [2, 0]]

    """

    ### À COMPLÉTER DÉBUT (Complexité O(h) où h est la hauteur de l'arbre)
    rep_i = uff_find(l,i)
    rep_j = uff_find(l, j)

    if l[rep_i][1] > l[rep_j][1]:
        # rep_i a un rang plus élevé, on rattache rep_j sous rep_i
        l[rep_j][0] = rep_i
    elif l[rep_i][1] < l[rep_j][1]:
        # rep_j a un rang plus élevé, on rattache rep_i sous rep_j
        l[rep_i][0] = rep_j
    else:
        # Les deux ont le même rang, on rattache rep_j sous rep_i
        # et on augmente le rang de rep_i
        l[rep_j][0] = rep_i
        l[rep_i][1] += 1
        

    ### À COMPLÉTER FIN

def kruskal_uff(g):
    """Retourne un arbre couvrant de poids minimum du graphe g en utilisant
    l'algorithme de Kruskal avec la structure UNION-FIND utilisant des forêts,
    et avec arrêt prématuré dès que le nombre d'arêtes ajoutées convient.

        :param g: un graphe (Graphe) connexe
        :return: un couple (t, l) où
        * t est un arbre (Graphe) couvrant de poids minimum de g
        * l est la liste telle que l[i] est l'arête ajoutée à l'itération i
        (None si aucune arête n'est ajoutée à cette itération)

        :Examples:

        >>> kruskal_uff(graphe_1())
        ({4: 0-1-1 0-2-2 1-4-3}, [(0, 1), (0, 2), None, (1, 3)])
        >>> kruskal_uff(graphe_2())
        ({4: 0-1-2 1-4-3 2-3-3}, [(0, 2), (2, 3), (1, 3)])
        >>> kruskal_uff(graphe_3(4))
        ({4: 0-1-1 0-2-2 1-4-3}, [(0, 1), (0, 2), None, (1, 3)])
        >>> kruskal_uff(graphe_3(5))
        ({5: 0-1-1 0-2-2 1-4-3 2-6-4}, [(0, 1), (0, 2), None, (1, 3), None, (2, 4)])
        >>> kruskal_uff(Graphe(7, [(0, 1, 1), (1, 2, 2), (3, 4, 3), (2, 4, 4), (0, 2, 5), (3, 5, 7), (0, 5, 6), (0, 6, 10)]))
        ({7: 0-1-1 0-6-5 0-10-6 1-2-2 2-4-4 3-3-4}, [(0, 1), (1, 2), (3, 4), (2, 4), None, (0, 5), None, (0, 6)])

    """

    n = g.nombre_sommets()
    t = Graphe(n)
    l = []
    uf = uff_creer(n)
    cmp = 0
    ### À COMPLÉTER DÉBUT (Complexité O(m log m))

    aretes = aretes_triees(g)
    for (i, j, poids) in aretes:

        # Vérifie si l'ajout de l'arête crée un cycle
        if uff_find(uf, i) != uff_find(uf, j):
            # Ajoute l'arête à l'arbre couvrant et à la liste des arêtes ajoutées
            t.ajouter_arete(i, j, poids)
            l.append((i, j))  # Ajoute l'arête à la liste
            # Fusionne les composantes connexes dans Union-Find
            uff_union(uf, uff_find(uf, i), uff_find(uf, j))
            cmp+=1
        else:
            # Ajoute None si l'arête n'est pas ajoutée pour éviter les cycles
            l.append(None)

        if cmp == n - 1:
            break


    ### À COMPLÉTER FIN

    return (t, l)


    ### À COMPLÉTER FIN

    return (t, l)
# Décommentez les lignes suivantes pour comparer la différence de temps
# d'exécution entre les deux implémentations de la structure UNION-FIND:

"""
t0 = time.time()
n = 4096
g = graphe_3(n)

kruskal_ufl(g) # 0.62s sur ma machine (Intel Core i5)
t1 = time.time()
print("KRUSKAL_UFL: ", round(t1-t0, 2), "s", sep="")

kruskal_uff(g) # 0.13s sur ma machine (Intel Core i5)
t2 = time.time()
print("KRUSKAL_UFF: ", round(t2-t1, 2), "s", sep="")

quit()
"""

#####################################
### Algorithme de Kruskal inversé ###
#####################################

#-----------------TP02----------------
def creer_file(n):
    """Retourne une file (File) dont le nombre d'éléments est <= n.

        :param n: nombre maximum d'éléments ajoutés à la file.

        :Examples:

        >>> creer_file(3)
        [[-1, -1, -1], 0, -1]

    """

    ### À COMPLÉTER DÉBUT
    return [[-1]*n, 0, -1]
    ### À COMPLÉTER FIN

def enfiler(f, e):
    """Ajoute un élément à la fin de la file f.

        :param f: une file
        :param e: élément à ajouter à la file

        :Examples:

        >>> f = creer_file(3)
        >>> f
        [[-1, -1, -1], 0, -1]

        >>> enfiler(f, 2)
        >>> f
        [[2, -1, -1], 0, 0]

        >>> enfiler(f, 3)
        >>> f
        [[2, 3, -1], 0, 1]

    """

    tab = f[0]

    ### À COMPLÉTER DÉBUT
    f[2] = f[2] + 1
    tab[f[2]] = e
    ### À COMPLÉTER FIN

def defiler(f):
    """Supprime et retourne le premier élément de la file f.

        :param f: une file

        :Examples:

        >>> f = creer_file(4)
        >>> enfiler(f, 2)
        >>> enfiler(f, 3)
        >>> enfiler(f, 5)
        >>> f
        [[2, 3, 5, -1], 0, 2]

        >>> defiler(f)
        2
        >>> defiler(f)
        3
        >>> defiler(f)
        5
        >>> f
        [[2, 3, 5, -1], 3, 2]

    """

    tab = f[0]

    ### À COMPLÉTER DÉBUT
    elem = tab[f[1]]
    f[1] = f[1]+1

    return elem 
### À COMPLÉTER FIN

def est_vide(f):
    """Renvoie True si la file f est vide.

        :param f: une file

        :Examples:

        >>> f = creer_file(2)
        >>> est_vide(f)
        True
        >>> enfiler(f, 2)
        >>> enfiler(f, 3)
        >>> est_vide(f)
        False
        >>> defiler(f)
        2
        >>> est_vide(f)
        False
        >>> defiler(f)
        3
        >>> est_vide(f)
        True

    """

    ### À COMPLÉTER DÉBUT

    return f[1]>f[2]
    
    ### À COMPL ÉTER FIN
def est_connexe(g):
    """Retourne True si g est connexe, False sinon.

        :param g: Un graphe (Graphe)

        :Examples:

        >>> est_connexe(graphe_1())
        True
        >>> est_connexe(graphe_2())
        True
        >>> est_connexe(Graphe(1))
        True
        >>> est_connexe(Graphe(6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]))
        True
        >>> est_connexe(Graphe(6, [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (4, 5)]))
        True
        >>> est_connexe(Graphe(2))
        False
        >>> est_connexe(Graphe(5))
        False
        >>> est_connexe(Graphe(4, [(0, 1), (2, 3)]))
        False
        >>> est_connexe(Graphe(5, [(0, 1), (1, 2), (2, 3)]))
        False
        >>> est_connexe(Graphe(5, [(i, j) for i in range(0, 4) for j in range(i+1, 4)]))
        False
        >>> est_connexe(Graphe(6, [(i, j) for i in range(0, 5) for j in range(i+1, 5)]))
        False
        >>> est_connexe(Graphe(6, [(0, 1), (0, 2), (1, 2), (3, 4), (4, 5), (3, 5)]))
        False
        >>> est_connexe(Graphe(8,
        ...     [(i, j) for i in range(0, 4) for j in range(i+1, 4)] +
        ...     [(i, j) for i in range(4, 8) for j in range(i+1, 8)]))
        ...
        False

    """

    # N'oubliez pas que les parcours de graphe sont des grands classiques à connaître !

    ### À COMPLÉTER DÉBUT
    u=0
    file = creer_file(g.nombre_sommets())
    vu = set()
    enfiler(file,u)
    liste = []
    vu.add(u)
    while not est_vide(file):
        v=defiler(file)
        liste.append(v)
        for k in g.voisins(v):
            if k not in vu :
                vu.add(k)
                enfiler(file,k)
    nbr = g.nombre_sommets()
    if (len(liste) < nbr):
        return False
    else :
        return True
    ### À COMPLÉTER FIN

def kruskal_inverse(g):
    """Retourne un arbre couvrant de poids minimum du graphe g en utilisant
    l'algorithme de Kruskal inverse : on commence avec toutes les arêtes de g,
    et on enlève les arêtes une par une si elles ne déconnectent pas le graphe, 
    en allant de la plus lourde à la moins lourde.

        :param g: un graphe (Graphe) connexe
        :return: un couple (t, l) où
        * t est un arbre (Graphe) couvrant de poids minimum de g
        * l est la liste telle que l[i] est l'arête retirée à l'itération i
        (None si aucune arête n'est retirée)

        :Examples:        >>> graphe_1()
        {4: 0-1-1 0-2-2 1-3-2 1-4-3}

        >>> kruskal_inverse(graphe_1())
        ({4: 0-1-1 0-2-2 1-4-3}, [None, (1, 2)])
        >>> kruskal_inverse(graphe_2())
        ({4: 0-1-2 1-4-3 2-3-3}, [(0, 1), (0, 3), (1, 2)])
        >>> kruskal_inverse(graphe_3(4))
        ({4: 0-1-1 0-2-2 1-4-3}, [(2, 3), None, (1, 2)])
        >>> kruskal_inverse(graphe_3(5))
        ({5: 0-1-1 0-2-2 1-4-3 2-6-4}, [(3, 4), None, (2, 3), None, (1, 2)])

    """

    n = g.nombre_sommets()
    t = copy.copy(g)
    l = []

    ### À COMPLÉTER DÉBUT (Complexité O(m(n+m)), environ 10 lignes)
    aretes = aretes_triees(g)
    ### À COMPLÉTER FIN
    cmp = 0
    while aretes:
        u, v, _ = aretes.pop()
        
        # Créer une copie temporaire de t pour tester la connexité après suppression de l'arête
        g1 = copy.copy(t)
        g1.supprimer_arete(u, v)
        
        # Si g1 est toujours connexe, l'arête (u, v) peut être supprimée dans t
        if est_connexe(g1):
            t.supprimer_arete(u, v)
            l.append((u, v))
            cmp += 1
        else:
            l.append(None)
        
    while l[-1] is None:
        l.pop()

    return (t, l)



##########################
### Algorithme de Prim ###
##########################

# Le pseudo-code de l'algorithme de Prim se trouve sur Wikipédia :
# https://fr.wikipedia.org/wiki/Algorithme_de_Prim
# Son implémentation requiert l'utilisation d'une structure de file de
# priorité. Il ne vous est pas demandé d'implémenter une telle structure pour
# ce TP (mais ça le sera pour le TP suivant :) ). Ici, vous pouvez utiliser la
# classe TasBinomial qui vous est fournie et s'utilise ainsi :

# Créer une file de priorité contenant des éléments indicés de 0 à n-1 :
# >>> f = TasBinomial(n)
# Ajouter un élément v de cout c ou mettre à jour son cout s'il est déjà dans
# la file :
# >>> f.ajouter(v, c)
# Retirer l'élément de cout minimum :
# >>> v, cv = f.retirer()
# Obtenir le cout de l'élément d'indice v (retourne float('inf') si v n'est pas
# dans la file) :
# >>> c = f.cout(v)
# Pour savoir si la file est vide :
# >>> f.est_vide()

def prim(g):
    """Retourne un arbre couvrant de poids minimum du graphe g en utilisant
    l'algorithme de Prim.

        Le sommet de départ est le sommet d'indice 0.

        :param g: un graphe (Graphe) connexe
        :return: un couple (t, l) où
        * t est un arbre (Graphe) couvrant de poids minimum de g
        * l est une liste telle que l[u] est l'itération à laquelle le sommet u
        a été traité.

        :Examples:

        >>> prim(graphe_1())
        ({4: 0-1-1 0-2-2 1-4-3}, [0, 1, 2, 3])
        >>> prim(graphe_2())
        ({4: 0-1-2 1-4-3 2-3-3}, [0, 3, 1, 2])
        >>> prim(graphe_3(4))
        ({4: 0-1-1 0-2-2 1-4-3}, [0, 1, 2, 3])
        >>> prim(graphe_3(5))
        ({5: 0-1-1 0-2-2 1-4-3 2-6-4}, [0, 1, 2, 3, 4])

    """

    # Petite astuce pour économiser une ligne :
    # >>> it = iter(range(n))
    # >>> next(it)
    # 0
    # >>> next(it)
    # 1
    # ...

    n = g.nombre_sommets()
    pred = [None] * n
    l = [None] * n  # l[v] == None <=> v n'a pas encore été ajouté
    t = Graphe(n)
    f = TasBinomial(n)
    iteration = -1  # Compteur pour l'itération

    # Initialisation avec le sommet de départ (indice 0)
    f.ajouter(0, 0)
    l[0] = 0  # Marque le sommet 0 comme traité en premier
    iteration += 1

    while not f.est_vide():
        # Retirer le sommet avec le coût minimal
        u, cost = f.retirer()
        
        # Si `u` n'est pas le premier sommet, ajouter l'arête correspondante à `t`
        if pred[u] is not None:
            t.ajouter_arete(pred[u], u, cost)

        # Marquer l'itération où `u` a été traité
        l[u] = iteration
        iteration += 1

        # Pour chaque voisin `v` de `u`, vérifier et mettre à jour les coûts
        for v, weight in g.voisins_avec_poids(u):
            if l[v] is None and (f.cout(v) > weight):  # Si `v` n'a pas encore été ajouté et coût supérieur
                f.ajouter(v, weight)  # Met à jour le coût du sommet voisin `v`
                pred[v] = u  # Mettre à jour le prédécesseur

    return (t, l)

def graphe_4(n):
    """Retourne le graphe G4 à n+2 sommet, tel que le sous-graphe induit par les
    n premiers sommets est complet avec un poids de 2 sur chaque arête, et G4
    contient les arêtes (0,n) avec un poids de 1 et (0,n+1) avec un poids de 3.

        :param n: Nombre de sommets, entier naturel non nul

        n
         \     /2
         3\   /
           \ /  2
            0---- ...
           / \
         1/   \
         /     \2
        n+1

        :Examples:

        >>> graphe_4(1)
        {3: 0-1-1 0-3-2}
        >>> graphe_4(2)
        {4: 0-2-1 0-1-2 0-3-3}
        >>> graphe_4(3)
        {5: 0-2-1 0-2-2 0-1-3 0-3-4 1-2-2}

    """

    g = Graphe(n+2)
    for u in range(n):
        for v in range(u+1, n):
            g.ajouter_arete(u, v, 2)
    g.ajouter_arete(0, n,   1)
    g.ajouter_arete(0, n+1, 3)
    return g

# Décommentez les lignes suivantes pour comparer la différence de temps
# d'exécution entre les différents algorithmes implémentés.
# Quelques résultats à noter :
# * L'algorithme de Kruskal inversé est toujours beaucoup plus lent que les
# autres algorithmes.
# * L'algorithme de Prim est le plus efficace sur les graphes denses, comme
# G4(n). Il bat largement les différentes versions de l'algorithme de Kruskal.
# * L'algorithme de Kruskal avec l'UNION-FIND utilisant les forêts est le plus
# rapide sur les graphes peu denses, comme G3(n), mais Prim n'est vraiment pas
# loin.
# * Sur les graphes denses, comme G4(n), l'algorithme de Kruskal avec
# l'UNION-FIND utilisant les forêts est un peu moins rapide que celui utilisant
# le tableau.

"""
g = graphe_4(1024)
# g = graphe_3(8192)
t0 = time.time()

# kruskal_inverse(g) # Beaucoup trop long sur ma machine... (Intel Core i5)
t1 = time.time()
# print("KRUSKAL_INV: ", round(t1-t0, 2), "s", sep="")

kruskal_ufl(g) # 0.48s sur ma machine (Intel Core i5)
t2 = time.time()
print("KRUSKAL_UFL: ", round(t2-t1, 2), "s", sep="")

kruskal_uff(g) # 0.63s sur ma machine (Intel Core i5)
t3 = time.time()
print("KRUSKAL_UFF: ", round(t3-t2, 2), "s", sep="")

prim(g) # 0.3s sur ma machine (Intel Core i5)
t4 = time.time()
print("PRIM:        ", round(t4-t3, 2), "s", sep="")

quit()
"""


if __name__ == "__main__":
    import doctest
    fonctions = [
            graphe_1,
            graphe_2,
            graphe_3,
            aretes_triees,
            ufl_creer,
            ufl_find,
            ufl_union,
            kruskal_ufl,
            uff_creer,
            uff_find,
            uff_union,
            kruskal_uff,
            est_connexe,
            kruskal_inverse,
            prim,

    ]
    for f in fonctions:
        print("**********************************************************************")
        print(f.__name__)
        doctest.run_docstring_examples(f, globals(), optionflags=doctest.FAIL_FAST)

 