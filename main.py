import random 
import time 
from data import all_kgasons
from kginfo import Kginfo

print("successfully imported")
print("kgamon gotta' put a lanyard on them all!")

#---- SETUP

kgavalues = list(all_kgasons.values())

activepk = random.choice(kgavalues)
active_enemypk = random.choice(kgavalues) # picks pokemon

while activepk == active_enemypk:
    activepk = random.choice(kgavalues) #makes sure same pokemon for both sides isnt chosen

print("Your kgamon is..", activepk.name, "and your facing..", active_enemypk.name)

if activepk.speed > active_enemypk.speed:
        print("Your faster!")
        current_turn = "player" # to actually make it playable
else:
     print(f"\n{active_enemypk.name} is faster! they go first")
     current_turn = "computer"
     
ability_desc = None

while activepk.health > 0 and active_enemypk.health > 0:
        time.sleep(2)
        if current_turn == "player": # first after it determines who is faster lets them go first and then gives the turn
            print("\n----YOUR MOVES ARE----") # display moves
            for move_name, move_damage in activepk.moves.items():
                print(f"- {move_name.title()}: {move_damage} damage")
            print("\n------------------")
            print(f"you have {activepk.health} health remaining ")
            userinput = input("Select an attack..lowercase-->").lower().strip()
            if userinput in activepk.moves:
                    damage_dealt = activepk.moves[userinput] # looks up for the attack
                    actual_damage = activepk.calc_and_dealdamage(active_enemypk, damage_dealt, userinput)
                    print(f"\nyou have used.. {(userinput).upper()} and dealt {actual_damage} damage")
                    print(f"\n{active_enemypk.name} has {max(0, active_enemypk.health)} health remaining")

                    # check if they have died
                    if active_enemypk.health <= 0:
                        print(f"🏆 {active_enemypk.name} fainted! You won!")
                        break
                    current_turn = "computer"
            else:
                 print("nuh uh try again")
                 continue
        elif current_turn == "computer":
            time.sleep(1)
            move_name = random.choice(list(active_enemypk.moves.keys()))
            compdamage_dealt = active_enemypk.moves[move_name]
            # prints out damage etc
            actualcomp_damage = active_enemypk.calc_and_dealdamage(activepk, compdamage_dealt, move_name)
            print(f"\n{active_enemypk.name} has used.. {move_name.upper()}, and dealt.. {actualcomp_damage} damage")
            print(f"\n{activepk.name}, has {max(0, activepk.health)} health remaining")
            
            if activepk.health <= 0:
                print("you lost LMAOO")
                break
            current_turn = "player"


            #current issues are if user is slower still goes first. dont bother, first get to work on multiple pokemon