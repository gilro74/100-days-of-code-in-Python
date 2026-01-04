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
print("Welcome to Treasure Island.\nYour mission is to find treasure.")
print('You\'re at a cross road. Where do you wanna go? ')
print('    Type "left"  or "right"  ')
direction = input().strip().lower()
if direction == "left":
    print("Congragulations! Your game continues!")
    at_the_river = input('You are now at the river, are you going to "swim" or "wait" ?\n').strip().lower()
    if at_the_river == "swim":
        print("Game Over!")
    elif at_the_river == "wait":
        print("Congragulations! Your can continues!")
        door_choice = input('which door do you wanna go with ? "red" or "blue" or "yellow" \n').strip().lower()
        if door_choice =="yellow":
            print("Congragulations!. You finally win. ")
        elif door_choice =="red" or door_choice =="blue":
            print("Game over!")
        else:
            print("you entered an invalid input!")
elif direction =="right":
    print("Game Over!")
else:
    print("Invalid direction.Please type the way it is, left or right")