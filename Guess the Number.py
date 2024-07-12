import random
from datetime import datetime
from pathlib import Path

# Get the current time
current_time = datetime.now().strftime("%H:%M:%S")

# Initialize high score data
highscore = float('inf')
highscore_user = 'N/A'

# Read the high score data
highscore_file = Path('High_score.txt')
if highscore_file.exists():
    text_data = highscore_file.read_text().split()
    if text_data:
        highscore, highscore_user = int(text_data[0]), text_data[2]

# Display welcome message and current high score
print(f'''Welcome to Guess the Number Game.
You are Challenged to Guess a Number b/w [0,100] and beat the Highscore of Previous User.
When you enter a input, the compiler will be giving you tips in the following way:
Too Far - The hidden number is more than 10 numbers away
Almost There - The Hidden Number is less than or equal to 10 numbers away
You are moving Far Away - You are moving in the wrong direction.
You are getting Closer - You are moving in the correct direction.
Current Highscore = {highscore} by {highscore_user}''')

# Get user's name
user_name = input('Enter your Name: ').title()

# Generate random number
hidden_number = random.randint(0, 100)

# Initialize game variables
prev_input = int(input('Enter a Number b/w [0,100]: '))
my_score = 1

# Main game loop
while (player_input := int(input('Enter a New Number: '))) != hidden_number:
    difference = abs(hidden_number - player_input)
    prev_difference = abs(hidden_number - prev_input)
    
    print('You are getting Closer' if difference < prev_difference else 'You are moving Far Away')
    if my_score == 1:
        print('Too Far' if difference > 10 else 'Almost There')
    
    prev_input = player_input
    my_score += 1

# Player guessed the number
print(f'You have Guessed the Number in {my_score} turns')

# Update high score if necessary
if my_score < highscore:
    print(f'Congratulations.....\nYou have beaten the previous Highscore by {highscore - my_score} turns.')
    highscore_file.write_text(f'{my_score} by {user_name}')
elif my_score == highscore:
    print('Congratulations....\nYou have same score as the Highscore user.')
    highscore_file.write_text(highscore_file.read_text() + f'\n{my_score} by {user_name}')
else:
    print(f'You lost to previous high score by {my_score - highscore} turns.\nBut you have tried your best.')

# Log the game history
with open('History.txt', 'a') as history_file:
    history_file.write(f'{user_name} ---> {my_score} at {current_time}\n')

print('Thank You for trying this Game')
