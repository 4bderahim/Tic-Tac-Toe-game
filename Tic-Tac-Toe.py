#ITNOG
import os
import random
import time
x = "X"
o= "O"
_n = "123456789"
wincheck = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['7', '4', '1'],
    ['8', '5', '2'],
    ['9', '6', '3'],
    ['7', '5', '3'],
    ['1', '5', '9']]
game_map = '\n\t\t      |     |\n\t\t    1 |  2  | 3\n\t\t  ----|-----|----\n\t\t    4 |  5  | 6\n\t\t  ----|-----|----\n\t\t    7 |  8  | 9\n\t\t      |     |\n'
NOONEWINS = [False, "\n\t\t\tNO ONE WINS !!!\n\n"]
dicc = {}
available_numbers = list(_n)

def winermap(THE_WINNER):
    global game_map
    THE_LOSER = o if THE_WINNER == x else x
    for i in game_map:
        if i==THE_WINNER:
            pass
        else:
            if i.isdecimal() or i == THE_LOSER:
                game_map = game_map.replace(i, " ")
            
def win(player):
    for play in wincheck:
        if len(dicc)==9:
            NOONEWINS[0] = True
        if dicc.get(play[0]) == dicc.get(play[1]) == dicc.get(play[2]) ==player:
            winermap(dicc.get(play[0]).upper())
            return True
def input_(pn):
    if pn=="AI":
        inpp = random.choice(available_numbers) 
        time.sleep(0.5)
        print(f"Player O > {inpp}")
        time.sleep(0.5)
    else:
        inpp = input(f"Player {pn} > ")
    if inpp not in _n or inpp in dicc or len(inpp) > 1 or str(inpp).isalnum() != True:
        return input_(pn)
    available_numbers.pop(available_numbers.index(str(inpp)))
    return inpp 
def playerinput(ent):
    if ent=="x":
        return input_("X")
    elif ent == "y":
        return input_("AI")
    return input_("O")

def gdf(ptype):
    global game_map
    dicc[ptype[0]] = ptype[1]
    game_map = game_map.replace(ptype[0],ptype[1].upper())

Game = True
def to_start():
    rules = input("Play against a 'blind' COMPUTER? Yes , No  Y/N :")
    if rules.capitalize() =="Y":
        print("\n\n\tYOU : X\n\tTHE BLIND COMPUTER : O\n")
        return "y"
    elif rules.capitalize()=="N":
        return "o"
    else:
        print("[!] Choose Y or N ")
        to_start()
_start = to_start()
def launch():
    while Game:
        print(game_map)
        gdf([playerinput("x"),"x"])
        if win("x") == True:
            print(f"\n\n\t\t {x} wins\t:)\n\n{game_map}")
            break
        print(game_map)
        if NOONEWINS[0]:
            print(NOONEWINS[1])
            break
        gdf([playerinput(_start),"o"])
        if win("o") == True:
            print(f"\n\n\t\t {o} wins\t:)\n\n{game_map}")
            break
if __name__ == '__main__':
    launch()   
input("\n\n\n PRESS ENTER TO EXIT..")
