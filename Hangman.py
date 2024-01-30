import random
import os


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game= False
word_list=["bhopal","gwalior","ujjain","indore","sehore"]

 
chosen_word=random.choice(word_list)
# print(chosen_word)

lives= 6

# creating blanks
display=[]

for i in range(len(chosen_word)):
    display+="_"


while not end_of_game:
    guess=input("Guess a letter: ").lower()
    os.system('cls')

    if guess in display:
        print ("You have already guessed that letter")

        # check guessed letter
    for position in range (len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter

            # check if user is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
        if lives==0:
            end_of_game=True
            print ("Sorry! You Lose.")
      


    print(f"{' ' .join(display)}")
    if "_" not in display:
        end_of_game=True
        print("Congratulations, you won!")

    print(stages[lives])
