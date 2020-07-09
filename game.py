import time

def print_message(message):
    print(message)
    #time.sleep(2)

print_message("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
print_message("Rumor has it that a gorgon is somewhere around here, and has been terrifying the nearby village.")
print_message("In front of you is a house.")
print_message("To your right is a dark cave.")
print_message("In your hand you hold your trusty (but not very effective) dagger.")
print_message("Enter 1 to knock on the door of the house.")
print_message("Enter 2 to peer into the cave.")
print_message("What would you like to do?")


response = input("please say\n"
                "1" "or" "2\n")
while True:
    if response == "1":
        print("you are e")
        break
    elif response == "2":
        print("here")
        break
    else:
        print("sorry i don't understand")
        break

