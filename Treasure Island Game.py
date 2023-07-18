
treasure='''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************'''
print("Welcome to TREASURE ISLAND")
print("Your Mission is to find Treasure")
res=str(input("DO you wanted to go Left or Right? \n"))
if res=='Left' or res=='left':
    res1=str(input("DO you wanted to Swim or Wait?\n"))
    if res1=="'Swim" or res1=='swim':
        print("You are Killed by a Crocodile in Water")
        print("Game Over For You")
    else:
        door=str(input("Select a Door Color: [Red/Blue]\n"))
        if door=='Blue' or door=='blue':
            print("You are teleported to water")
            print("You are Killed by a Crocodile in Water")
            print("Game Over For You")
        else:
            res2=str(input("Do you want any ride? [Horse/Rhino]\n"))
            if res2=='Rhino' or res2=='rhino':
                print("You are Dead")
            else:
                print("You Reached Your Destination")
else:
    res1= str(input("Do you wanted to Ride or Fly?\n"))
    if res1=='Fly' or res1=='fly':
        print("You are Killed by Giant Birds")
        print("You Lose")
    else:
        ride= str(input("What do you wanted to ride? [Rhino/Horse]\n"))
        if ride=='Rhino' or ride=='rhino':
            print("You are Killed by the Rhino")
            print("Game Over For You")
        else:
            print("You have reached Your Destination")
        print(f"Treasure Found\n{treasure}")
