# all of the variables will be stored here

attack = 1.00
defense = 1.00
industrial_capacity = 250
divisions = 0
turn = 1
attacking_force = divisions*attack
defending_force = 0
research_points = 1
actions = ["ATTACK", "RESEARCH", "BUILD", "STATS", "TRAIN", "END"]
attackable_factions = ["Poland", "France", "Belgium", "Netherlands", "United Kingdom", "United States", "Nevermind"]
researches = ["Military Equipment", "Garrison Equipment"]
buildings = ["University (250 BP)", "Anti-Air (300 BP)", "Wunderwaffen (500 BP)"]

    

import time

# start of the game

print(f"ACHTUNG!")
start = input("Type 'start'")
if start == "start":
    print(f"December, 1938. You are a person of major authority in the third reich.")
    time.sleep(1)
    print(f"Your decisions will shape the future of the world.")
    time.sleep(1)
    print(f"Good luck, chancellor!")
    time.sleep(0.5)


while turn <=60:
    print(f"TURN {turn}")
    print(f" ACTIONS AVAILABLE: {actions}")
    current_action = input("What do you want to do, chancellor?")
    
    if current_action == "attack":
        print(f"The current attackable factions are {attackable_factions}")
        current_action = input("Who do you wish to attack, chancellor?")

        if current_action == "Poland":
            defending_force = 50
            attacking_force = divisions*attack
            if attacking_force <= defending_force:
                divisions = 0
                print("All of our divisions were obliterated!")
            else:
                divisions = (attacking_force/attack)-(defending_force/attack)
                print("We won!")
                attackable_factions.remove("Poland")
                research_points = research_points+1

        if current_action == "France":
            defending_force = 100
            attacking_force = divisions*attack
            if attacking_force <= defending_force:
                divisions = 0
                print("All of our divisions were obliterated!")
            else:
                divisions = (attacking_force/attack)-(defending_force/attack)
                print("We won!")
                attackable_factions.remove("France")
                research_points = research_points+1

        if current_action == "Belgium":
            defending_force = 10
            attacking_force = divisions*attack
            if attacking_force <= defending_force:
                divisions = 0
                print("All of our divisions were obliterated!")
            else:
                divisions = (attacking_force/attack)-(defending_force/attack)
                print("We won!")
                attackable_factions.remove("Belgium")
                research_points = research_points+1

        if current_action == "Netherlands":
            defending_force = 10
            attacking_force = divisions*attack
            if attacking_force <= defending_force:
                divisions = 0
                print("All of our divisions were obliterated!")
            else:
                divisions = (attacking_force/attack)-(defending_force/attack)
                print("We won!")
                attackable_factions.remove("Netherlands")
                research_points = research_points+1

        if current_action == "United Kingdom":
            defending_force = 400
            attacking_force = divisions*attack
            if attacking_force <= defending_force:
                divisions = 0
                print("All of our divisions were obliterated!")
            else:
                divisions = (attacking_force/attack)-(defending_force/attack)
                print("We won!")
                attackable_factions.remove("United Kingdom")
                research_points = research_points+1

        if current_action == "United States":
            defending_force = 2000
            attacking_force = divisions*attack
            if attacking_force <= defending_force:
                divisions = 0
                print("All of our divisions were obliterated!")
            else:
                divisions = (attacking_force/attack)-(defending_force/attack)
                print("We won!")
                attackable_factions.remove("United States")
                research_points = research_points+1
                turn = turn+70

    if current_action == "research":
        print(f"The current available researches are {researches}")
        current_action = input("What do you wish to research?")
        if current_action == "Military Equipment" and research_points >= 0.5:
            attack = attack+0.25
            research_points = research_points-1
            print(f"Your army has gained more attack")
            
        elif current_action == "Garrison Equipment" and research_points >= 0.5:
            defense = defense+0.25
            research_points = research_points-1
            print(f"Your army has gained more defense")
        else:
            print("Sorry Chancellor, not enough research points")

    if current_action == "build":
        print(f"The current buildings available to build are {buildings}")
        print(f"You have {industrial_capacity} building points left")
        current_action = input("What do you wish to build, chancellor?")

        if current_action == "University" and industrial_capacity >= 249:
            research_points = research_points+1
            print(f"You have increased your research capacity!")
            industrial_capacity = industrial_capacity-250
        elif current_action == "Anti-Air" and industrial_capacity >= 299:
            defense = defense+0.50
            print(f"You have increased your defenses!")
            industrial_capacity = industrial_capacity-300
        elif current_action == "Wunderwaffen" and industrial_capacity >= 499:
            attack = attack+0.50
            print(f"You have created weapons of mass destruction!")
            industrial_capacity = industrial_capacity-500
        else:
            print("You do not have the building points to build this")

    if current_action == "stats":
        print(f" ATTACK = {attack}")
        print(f" DEFENSE = {defense}")
        print(f" RESEARCH POINTS = {research_points}")
        print(f" DIVISIONS = {divisions}")
        

    if current_action == "train":
        print(f"Training a new division costs 100 building points (BP)")
        print(f"You have {industrial_capacity} building points.")
        current_action = input("Do you wish to train a new division?")
        if current_action == "yes" and industrial_capacity >= 99:
            print(f"New unit trained!")
            divisions = divisions+1
            industrial_capacity = industrial_capacity-100
        elif current_action == "yes" and industrial_capacity <= 99:
            print(f"Not enough building points!")
        else:
            print(f"Oh well.")

    if current_action == "end":
        industrial_capacity = industrial_capacity+500
        research_points = research_points+1
        turn = turn+1
        if turn == 30 and defense <= 10:
            divisions = divisions-30
            print("You have lost a battle against the allies.")
            if divisions <= 0:
                turns = turns+90
        elif turn == 30 and defense >= 10:
            print("You have won against an allied attack! Long live Germany!")
            
    
        

if "United States" in attackable_factions:
    print(f"We have lost an honourable battle from the allies, chancellor. GAME OVER.")

else:
    print(f"We have won the war chancellor! Long live germany!")



print(f"Achtung!")

            

    
    





        


                


        


        
                                                



