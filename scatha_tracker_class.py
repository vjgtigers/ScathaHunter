import threading
from pynput import keyboard
import os
import json
import time
import webbrowser
import threading

class mainTracker():
    save = {
        "scathaList" : ["None","None","None","None","None","None","None4","None3","None2","None1"],
        "achievments": [[0,["BackToBack", "Get 2 Scathas back to back"]],[0,["Unlikely", "Get 2 Worms within 40 Sec"]], [0,["Impossible?", "Get 2 Worms within 30 Sec"]]],
        "userData": [],
        "initalData": [],
        "recordedData":[0,0],
        "sv" : "0.0.1"
    }
    sessionWorm = 0
    sessionScatha = 0
    startTime = time.time()
    fromLast = 0
    isActive = True
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
        elif os.path.isfile(self.path+"/save.txt") == True and input("Would you like to open current save? (y/n):") == "y":
                with open(self.path+"/save.txt") as saveImport:
                    self.save = json.load(saveImport)
                print(self.save)
                self.initThreads()
        else:
            print("returning to homescreen")
            time.sleep(2)
            return homeScreen()


    def initThreads(self):
        #self.keyTracker()
        #keyThread = threading.Thread(target=self.keyTracker)
        #keyThread.start()
        #keyThread.join()
        printThread = threading.Thread(target=self.thread_function)
        printThread.start()
        #printThread.join()
        #self.isActive =False
        #exit()
        pp = {
            'm': self.scathaCall,
            'n': self.wormCall,
            'b': self.quitter

        }
        with keyboard.GlobalHotKeys(pp) as self.h:
            self.h.join()




        print("next")


    def thread_function(self):
        initScatha = self.save["initalData"][0]
        initWorm = self.save["initalData"][1]
        start = time.time()
        while self.isActive:
            time.sleep(1)
            scathaList = self.save["scathaList"]
            os.system('cls')
            print(self.isActive)
            print("Session Scathas: " + str(self.sessionScatha) + "\t \t \t \t \t 1." + self.save["scathaList"][len(scathaList) - 1])
            print("Session Worms: " + str(self.sessionWorm) + "\t \t \t \t \t 2." + self.save["scathaList"][len(scathaList) - 2])
            total = self.sessionScatha + self.sessionWorm
            conTime = time.time() - start
            if total != 0:
                print("Avg Time Per Worm: " + str(round(conTime / total, 2)) + " sec" + " \t\t\t 4." + self.save["scathaList"][len(scathaList) - 3])
            else:
                print("none")
            print("Last Scatha:" + str(round(time.time() - self.fromLast)) + " Sec" + "\t \t \t\t 5." + self.save["scathaList"][len(scathaList) - 4])
            print("Scatha Find RNG:", end="")
            if total != 0:
                if self.sessionScatha / total > .2:
                    print("above RNG", end="")
                elif self.sessionScatha / total < .2:
                    print("below RNG", end="")
                else:
                    print("Equal RNG", end="")
                print("\t \t \t 5." + scathaList[len(scathaList) - 6])
            else:
                print("Summon a worm/Scatha!!")
        os.system("cls")
        return homeScreen()


    def saveSave(self):

        with open(self.path + "/save.txt", "w") as outfile:
            json.dump(self.save, outfile)


    def keyTracker(self): #i dont think currently in use
        pp = {
            'm': self.scathaCall,
            'n': self.wormCall,
            'b': self.quitter,
            'v': self.quitter

        }
        with keyboard.GlobalHotKeys(pp) as self.h:
            self.h.join()

    def scathaCall(self):
        print("scatha")

        self.save["scathaList"].append("Scatha")
        self.fromLast = time.time()
        self.sessionScatha +=1
        self.save["recordedData"][0] += 1
        self.saveSave()


    def wormCall(self):
        print("worm")

        self.save["scathaList"].append("worm")
        self.fromLast = time.time()
        self.sessionWorm +=1
        self.save["recordedData"][1] += 1
        self.saveSave()

    def quitter(self):
        self.h.stop()
        self.isActive = False
        print("wuitting")

class viewAch():
    path = "scathSave"
    def __init__(self):
        os.system("cls")
        print("not yet developed")
        #time.sleep(2)
        #return homeScreen()

        if os.path.isfile(self.path + "/save.txt"):
            with open(self.path + "/save.txt") as saveImport:
                self.save = json.load(saveImport)

        #print(self.save["achievments"][0][1][0])
        isCom = lambda i: f" -Complete- " if i[0] == 1 else f" -Incomplete- "
        for i in self.save["achievments"]:
            print(i[1][0] + isCom(i) + i[1][1])


class info():
    def __init__(self):
        os.system("cls")
        print("not yet fully developed - achivements will not currently show that they have been completed.")
        print("However they should be able to be completed retroactivly")
        #time.sleep(2)
        #return homeScreen()
        self.options()


    def abKey(self):
        print("=====KEY TRACKER INFO=====")
        print("Moduel: pynput")
        print("The only time this program moniters keypresses outside of window is in scatha tracking mode")
        print("This can be easily varified in the code - unless i made a mistake :/")
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