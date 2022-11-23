from importlib.resources import contents
from subprocess import call
import os

print("""
██╗░░██╗██╗███╗░░██╗░██████╗░░░░░░░░█████╗░░██████╗
██║░██╔╝██║████╗░██║██╔════╝░░░░░░░██╔══██╗██╔════╝
█████═╝░██║██╔██╗██║██║░░██╗░█████╗██║░░██║╚█████╗░
██╔═██╗░██║██║╚████║██║░░╚██╗╚════╝██║░░██║░╚═══██╗
██║░╚██╗██║██║░╚███║╚██████╔╝░░░░░░╚█████╔╝██████╔╝
╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░░░░░╚════╝░╚═════╝░


""")

def doesFileExists(filePathandName):
    return os.path.exists(filePathandName)
    
if doesFileExists('./Password.txt'):
    PasswordCheck = input("Password: ")
    with open('Password.txt') as f:
        contents = f.read()
    if contents == PasswordCheck:
        print("Password is correct")
        call(["python", "home.py"])
else:
    nme = input("New Password: ")
    file = open('Password.txt', 'w')
    file.write(nme)
    file.close()
    quit()