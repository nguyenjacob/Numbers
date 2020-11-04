import time

time.sleep(0.5)

def Easy():
    print("You have selected Easy Mode!")
    time.sleep(3)
    print("You have 7 chances to guess the number I'm thinking of from 1-15")
    time.sleep(3)
    import easymode

def Hard():
    print("You have selected Hard Mode!")
    time.sleep(3)
    print("You have 5 chances to guess the number I'm thinking of from 1-30")
    time.sleep(3)
    import hardmode

def menusys():
    print("Guess that Number!")
    time.sleep(1)
    print("0. Easy \n1. Hard")

    menunumchosen = input("What do you want to do?\n")
    userChoice = menu[int(menunumchosen)]
    userChoice()

menu = {0 : Easy, 1 : Hard}

menusys()