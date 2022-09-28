import random

my_list=['bag','rush','comb','wattch']

rand=random.choice(my_list)

# print(rand)  # checking

word_length=len(rand)

live=5

display=[]

for obj in rand:
    display.append('_')

print(f'The word is {word_length} letters long')

game_on=True
while game_on:

    guess=input(f'make your guess : ').lower()

    if guess in display:
        print('already guessed')


    if guess not in rand:
        live-=1
        print(f'you guessed wrong you have {live} lives left')

        if live==0:
            print('GAME OVER')
            print(f'The word was {rand}')
            game_on=False

    
    for pos in range(0,word_length):

        letter=rand[pos]
        if letter==guess:
            print('you guessed right')
            display[pos]=letter
            
    


    word=''
    for char in display:
        word+=char

    print(word)
    
    if word==rand:
        print('YOU WIN')
        print(f'The word was {rand} ')
        game_on=False
            


        
       
        



    #print(letter)

    
   
    # letter=guess[pos]
    # if letter == rand:
    #     print('okay')

# else:
    
#     pass

    
