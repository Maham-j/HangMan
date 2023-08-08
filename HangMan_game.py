from random import*                                          # Importing required modules
from IPython.display import clear_output

HANGMANPICS = ['''                                          # Defining ASCII art for Hangman stages
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

logo = '''                      # ASCII art for the game logo
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                     '''




print(logo)
lives = 7                #Initializing variables          
display = []
words = [
    # Animation Movies
    'frozen',
    'moana',
    'zootopia',
    'coco',
    'toystory',
    'finding nemo',
    'shrek',
    'thelionking',
    'aladdin',
    'cars',
    'mulan',
    'insideout',
    'ratatouille',
    'theincredibles',
    'kungfupanda',
    'despicable me',
    'madagascar',
    'brave',
    'pussinboots',
    
    # Fruits
    'apple',
    'banana',
    'orange',
    'grape',
    'watermelon',
    'strawberry',
    'pineapple',
    'mango',
    'cherry',
    'blueberry',
    'kiwi',
    'lemon',
    'papaya',
    'apricot',
    'pear',
    'peach',
    'plum',
    'raspberry',
    'blackberry',
    'guava',
    'cantaloupe',
    'cranberry',
    'fig',
    'date',
    'nectarine',
    'lime',
    'coconut',
    'passionfruit',
    'dragonfruit',
    'lychee',
    'pomegranate',
    'kiwifruit',
    'apricot',
    'pomelo',

    # Vegetables
    'carrot',
    'potato',
    'broccoli',
    'cucumber',
    'onion',
    'pepper',
    'tomato',
    'lettuce',
    'pumpkin',
    'cabbage',
    'cauliflower',
    'eggplant',
    'zucchini',
    'radish',
    'beetroot',
    'celery',
    'asparagus',
    'spinach',
    'artichoke',
    'sweet potato',

    # Others
    'elephant',
    'giraffe',
    'penguin',
    'koala',
    'dolphin',
    'butterfly',
    'rainbow',
    'bicycle',
    'guitar',
    'umbrella',
    'pizza',
    'chocolate',
    'sandwich',
    'umbrella',
    'suitcase',
    'television',
    'clock',
    'computer',
    'sunglasses',
    'moon',
    'raindrop',
    'starfish',
    'whale'
]


rangee = randint(0,10)                      # Selecting a random word
chosen_word = words[rangee]
for _ in range (len(chosen_word)):
    display.append('_')
print(display)                              #Displaying initial status

while '_' in display and  lives > 0:            # Main game loop
    guess = input('Guess a word: ').lower()
    clear_output(wait=True)
    
    for  letter in range(len(chosen_word)):      # Checking if the guessed letter is in the word
        if chosen_word[letter] == guess:
            display[letter] = guess        
    print(display)
    
        
    if guess not in chosen_word:                  # Handling incorrect guesses
        lives -= 1
        print(HANGMANPICS[6-lives])
    print('lives Left:',lives)
    
if not '_' in display :                        # Displaying game result
    print('You Won')
else:
    print(f'You Lose.The word was {chosen_word}')
    
    
    
    
