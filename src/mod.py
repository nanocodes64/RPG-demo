from json import dumps, loads
from time import sleep
from os import chdir, system
class JSONINTERFACE:
    def __init__(self, current_file):
        self.cfile = current_file
    def fetch(self, toFetch):
        chdir("mods")
        readF = open(self.cfile, "r")
        jsonF = loads(readF.read())
        readF.close()
        chdir("..")
        if  toFetch=="A_A_A_A":
            return jsonF
        else:
            return jsonF[toFetch]
    

        
            
