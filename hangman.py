from random import choice
import time
from colorama import Fore, Back, Style
from random_word import RandomWords

r = RandomWords()
word = r.get_random_word()
print(
    Fore.CYAN,
    """
-----Let's Play a Game!-----
             __              
|__| /\ |\ |/ _`|\/| /\ |\ | 
|  |/~~\| \|\__>|  |/~~\| \|                             
""",
)


def hangman(word):
    print(Fore.RESET, "I've thought of a word!")
    time.sleep(1.4)
    print()
    display = []
    for i in range(len(word)):
        display.append("_")
    print("It contains", len(word), "letters.")
    time.sleep(1.2)
    print()
    play = True
    chances = 8
    wrong_letters = []
    all_guessed_letters = []

    print("You will start with", chances, "lives, good luck!")
    time.sleep(1.7)
    print()
    while play == True:
        guess = input(Fore.YELLOW + "Guess a letter! ").lower()
        if guess == "stop":
            break
        time.sleep(0.5)
        print(Fore.RESET)
        if guess in wrong_letters:
            print(Fore.RED, "You already guessed", guess, "! Try again!")
        elif guess not in word:
            print(Fore.RED, Style.BRIGHT, guess, "is not in the word I'm thinking of.")
            print(Fore.RESET, Style.RESET_ALL)
            chances = chances - 1
            wrong_letters.append(guess)
        index = 0
        for char in word:
            if char == guess:
                display[index] = guess
                if guess in display and not wrong_letters:
                    print(Fore.GREEN, Style.BRIGHT, "You guessed a letter right!")
                # elif guess in display and wrong_letters:
                #     print(
                #         Style.DIM,
                #         Fore.GREEN,
                #         "You already got that one right!",
                #         Style.RESET_ALL,
                #     )
                #     print()
            index = index + 1
        print(Fore.RESET, "".join(display))
        print("Lives:", chances)
        print()
        if "_" not in display:
            print(Fore.WHITE, Back.GREEN, "You win! Nicely done!")
            play = False
        elif chances == 0:
            print(Fore.RED, Back.BLACK, Style.BRIGHT, "You lose!")
            time.sleep(0.5)
            print("The word was", word, "!")
            play = False

        # end_of_game = True
        # while end_of_game:
        #     answer = input(
        #         "If you'd like to play again, enter 'yes', otherwise enter 'no'."
        #     ).lower()
        #     if answer == "yes":
        #         hangman()
        #     elif answer == "no":
        #         end_of_game = False
        #     else:
        #         print("Please answer 'yes' or 'no'.")


hangman(word)
