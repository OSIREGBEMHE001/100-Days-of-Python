print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroads. Where do you want to go?\n"
      "Type LEFT or RIGHT: ").lower()
if choice1 == "left": #continue in game
    choice2 = input("You've come to the lake. There's an island in the middle of the lake. Do you want to swim across or wait for a boat?\n"
          "Type SWIM or WAIT: ").lower()
    if choice2 == "wait":  #game continue
        choice3 = input("A boat came by and you arrived at the island unharmed.\n"
              "There is a house with three doors. One RED, one BLUE and one YELLOW.\n"
              "Which door do you choose? Type 'RED', 'BLUE' or 'YELLOW': ").lower()
        if choice3 == "red":
            print("You fell in to a lava pit. GAME OVER")
        elif choice3 == "yellow":
            print("Congratulations. You found the treasure!")
        elif choice3 == "blue":
            print("You woke a fire breathing dragon. GAME OVER")
        else:
            print("You chose incorrectly, GAME OVER")
    elif choice2 == "swim":
        print("You were eaten by a passing jaguar. GAME OVER")
    else:
        print("You chose wrong! GAME OVER")

else:
    print("You have fallen into a hole. GAME OVER")


