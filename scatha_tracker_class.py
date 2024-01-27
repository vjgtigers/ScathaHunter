import threading
from pynput import keyboard
import os
import json
import time
import webbrowser

class mainTracker():
    save = {
        "scathaList" : ["None","None","None","None","None","None","None4","None3","None2","None1"],
        "achievments": [],
        "userData": [],
        "initalData": []
    }
    sessionWorm = 0
    sessionScatha = 0
    startTime = time.time()
    fromLast = 0
    def __init__(self):
        self.path = "scathSave"
        isExist = os.path.exists(self.path)
        if not isExist:
            os.mkdir(self.path)
        if os.path.isfile(self.path+"/save.txt") == False:
            u_in = input("No save file detected. Would you like to make a new save? (y/n): ")
            if u_in == "y":
                print("creating new save")
                corrInit = True
                while corrInit:
                    self.scathaInitAmout = int(input("scatha kills:"))
                    self.wormInitAmout = int(input("worm kills:"))
                    self.totalInitAmout = int(input("total kills:"))
                    if self.scathaInitAmout+self.wormInitAmout == self.totalInitAmout:
                        self.save["initalData"] = [self.scathaInitAmout,self.wormInitAmout,self.totalInitAmout]
                        with open(self.path+"/save.txt", "w") as outfile:
                            json.dump(self.save, outfile)
                        corrInit = False
                    else:
                        os.system("cls")
                        print("error. Please try again")

            else:
                print("exiting program")
                exit()


    isActive = True


    def scathaCall(self):
        print("scatha")
        global fromLast
        self.save["scathaList"].append("Scatha")
        self.fromLast = time.time()
        self.sessionScatha +=1
    def worm(self):
        print("worm")
        global worm1
        global fromLast
        global scathaList
        self.save["scathaList"].append("worm")
        self.fromLast = time.time()
        self.sessionWorm +=1
    def quitter(self):
        self.isActive = False


class viewAch():
    def __init__(self):
        print("not yet developed")
        time.sleep(2)
        return homeScreen()
class info():
    def __init__(self):
        print("not yet fully developed")
        #time.sleep(2)
        #return homeScreen()
        self.options()
    def abKey(self):
        print("=====KEY TRACKER INFO=====")
        print("Moduel: pynput")
        print("The only time this program moniters keypresses outside of window is in scatha tracking mode")
        print("This can be easily varified in the code")
    def options(self):
        print("1. Open Github page in broswer")
        print("2. About KeyTracker")
        print("3. Return to home")
        uin = input("Choose number: ")
        if uin == "1":
            webbrowser.open("https://github.com/vjgtigers/ScathaHunter", new=0, autoraise=True)
        if uin == "2":
            self.abKey()
        if uin == "3":
            return homeScreen()

def programEnd():
    print("Exiting Program")
    exit()
def homeScreen():
    os.system("cls")
    print("1. Start Tracker")
    print("2. View Achivements")
    print("3. Info")
    print("4. Exit Program")
    uin = input("chose Number: ")
    if uin == "1":
        mainTracker()
    elif uin == "2":
        viewAch()
    elif uin == "3":
        info()
    elif uin == "4":
        programEnd()

homeScreen()