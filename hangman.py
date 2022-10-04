from random import choice

print(
    """
----------Let's Play a Game!----------
   _    _    _    _    _    _    _  
  / \  / \  / \  / \  / \  / \  / \ 
 ( H )( a )( n )( g )( m )( a )( n )
  \_/  \_/  \_/  \_/  \_/  \_/  \_/ 

"""
)

word_list = [
    "tree",
    "tower",
    "bubble",
    "fortress",
    "ivory",
    "images",
    "park",
    "marriage",
    "clone",
    "shake",
]
word = choice(word_list)

print("Here's your word!")
for i in word:
    print("_", end=" ")

play = True
chances = len(word) + 2
correct_guesses = 0
flag = 0

def hangman(word):
    # while play == True chances != 0

    # break
