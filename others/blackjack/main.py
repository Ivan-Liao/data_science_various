# Dependancies
import random
from Player import Player
from Deck import Deck
from Card import Card
from IPython.display import clear_output

def print_game_state(h1,h2):
    clear_output()
    print('computer        \n')
    
    l1,l2,l3,l4,l5,l6 = '  ','  ','  ','  ','  ','  '
    for i in range(len(h1)):
        if (computer.turn_bool == False) and (i == 1):
            card_string = '?'
            comp_value = deck.dict_blackjack_values[computer.list_hand[0].rank]
        else:
            card_string = h1[i].rank + h1[i].suit
            comp_value = computer.hand_value()
        l1 += ('    --------   ')
        l2 += ('    |      |   ')
        l3 += (f'    |  {(card_string):3} |   ')
        l4 += ('    |      |   ')
        l5 += ('    --------   ')
        l6 += ('               ')
    print(l1 + '\n' + l2 + '\n' + l3 + '\n' + l4 + '\n' + l5 + '\n' + l6 + '    ' + str(comp_value) + '\n')
    
    l1,l2,l3,l4,l5,l6 = '  ','  ','  ','  ','  ','  '
    for i in range(len(h2)):
        l1 += ('    --------   ')
        l2 += ('    |      |   ')
        l3 += (f'    |  {(h2[i].rank + h2[i].suit):3} |   ')
        l4 += ('    |      |   ')
        l5 += ('    --------   ')
        l6 += ('               ')
    print(l1 + '\n' + l2 + '\n' + l3 + '\n' + l4 + '\n' + l5 + '\n' + l6 + '    ' + str(player.hand_value()))
    print('player         \n')
    
def replay():
    replay = input("Would you like to play another game? Enter 'y' for yes.")
    replay.lower()
    return replay == 'y'
    
if __name__ == '__main__':

    player_name = input('What is your name? ')

    while True:
        try:
            player_balance = int(input('How much money did you bring to the table? '))
            if player_balance > 0:
                break
            else:
                print("You don't have enough money.")
        except:
            print('Please enter a valid integer.')

    player = Player(player_name,player_balance)
    computer = Player('computer', 100000000000)
    deck = Deck()
    
    while True:
        player_bust_bool = False
        deck.shuffle()
        player.list_hand, computer.list_hand = deck.deal_start(computer.list_hand, player.list_hand)
        player.turn_bool == True
        bet = player.pick_bet()
        print_game_state(computer.list_hand, player.list_hand)
        
        while player.stand_or_hit() == 'h':
            player.list_hand += [deck.draw()]
            print_game_state(computer.list_hand, player.list_hand)
            if player.check_bust():
                print("Bust! You've gone over 21.")
                player.stats['games_played'] += 1
                player.stats['losses'] += 1
                player.stats['earnings'] -= bet
                player.balance -= bet
                player_bust_bool = True
                print(player)
                break
        
        player.turn_bool = False
        if player_bust_bool:
            replay_bool = replay()
            if not replay_bool:
                break
            else:
                continue
            
        computer.turn_bool = True
        
        while True:
            if (computer.hand_value() < 17):
                computer.list_hand += [deck.draw()]
                print_game_state(computer.list_hand,player.list_hand)
            elif (computer.hand_value() < player.hand_value()):
                computer.list_hand += [deck.draw()]
                print_game_state(computer.list_hand,player.list_hand)
            else:
                print_game_state(computer.list_hand, player.list_hand)
                if computer.check_bust():
                    print('Computer Busted! Congrats you won! ^_^')
                    player.stats['games_played'] += 1
                    player.stats['wins'] += 1
                    player.stats['earnings'] += bet
                    player.balance += bet
                    break
                elif computer.hand_value() == player.hand_value():
                    print("It's a draw.")
                    player.stats['games_played'] += 1
                    player.stats['draws'] += 1
                    break
                else:
                    print('Computer has won. @_@')
                    player.stats['games_played'] += 1
                    player.stats['losses'] += 1
                    player.stats['earnings'] -= bet
                    player.balance -= bet
                    break
        
        computer.turn_bool = False
        print(player)

        replay_bool = replay()
        if not replay_bool:
            break