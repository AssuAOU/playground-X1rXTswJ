from Prise_en_main_Exo_1 import mon_programme
import sys
import io

#modifications de mon_programme si necessaire
mon_programme_modifié=lambda a,b: round(mon_programme(a,b),5)

#liste des couples input/output
input_output=[\
((3,4),7),\
((0,0),0),\
((-1,4),3),\
((2.4,-3.1),-0.7)\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser return pour renvoyer le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        sauvegarde_stdout=sys.stdout
        sauvegarde_stderr=sys.stderr
        sys.stdout=io.StringIO()
        sys.stderr=io.StringIO()
        mon_programme_modifié(*inp)
              count1 = sys.stdout.getvalue()
        message_erreur=sys.stderr.getvalue()
        sys.stdout=sauvegarde_stdout
        sys.stderr=sauvegarde_stderr
        send_msg("Messages pour débugguer",message_erreur)
        assert count1 == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__":
	test()
