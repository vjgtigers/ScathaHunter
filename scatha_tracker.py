import time
import threading
start = time.time()

import json


###ACOMMPLISHMENTS
#back to back scathas
#some number without a scatha
#quickest time between worms/scathas
#longest time between
#scatha farming time


#print(start)
from pynput import keyboard
import os
x = 0
runner = True
scatha1 = 1
worm1 = 0
scathaList = ["None","None","None","None","None","None","None4","None3","None2","None1"]


def thread_function():
    global x
    global runner
    global scatha1
    global worm1
    global start
    while runner:
        time.sleep(1)
        os.system('cls')
        print("Scathas: "+str(scatha1) + "\t \t \t \t \t 1." + scathaList[len(scathaList)-1])
        print("Worms: "+str(worm1) + "\t \t \t \t \t 2." + scathaList[len(scathaList)-2])
        total = worm1+scatha1
        if total<94:
            print("Next Bestiary: "+str(94-(worm1+scatha1)) + " \t \t \t 3." + scathaList[len(scathaList)-3])
        else:
            print("Please add this part")
        conTime = time.time()-start
        if total != 0:
            print("Avg Time Per Worm: " + str(round(conTime/total,2)) + "\t \t 4." + scathaList[len(scathaList)-4])
        else: print("none")
x1 = threading.Thread(target=thread_function)
x1.start()



def scatha():
    print("scatha")
    global x
    global scatha1
    scatha1 +=1
def worm():
    print("worm")
    global worm1
    worm1 +=1

def on_activate_i():
    print('<ctrl>+<alt>+i pressed')
def quitter():
    global runner
    runner = False
    exit()

pp = {
    'm': scatha,
    'n': worm,
    '<ctrl>+<alt>+i': on_activate_i,
    '<ctrl>+<alt>+b': quitter,


}
with keyboard.GlobalHotKeys(pp) as h:
    h.join()
