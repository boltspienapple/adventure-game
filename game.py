import time
import random

def print_message(message):
    print(message)
    #time.sleep(2)

choices = random.choice(["dragon", "Fly", "troll","ghost"])
item = []
def intro():
    print_message("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_message("Rumor has it that a " + choices + "    is somewhere around here, and has been terrifying the nearby village.")
    print_message("To your right is a dark cave.")
    print_message("In your hand you hold your trusty (but not very effective) dagger.")
    again()

def again():
    print_message("Enter 1 to knock on the door of the house.")
    print_message("Enter 2 to peer into the cave.")
    print_message("What would you like to do?")
    game()

def game():
    response = input("please say 1 or 2\n")
    while True:
        if response == "1":
            print_message("You approach the door of the house.")
            print_message("You are about to knock when the door opens and out steps a " + choices +".")
            print_message("Eep! This is the " +choices +"'s house!")
            print_message("The " +choices+" attacks you!")
            print_message("You feel a bit under-prepared for this, what with only having a tiny dagger.")
            respond = input("Would you like to (1) fight or (2) run away?\n")

            if respond == "1":
                print_message(" You do your best...")
                print_message("but your dagger is no match for the "+ choices +".")
                print_message("You have been defeated!")
                option = input("Would you like to play again? (y/n)")
                if option == "y":
                    print_message("Excellent! Restarting the game ...")
                    intro()
                elif option =="n":
                    print_message("You run back into the field. Luckily, you don't seem to have been followed.")
                    again()
            break
        elif response == "2":
            if "sword" in item:
                print_message("You were already here")
                print_message("There is nothing to loot") 
                print_message("you walk back to the field")
            else:
                print_message("You peer cautiously into the cave.")
                print_message("It turns out to be only a very small cave.")
                print_message("Your eye catches a glint of metal behind a rock.")
                print_message("You have found the magical Sword of Ogoroth!")
                print_message("You discard your silly old dagger and take the sword with you.")
                print_message("You walk back out to the field.")
                item.append("sword")
            again()

            





            break
        else:
            print("sorry i don't understand")
            break

intro()
