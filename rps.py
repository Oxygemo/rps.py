import random
import os
import sys
#What text editor you using? I use VSCode

print("Rock, paper, scissors! \n Choose your gesture: \n 1. Rock \n 2. Paper \n 3. Scissors.")
human = input("Input:")

if human == "1":
    choicelist = ['1','2','3']
    computer = random.choice(choicelist)
    if computer == '1':
        print ("Oh god... A tie! Try again.")
        input("Try again.")
        os.system("start rps.py")
        sys.exit()
    if computer == '2':
        print ("Computer took paper. You lost!")
        input("Play again!")
        os.system("start rps.py")
        sys.exit()
    if computer == '3':
        print ("Computer took scissors. You won!")
        input("Play again!")
        os.system("start rps.py")
        sys.exit()
if human == "2":
    choicelist = ['1','2','3']
    computer = random.choice(choicelist)
    if computer == '2':
        print ("Oh god... A tie! Try again.")
        input("Try again.")
        os.system("start rps.py") 
        sys.exit()
    if computer == '1':
        print ("Computer took rock. You won!")
        input("Play again!")
        os.system("start rps.py")
        sys.exit()
    if computer == '3':
        print ("Computer took scissors. You lost!")
        input("Play again!")
        os.system("start rps.py")
        sys.exit()
if human == "3":
    choicelist = ['1','2','3']
    computer = random.choice(choicelist)
    if computer == '3':
        print ("Oh god... A tie! Try again.")
        input("Try again.")
        os.system("start rps.py")
        sys.exit()
    if computer == '1':
        print ("Computer took rock. You lost!")
        input("Play again!")
        os.system("start rps.py")
        sys.exit()
    if computer == '2':
        print ("Computer took paper. You won!")
        input("Play again!")
        os.system("start rps.py")
        sys.exit()

    
