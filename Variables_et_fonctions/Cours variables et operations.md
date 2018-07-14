# Cours : Variables et opérations

### Première partie : Les variables

Une variable en informatique permet de garder en mémoire (le temps que le programme s'exécute) des données comme par exemple le résultat d'un calcul ou un mot, une liste ou bien d'autres choses.  
Pour stocker en mémoire une valeur dans une variable, on utilise simplement le signe égal =.  
Par exemple : 
```python
a=3
b=7
c=b+a+2
```
Dans cet exemple, on a mis en mémoire 3 variables. Dans a, on a stocké la valeur 3, dans b la valeur 7 et dans c la valeur 12. Remarque importante : ce qui est stocké est le résultat du calcul et non le calcul. Ce qui veut dire que si on modifie la valeur de a, la variable c elle restera à 12.

Pour afficher la valeur d'une variable, on utilise la fonction `print`. Appuyez sur le bouton Run pour voir l'effet du code ci-dessous :
```python runnable
a=3
b=7
c=b+a+2
print(c)
```
On voit s'afficher la valeur de c. 

### Deuxième partie : Les opérations sur les variables numériques

Dans cette partie, nous allons voir les opérations de base que l'on peut effectuer en python sur des nombres.

1. Il y a bien sur les quatre opérations classiques +, -, \*, / avec les priorités opératoires habituelles. Par exemple :
```python runnable
a=5
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
```
2. Les deux autres opérations qu'on utilise couramment sont les puissances et la racine carrée.  
Pour les puissances, on double simplement la multiplication. Ainsi $`x^n`$ s'obtiendra en écrivant `x**n`.  
Pour la racine carrée, on va simplement utiliser une propriété mathématique : $`\sqrt x = x^{0.5}`$. Donc pour calculer la racine carrée d'un nombre x, il suffit d'écrire `x**0.5`.  Voici quelques exemples. On a rajouté des commentaires à coté des instructions d'affichage des calculs pour que ces instructions soient plus claires. Pour écrire un commentaire, il suffit de mettre un # devant. Tout ce qui suit le # ne sera pas executé par l'ordinateur et ne sert donc qu'à la personne qui lit le programme.
```python runnable
print(2**3) # Affiche le résultat de 2 puissance 3
print(3**2) # Affiche le résultat de 3 puissance 2
print(9**0.5) # Affiche la racine carrée de 9
print(2**0.5) # Affiche la racine carrée de 2
```
