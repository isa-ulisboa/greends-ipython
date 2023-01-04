#25.11 gewoon overgeschreven van bord (zijn file: iPython_lesson_7_api.py)
#API file maken: dit is zoals een functie maar dan een file, dus jij (een consultant bvb) maakt een code voor een bedrijf en zij geven zelf argumenten mee
#je moest eerst iets doen in terminal hieronder om argumenten mee te geven, hoe? zie word file 
import sys 
args = sys.argv
print(args)

#try en except is een methode voor als er mogelijks errors zijn dus je doet 
try: 
    nameofscript = args[0]
    in1 = args[1]   #als je geen argumenten meegegeven hebt krijg je hier een error, dit type error is een indexerror
    in2 = args[2]
    in3 = args[3]

    res = in1 + in2 + in3 #+ doet som voor nummers en concatenates in geval vn strings
    print(res)
    res = in1 * in2 * in3 #geeft error indien argumenten strings zijn dit type error is een syntaxerror 
except  IndexError: #als er een indexerror is, laat dan volgende boodschap verschijnen:
    print("you did not specify arguments")
except Exception as err: 
    print(f"unexpected {err=}, {type(err)=}")

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--lon')