import random

HANGMAN=("""


_____________
  |                   |
  |
  |
  | 
  |
  |
  |
_|___________

""",
"""
_____________
  |                   |
  |                  O
  |
  | 
  |
  |
  |
_|___________
""",
"""
_____________
  |                   |
  |                  O
  |                  +
  |                   |
  |
  |
  |
_|___________



""",
"""
_____________
  |                   |
  |                  O
  |                  +-\\
  |                   |
  |
  |
  |
_|___________
""",
"""
_____________
  |                   |
  |                  O
  |                /-+-\\
  |                   |
  |
  |
  |
_|___________
""",
"""
_____________
  |                   |
  |                  O
  |                /-+-\\
  |                   |
  |                  /
  |                             
  |
_|___________
""",
"""

_____________
  |                   |
  |                  O
  |                /-+-\\
  |                   |
  |                  / \\
  |                             
  |
_|___________
""")



#Constants
MAX_WRONG = len(HANGMAN) -1
WORDBANK = ("SPAGHETTI" , "MEATBALL", "FLASHDRIVE", "IGUANA",
            "MEGAMIND","BINGO")

word = random.choice(WORDBANK)
soFar ="- " * len(word)

wrong = 0 #Amount of wrong guess
used = [ ] # Already Guessed letters
print("Welcome To Hangman! A Fun Game For Everyone\
Except For The Hanging Man!")

while wrong < MAX_WRONG and soFar != word:

    print(HANGMAN [wrong])
    print("\nYou've used the following letters: \n", used)
    print("\nSo far, the Word is: \n", soFar)

    guess = input("\n\nEnter your guess:   ")
    guess = guess.upper()

    while guess in used:
        print("You already guessed that letter", guess)
        guess = input("\n\nEnter your guess:   ")
        guess = guess.upper()

    used.append(guess)
    if guess in word:
        print("\nYes! ", guess , "Is in the word")
        new = " "
        for i in range(len(word)) :
            if guess == word[i] :
                new += guess
            else:
                new += soFar[i]
        soFar = new
    else:
        print("\nSorry ", guess , "Isn't in the word")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been Hung")
else:
    print("\n You Guessed it!")

print("\n The word was", word)
input("\n\nPress Enter to exit.")




























