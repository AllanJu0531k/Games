import random
hand = ['Rock','Paper','Scissors']
player = False
comp_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
    computer = random.choice(hand)

    if player == computer:
        print('TIE')
    elif player == 'Rock':
        if computer == 'Paper':
            print('lost',computer,'covers',player)
            comp_score+=1
        else:
            print('won',player,'smashes',computer)
            player_score+=1
    elif player == 'Scissors':
        if computer == 'Rock':
            print('lost',computer,'smashes',player)
            comp_score+=1
        else:
            print('won',player,'cuts',computer)
            player_score+=1
    elif player == 'Paper':
        if computer == 'Scissors':
            print('lost',computer,'cuts',player)
            comp_score+=1
        else:
            print('won',player,'covers',computer)
            player_score+=1
    elif player == 'End':
        print('game over')
        print('computer score is {0}'.format(comp_score))
        print('player score is {0}'.format(player_score))
        if comp_score>player_score:
            print('Computer won')
        elif player_score>comp_score:
            print('Player won')
        else:
            print('TIE')
        break
