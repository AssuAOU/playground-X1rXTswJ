# A modifier si besoin
nom_fonction="Mandelbrot"

#liste des valeurs à tester
# Attention de bien mettre dans un tuplet ou une liste les valeurs à tester même si la fonction n'a qu'un argument.
valeurs_a_tester=[[3.9], [complex(-1,1)],[complex(0.5,0.5)],[complex(1,1)],[complex(-1,0.5)]]



#message d'aide si besoin
help="N'oublie pas d'utiliser return pour renvoyer le resultat."

#------------------------------------
# Les imports
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw

import sys
# On rajoute le chemin de ma_bao.py dans le sys.path
sys.path.append("/project/target")
# Ma boite à outils
from ma_bao import * 
# Donne les noms du dossier et du module (automatiquement avec __file__
chemin,module=donner_chemin_nom(__file__)
# On teste s'il n'y a pas d'erreurs de synthaxe etc. et on les montre si besoin
tester("from {} import *".format(module),globals()) 
# On renomme ma fonction f
f=eval(nom_fonction)
# Si le mot de passe est bon on affiche la correction
try :  
    cheat(chemin+module,mdp) 
except: pass
# On récupère la fonction solution
exec("from {}_Correction import {} as f_sol".format(module,nom_fonction))

#--------------------------------------
BORNE = 1000
MAX_ITER = 200
WIDTH,HEIGHT = 900,600
X_MIN,Y_MIN,X_MAX = -2,-2,4 # Valeurs min et max pour les parties reelles et imaginaires
Y_MAX=Y_MIN+HEIGHT*(X_MAX-X_MIN)/WIDTH #Pour avoir un repère normé


def creer_image(max_iter=MAX_ITER):
    im = Image.new('HSV', (WIDTH, HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    X = np.linspace(X_MIN, X_MAX, WIDTH)
    Y = np.linspace(Y_MIN, Y_MAX, HEIGHT)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            n=mandelbrot(complex(X[x],Y[y]))
            draw.point((x, y), (n%255, 255, 255 if n < max_iter else 0))
    im.convert('RGB').save('output.png', 'PNG')
    
    
def test():
    try:
        for valeur in valeurs_a_tester:
            rep=f(*valeur)
            sol=f_sol(*valeur)
            assert str(rep) == str(sol), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(",".join([str(val) for val in valeur]),str(rep),str(sol))
            send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(",".join([str(val) for val in valeur]),str(rep)))
        creer_image()
        print("TECHIO> open -s /project/target/ index_grossissant.html")
        success(chemin+module)
    except AssertionError as e:
        fail()
        send_msg("Oops! ", e)
        if help:
            send_msg("Aide 💡", help)


#--------------------------------------
if __name__ == "__main__": test()
