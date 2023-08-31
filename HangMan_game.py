# Importing required modules
from random import*                                          
from IPython.display import clear_output
from game_data.py import words
from game_images.py import HANGMANPICS, logo

print(logo)

#Initializing variables   
lives = 7                       
display = []


# Selecting a random word
rangee = randint(0,10)                      
chosen_word = words[rangee]
for _ in range (len(chosen_word)):
    display.append('_')

#Displaying initial status
print(display)                              


 # Main game loop
while '_' in display and  lives > 0:           
    guess = input('Guess a word: ').lower()
    clear_output(wait=True)

     # Checking if the guessed letter is in the word
    for  letter in range(len(chosen_word)):     
        if chosen_word[letter] == guess:
            display[letter] = guess        
    print(display)
    
     # Handling incorrect guesses    
    if guess not in chosen_word:                 
        lives -= 1
        print(HANGMANPICS[6-lives])
    print('lives Left:',lives)

  # Displaying game result
if not '_' in display :                      
    print('You Won')
else:
    print(f'You Lose.The word was {chosen_word}')
    
    
    
    
