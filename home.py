import os
from subprocess import *
import time
from oskextention import *

os.system('cls')

kosnum = 12
num1fw = 1
opennum = 6
readnum = 10
wrnum = 11


while True:
    Q = input("")
    if Q == "shutdown":
            quit()
    else:
        if Q == "time":
            print(time.strftime("%I:%M:%S %p"))
        else:
            if Q == "help":
                print("""
                help - Gives you the list of commands
                time - tells the time
                shutdown - turns off the OS
                open - opens a file/app
                createFile - creates file with .osk extention
                readFile - reads the .osk file
                writeFile - writes in the .osk file
                clear - clear terminal""")
            else:
                if "open" in Q:
                    loopon2 = True
                    while loopon2:
                        if Q[opennum] == ")":
                            loopon2 = False
                        else:
                            opennum = opennum + num1fw
                    nameo = Q[5:opennum]
                    os.startfile(nameo)
                else:
                    if "createFile" in Q:
                        loopon = True
                        while loopon:
                            if Q[kosnum] == ")":
                                loopon = False
                            else:
                                kosnum = kosnum + num1fw
                        namecf = Q[11:kosnum]
                        createfile(namecf)
                    else:
                        if "readFile" in Q:
                            loopon3 = True
                            while loopon3:
                                if Q[readnum] == ")":
                                    loopon3 = False
                                else:
                                    readnum = readnum + num1fw
                            namer = Q[9:readnum]
                            namer = namer + ".osk"
                            readFile(namer)
                        else:
                            if "writeFile" in Q:
                                loopon3 = True
                                while loopon3:
                                    if Q[wrnum] == ",":
                                        loopon3 = False
                                    else:
                                        wrnum = wrnum + num1fw
                                namew = Q[9:wrnum]
                                namew = namew + ".osk"
                                keepwr = wrnum + 1
                                loopon3 = True
                                while loopon3:
                                    if Q[wrnum] == ")":
                                        loopon3 = False
                                    else:
                                        wrnum = wrnum + num1fw
                                namet = Q[keepwr:wrnum]
                                namew = namew.replace('(', '')
                                writefile(namew,namet)
                            else:
                                if Q == "clear":
                                    os.system('cls')
                                else:
                                    print("Syantax error!")