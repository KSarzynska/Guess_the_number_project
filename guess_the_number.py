import random
import sys

def welcome_screen():
    print("Welcome to 'What's the number?'!")

def start_screen():
    print("Now, you have to guess the number I am thinking of. You will have three chances.\nOf course, I will give you some hints after every round.\nPlease choose your difficulty:\nEasy\nMedium\nHard")

def choosing_levels():
    dif_level = input()
    if dif_level == "Easy" or dif_level == "easy" or dif_level == "EASY":
        num_easy = random.randint(0, 10)
        print(num_easy)
        guess_easy(num_easy)
    elif dif_level == "Medium" or dif_level == "medium" or dif_level == "MEDIUM":
        num_medium = random.randint(0, 25)
        print(num_medium)
        guess_medium(num_medium)
    elif dif_level == "Hard" or dif_level == "hard" or dif_level == "HARD":
        num_hard = random.randint(0, 50)
        print(num_hard)
        guess_hard(num_hard)
    else:
        error_screen()
        choosing_levels()

def play_again_fun():
    play_again = input("Do you want to play again? (yes/no)\n")
    if play_again == "yes" or play_again == "Yes" or play_again == "YES":
         print("Please, choose the level again:")
         choosing_levels()
    elif play_again == "no" or play_again == "No" or play_again == "NO":
        print("Thank you for playing the game! See you next time :)")
        sys.exit(0)
    else:
        print("Please choose yes/no!")
        play_again_fun()

def error_screen():
    print("Sorry, I don't understand you. Please, choose again:")

def guess_easy(num_easy):
    print("Please, guess a number from 0 to 10.")
    guess1_easy = int(input())
    if guess1_easy == num_easy:
        print("Bravo! You guessed right")
        play_again_fun()
    elif guess1_easy > num_easy:
        print("Sorry, that's not it! It is less than that.")
        guess_easy(num_easy)
    elif guess1_easy < num_easy:
        print("Sorry, that's not it! It is more than that.")
        guess_easy(num_easy)

def guess_medium(num_medium):
   print("Please, guess a number from 0 to 25.")
   guess1_medium = int(input())
   if guess1_medium == num_medium:
       print("Bravo! You guessed right")
       play_again_fun()
   elif guess1_medium > num_medium:
       print("Sorry, that's not it! It is less than that.")
       guess_medium(num_medium)
   elif guess1_medium < num_medium:
       print("Sorry, that's not it! It is more than that.")
       guess_medium(num_medium)

def guess_hard(num_hard):
   print("Please, guess a number from 0 to 50.")
   guess1_hard = int(input())
   if guess1_hard == num_hard:
       print("Bravo! You guessed right")
       play_again_fun()
   elif guess1_hard > num_hard:
       print("Sorry, that's not it! It is less than that.")
       guess_hard(num_hard)
   elif guess1_hard < num_hard:
       print("Sorry, that's not it! It is more than that.")
       guess_hard(num_hard)

#MAIN
welcome_screen()
start_screen()
choosing_levels()

