#Ne pas oublier de changer le module à importer
from Nature_d_un_triangle import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
((3,4,5),"RECTANGLE"),\
((3,5,4),"RECTANGLE"),\
((2,2,3),"ISOCELE"),\
((2,3,2),"ISOCELE"),\
((2,2,2),"EQUILATERAL"),\
((2,3,4),"QUELCONQUE"),\
((1,1,1.4142135623730951),"RECTANGLE ISOCELE"),\
((1.4142135623730951,2,1.4142135623730951),"RECTANGLE ISOCELE"),\
((1.618033988749895,1.618033988749895,1),"TRIANGLE D'OR"),\
((1.618033988749895,1,1.618033988749895),"TRIANGLE D'OR")\
]


#message d'aide si besoin
help="N'oublie pas qu'être rectangle ou isocèle doit se vérifier aux 3 sommets."



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(*inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp) or (outp=="TRIANGLE D'OR" and str(count1)=="ISOCELE"), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        if str(count1)=="TRIANGLE D'OR":
            send_msg("Tests validés", "Très bien ! Le triangle est bien un triangle d'or."
        else:
            send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
