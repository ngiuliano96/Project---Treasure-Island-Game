print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.") 

print("Your journey begins on the beach. You walk into the jungle and find an ancient dirt path. Following the path, you find that it forks to the left or to the right.")
choice = (input("Which direction do you choose?\n")).lower()

if choice == "left" or choice == "l":
  print("As you travel down the leftward path, you find it leads to a raging river. The water is moving very quickly and it doesn't look very safe to swim.")
  choice = (input("Should you wait or swim?\n")).lower()
  
  if choice == "wait" or choice == "w":
    print("You decide to wait. After several minutes a sharp sound cracks the air as a massive bolt of lightning strikes a nearby tree. The tree falls and makes a bridge across the river! You carefully cross the bridge and travel on, only to find a large temple with three colored doors looming in front of you.")
    choice = (input("Which door do you choose: red, blue, or yellow?\n")).lower()
    
    if choice == "yellow" or choice == "y":
      print("You force open the yellow door and travel through a dimly lit, golden-hued hallway. At the end, you find a dazzling treasure room, filled with golden coins and trinkets.")
      print("You win!")
    elif choice == "red" or choice == "r":
      print("You force open the red door and travel down a brightly lit, oddly warm hallway. At the end, you come upon a room. As you enter , the entrance caves in and the room erupts into flames. There is no escape!")
      print("Game over!")
    elif choice == "blue" or choice == "b":
      print("You force open the blue door and travel down a dark, dank hallway. At the end, you come upon a room. As you enter, a solid metal gate blocks the entrance and the room begins to flood with water. There is no escape!")
      print("Game over!") 
    else:
      print("Thinking about the possibility of failure, you get scared and turn around, running back to the beach. Once there, you hop into your boat and sail away, defeated.")
      print("Game over!")
      
  else:
    print("Seeing no other choice, you dive into the river and try to swim, but the current is too strong. The force sweeps you away, into the cold, wet abyss.")
    print("Game over!")
    
else: 
  print("You make your choice and travel on. After several steps, the ground crumbles beneath your feet. You plummet down into a dark hole.")
  print("Game over!")
  
