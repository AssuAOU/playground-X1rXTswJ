#Ne pas oublier de changer le module à importer
module="Chaines_caracteres/Pliage_papier"

import sys
import io
from ma_bao import *
tester("from Pliage_papier import mon_programme",globals())




#liste des couples input/output
input_output=[\
(1,"G"),\
(2,"GGD"),\
(3,"GGDGGDD"),\
(6,"GGDGGDDGGGDDGDDGGGDGGDDDGGDDGDDGGGDGGDDGGGDDGDDDGGDGGDDDGGDDGDD"),\
(8,"GGDGGDDGGGDDGDDGGGDGGDDDGGDDGDDGGGDGGDDGGGDDGDDDGGDGGDDDGGDDGDDGGGDGGDDGGGDDGDDGGGDGGDDDGGDDGDDDGGDGGDDGGGDDGDDDGGDGGDDDGGDDGDDGGGDGGDDGGGDDGDDGGGDGGDDDGGDDGDDGGGDGGDDGGGDDGDDDGGDGGDDDGGDDGDDDGGDGGDDGGGDDGDDGGGDGGDDDGGDDGDDDGGDGGDDGGGDDGDDDGGDGGDDDGGDDGDD")\
]


#message d'aide si besoin
help=""



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    afficher_correction(module)
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
