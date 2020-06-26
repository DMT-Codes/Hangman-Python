import random
print('Enter your name')
name=input()
print("Welcome to Jamarri White's hangman game, " + name)


words_dict = {1:"chaos",
           2:"period",
           3:"trend",
           4:"farm",
           5:"brick",
           6:"dictionary",
           7:"fishhook",
           8:"sophomore",
           9:"hyphen",
           10:"quip",
           11:"quad",
           12:"howard",
           13:"bison",
           14:"freshman",
           15:"legacy",
           16:"important",
           17:"rogue",
           18:"sphinx",
           19:"today",
           20:"birth"
}

hangman_body = ["""
              _______
              |     |
              |     
              |    
              |    
              |
             _|_______""",
            """\
              _______
              |     |
              |     O
              |    
              |    
              |
             _|_______""",
            """\
              _______
              |     |
              |     O
              |     |
              |    
              |
             _|_______""",
            """\
              _______
              |     |
              |     O
              |    /|
              |    
              |
             _|_______""",
            """\
              _______
              |     |
              |     O
              |    /|\ 
              |    
              |
             _|_______""",
            """\
              _______
              |     |
              |     O
              |    /|\ 
              |    / 
              |
             _|_______""",
            """\
              _______
              |     |
              |     O
              |    /|\ 
              |    / \  
              |
             _|_______
            """
]


def display_game(hangman_body, missed_letter, correct_letters, secret_word):
  print(hangman_body[(len(missed_letter)- 1)])
  blank_spaces = ("_" * (len(secret_word)))

  for i in range(len(secret_word)):
    if secret_word[i] in correct_letters:
      blank_spaces = blank_spaces[:i] + secret_word[i] + blank_spaces[i+1:]
  
  for letter in blank_spaces:
    print(letter, end=" ")
pass

def get_guess(letters_guessed):

  while True:
    print("\nYou have",attempts,"wrong chances remaining")
    print("\nLetters previously used:",(correct_letters + missed_letters))
    user_guess = input("\nGuess a letter: ")
    if len(user_guess) > 1:
      print("Please enter 1 letter at a time please.")
    elif (user_guess.isalpha() == False):
      print("Please enter a letter between A-Z.")
    elif user_guess in letters_guessed:
      print(" You have already tried that letter")
    else: 
      return user_guess
pass

def welcome_screen():
   return ("A random word is going to appear and you will be required to try and figure it out. You can guess one letter at a time and  you have 6 incorrect guesses after which the hangman body will be built and you will recieve a game over. GOOD LUCK!")
pass

def play_game():
  print(welcome_screen())
  global attempts, correct_letters, missed_letters
  missed_letters = " "
  correct_letters = " "
  secret_word = words_dict[random.randint(1, (len(words_dict)))]
  attempts = (len(hangman_body)-1)
  
  while (attempts > 0):
    display_game(hangman_body, missed_letters, correct_letters, secret_word)

    user_guess = get_guess((missed_letters + correct_letters))

    if user_guess in secret_word:
      correct_letters = correct_letters + user_guess

      found_all = True
      for i in range(len(secret_word)):
         if secret_word[i] not in correct_letters:
           found_all = False
           break
    
      if found_all:
        print("The word was",secret_word,"! You WON!!!!")
        print("Do you want to play again?")
        reply = input("Yes or No? ").lower()
        if (reply == "yes"):
          print(play_game())
        else: 
          return("Thanks for playing!!")
    else:
      missed_letters += user_guess
      attempts -= 1
  display_game(hangman_body, missed_letters, correct_letters, secret_word)
  print("\nYou ran out of attempts")
  print("The word was",secret_word,)
  print("Do you want to play again?")
  reply = input("Yes or No? ").lower()
  if (reply == "yes"):
    print(play_game())
  else:
    return("Thanks for playing!!")
pass

print(play_game())