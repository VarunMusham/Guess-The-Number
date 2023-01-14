from random import randint
from datetime import datetime
now=datetime.now()
current_time=now.strftime("%H:%M:%S")
with open('High_score.txt','r') as myfile:
    text_data=(myfile.read())
    text_data=text_data.split()
    highscore=text_data[0]
    highscore_user=text_data[2]
    myfile.close()
print(f'''Welcome to Guess the Number Game.
You are Challenged to Guess a Number b/w [0,100] and beat the Highscore of Previous User.
When you enter a input, the compiler will be giving you tips in the following way:
Too Far - The hidden number is more than 10 numbers away
Almost There - The Hidden Number is less than or equal to 10 numbers away
You are moving Far Away - You are moving in the wrong direction.
You are getting Closer - You are moving in the correct direction.
Current Highscore = {highscore} by {highscore_user}''')
user_name=input('Enter your Name:  ').title()
x=randint(0,101)
player_input=int(input('Enter a Number b/w [0,100]:  '))
prev_input=player_input
my_score=1
while player_input!=x:
    if (x-player_input<x-prev_input and x-player_input>0) or (player_input-x<prev_input-x and x-player_input<0):
        print('You are getting Closer')
    if (x-player_input>x-prev_input and x-player_input>0) or (player_input-x>prev_input-x and x-player_input<0):
        print('You are moving Far Away')
    if ((x-player_input>10 and x- player_input>0) or (x-player_input<-10 and x- player_input<0)) and my_score==1:
        print('Too Far')
    if ((x-player_input<=10 and x-player_input>0) or (x-player_input>=-10 and x-player_input<0)) and my_score==1:
        print('Almost There')
    prev_input=player_input
    my_score+=1
    player_input=int(input('Enter a New Number:  '))
if player_input==x:
    print(f'You have Guessed the Number in {my_score} turns')
    if int(highscore)>my_score:
        print(f'''Congratulations.....
You have beaten the previous Highscore by {int(highscore)-my_score} turns.''')
        with open('High_score.txt','w') as myfile:
            myfile.write(f'{str(my_score)} by {user_name}')
            myfile.close()
    elif int(highscore)==my_score:
        print('''Congratulations....
You have same score as the Highscore user.''')
        with open('High_score.txt','a') as myfile:
            myfile.write(f'\n{str(my_score)} by {user_name}')
            myfile.close()
    else:
        print(f'''You lost to previous high score by {my_score-int(highscore)} turns.
But you have tried your best.''')

with open('History.txt','a') as myfile:
    myfile.write(f'{user_name} ---> {my_score} at {current_time}\n')
    myfile.close()
print('Thank You for trying this Game')