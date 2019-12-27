import random

# the starting room 
def startingRoom():
    # ask user for their name 
    name = raw_input("What's your name? ")
    # explain the situation 
    print("\nHello, " + name + ". We need to follow Snape to stop him from controlling the school!")
    print("\nWe are in front of a door. Do you?")
    print("1. Open the door \n2. Ignore the door")
    #get user choice 
    choice = raw_input("Enter a number: ")
    # check user choices 
    if choice == '1':
        print('\nYou opened the door.')
        fluffy_room()
    elif choice == '2':
        print('\nYou ignored the door. I\'m sorry, but Hogwarts was lost to Voldemort :(')
        replay()
    else:
        print('\nYou entered an invalid input. We will re-enter the room.')
        print("\n===================")
        startingRoom() 

# the room with fluffy 
def fluffy_room():
    # explain the situation
    print("\n===================")
    print('\nYou entered the room with Fluffy, a three-headed dog in the room.')
    print('Fluffy is growling at you. What do you do?')
    print(" 1. Find and play a flute \n 2. Find and don't play the flute \n 3. Don't find the flute")
    #get user choice 
    choice = raw_input("Enter a number: ")
    # check user choices 
    if choice == '1':
        print('\nGood job! Now you can enter the next room.')
        chess_room()
    elif choice == '2' or choice == '3':
        print('\nSorry, Fluffy hurt you, and now, you\'re in the hospital. :( ')
        replay()
    else:
        print("\nInvalid input! Please try again. We will re-enter the room.")
        fluffy_room()

def chess_room():
    # explain the situation
    print("\n===================")
    print('\nYou have just entered the chess room.')
    print('On a scale of 1 (beginner) to 10 (expert), how well do you BELIEVE you are at playing chess?')
    #get user choice 
    skill_level = raw_input('Enter a number: ')
    # check user choices 
    if skill_level in "10234567891":
        r = random.randint(0,10)
        skill_level = int(skill_level)
        if r <= skill_level:
            print('\nYou won the game against the chess pieces! You enter the next room.')
            final_room()
        else:
            print("\nI'm sorry, but you just lost the game :( ")
            replay()
    else:
        print("\nInvalid input! Please try again. We will re-enter the room.")
        chess_room()

def final_room(): 
    # explain the situation
    print("\n===================")
    print("\nThe Mirror of Erised is in the room.")
    #get user choice 
    view = raw_input('What do you see in the mirror? ').lower()
    # check user choices 
    if view in ["philosopher's stone", "philosophers stone", "philosophersstone", "philosopher", "philosophers", "stone"]:
        print('\nYou see the philosopher\'s stone in the reflection!')
        print('CONGRATULATIONS! You have just beat Voldemort, and won the game!\n')
    else:
        print("I'm sorry, but you have just lost :(")
    replay()
    
def replay():
    #get user choice 
    choice = raw_input('\nDo you want to play again? Enter "y" or "n" (without quotes): ')
    # check user choices 
    if choice == 'y':
        print("\n===================")
        startingRoom()
    elif choice == 'n':
        print("\n===================")
        end_of_game()
    else:
        print("\n===================")
        print('\nPlease enter a valid input')
        replay()
        
def end_of_game():
    print("\nThanks for playing!")

startingRoom()