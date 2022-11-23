import os

def createfile(name):
    file = open(name + '.osk', 'w')
    file.write("")
    file.close()

def readFile(name2):
    with open(name2) as f:
        print(f.readlines())

def writefile(name3,writetxt):
    file = open(name3, 'w')
    file.write(writetxt)
    file.close