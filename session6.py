#!/usr/bin/env python
import numpy as np

vals= ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

def lambda_func(vals : 'list of values'= vals,suits :'List containing suits'= suits):
    '''Lambda function for listing down all the cards '''
    return list(map(lambda x : x[0] +'-'+ x[1] ,zip(vals*len(suits), suits*len(vals))))
def card_combination(vals : 'list of values'= vals,suits :'List containing suits'= suits):
    ''' This is a simple function which creates a combination that includes all the cards in a pack from 2 lists
    '''
    list1 = []
    for val in vals :
        for suit in suits:
            list1.append(val + '-' + suit)
    return list1

def convert_card(player_card: 'list'= None) -> 'returns two lists which contains the digits and suit of the card':

    ''' In Poker type game not only the digits are important but also the suits . So it needs to be analyzed in case of a tie.so this
    function separates this out and converts the strings to integer for comarision.

    input  : The cards 
    output : 2 lists . one with the digits after sorted and another with suits 

    '''

    if bool(player_card):
        conversion_dict = {'ace':14,'king':13,'queen':12,'jack':11}
        player_digit_list=[]
        player_suit_list=[]

        for card in player_card:
            if card.split('-')[0] in conversion_dict:
                player_digit_list.append(conversion_dict[card.split('-')[0]])
            else:
                player_digit_list.append(int(card.split('-')[0]))

            player_suit_list.append(card.split('-')[1])

        return player_digit_list, player_suit_list
    else:
        raise ValueError(f' Empty List')

def check_sequence(player_list:'the list of cards ')-> 'returns if the cards in sequence or not': 
    ''' Decides if the cards been given is in sequence or not 
    input : the list of cards 
    output : True - for in sequence , False- Not in sequence 
    Benefit : This helps decides Rank No 1, 2 and 6

    '''
    print("=====", player_list)
    return sorted(player_list) == list(range(min(player_list), max(player_list)+1)) 

def check_for_sequence_rank(player_digit_list: 'the list containing the digits' = None , player_suit_list: 'the list with suits' = None)-> 'returns rank':
    ''' if the Cards are in sequence then this function decides the rank 
    input : List of Card digits and List of card suits 
    output : The rank of the cards . If no rank matches then it sends None 

    '''
    if sorted(player_digit_list,reverse=True)[0] == 14 and len(set(player_suit_list)) ==1:
        return 1
    elif sorted(player_digit_list,reverse=True)[0] == 10 and len(set(player_suit_list)) ==1:
        return 2
    elif len(set(player_suit_list)) == len(player_suit_list)-1 :
        return 6
    else:
        return None 

def check_non_sequence_rank(player_digit_list: 'the list containing the digits' = None, player_suit_list: 'the list with suits' = None)-> 'returns rank':
    ''' if the Cards are not in sequence then this function decides the rank 
    input : List of Card digits and List of card suits 
    output : The rank of the cards . If no rank matches then it sends None 
    Processing : It checks each condition for the list of cards received . It also matches the cards in the high_card dictionary to
    find out if any of the cards are the highest cards in which case it can also assume a rank 
    '''
    high_card = [14,13,12,11]
    count_dict={}

    for element in player_digit_list:
        print("----", element)
        if element in count_dict:
            count_dict[element] +=1
        else:
            count_dict[element] = 1
    # four of a Kind check 
    print(count_dict)
    if  4 in list(count_dict.values()):   # len(count_dict) == 2 and
        return 3
    #full house check
    elif 14 in count_dict and 13 in count_dict and len(count_dict) == 2 and count_dict[14]==3 and count_dict[13]==2:
        return 4
    #flush check
    elif len(count_dict) ==len(player_digit_list) and len(set(player_suit_list)) ==1:
        return 5
    # three of a kind 
    elif 3 in list(count_dict.values()):
        return 7
    #two pairs of cards
    elif sorted(list(count_dict.values()),reverse=True)[0] ==2 and sorted(list(count_dict.values()),reverse=True)[1] ==2:
        return 8
    #one pair 
    elif len(count_dict) ==len(player_digit_list) -1 and sorted(list(count_dict.values()),reverse=True)[0] ==2:
        return 9
    #High Card
    elif sorted(list(count_dict),reverse=True)[0] in high_card and sorted(list(count_dict),reverse=True)[0] in high_card:
        return 10
    else:
        return None 

def suit_rank(player1_suite_list,player2_suite_list)-> 'returns winner':
    ''' This function decides who wins if the ranks are same . This decision is based on the rank of the suits 
    input     : the list of suits for both the players
    output    : The winner based on ranking dictionary
    Exception : Returns tie if the first two also matches.Can we conditioned to check all the cards  
    '''
    suit_rank_dict = {'hearts':1, 'spades':2,'diamonds':3,'clubs':4}
    for i in range(len(player1_suite_list)):
        if suit_rank_dict[player1_suite_list[i]] == suit_rank_dict[player2_suite_list[i]]:
            pass
        elif suit_rank_dict[player1_suite_list[i]] < suit_rank_dict[player2_suite_list[i]]:
            return 'player 1 won'
        elif suit_rank_dict[player1_suite_list[i]] > suit_rank_dict[player2_suite_list[i]]:
            return 'player 2 won'
        else:
            return ' It is a tie based on suit rank which is very much unusual'

def card_game(player1_card : 'list of cards ' = None , player2_card : 'list of cards ' = None,*args,**kwargs )-> 'returns the winner ':

    ''' This is a poker type game in which two players share their set of cards and this game decides who wins based on a certain condition
    input : two set of cards - List
    output : winner

    Ranking Logic :
    =============
    Rank 1  :  -   Sequence of cards starting Ace 
    Rank 2  : -    Sequence of cards starting 10
    Rank 3  :  -   Four cards of same number
    Rank 4  : -    3 Ace and 2 King
    Rank 5  : -    5 Cards of same suit
    Rank 6  : -    5 cards in sequence but different suit
    Rank 7  : -    3 of one kind
    Rank 8  : -    Two pairs 
    Rank 9  : -    One pair 
    Rank 10 : -    Contains at least 2cards from Ace, King, Queen and Jack

    Winning Condition
    =================
    Condition:1 - If both Player1 and Player2 falls under one of the above rank then the player with lowest rank number wins 

    Condition:2 - If one of the players doesn't fall under the above defined rank then he looses 

    Condition:3 - If None of the players fall under the above rank then the sum of the digits decides the winner - The higher the better

    Special Condition : If both attains the same rank then the winner is decided by the following ranking based on suit
        1- Hearts 
        2- Clubs
        3- Diamond
        4- Spead
    If None of the conditions satisfied and still the sum of the digits are same then the Match can be tie  but we are checking till the last digit and last suit, Both return happily after having Draught Beer

    Error Check
    =============

    1. If Both players have unequal number of cards then raise Value Error
    2. If any of the lists are empty then raise ValueError
    3. If any of the card is invalid then raise Value Error


    '''
    valid_cards = ['2-spades', '2-clubs', '2-hearts', '2-diamonds', '3-spades', '3-clubs', '3-hearts', '3-diamonds', '4-spades', '4-clubs', '4-hearts', '4-diamonds', '5-spades', '5-clubs', '5-hearts', '5-diamonds', '6-spades', '6-clubs', '6-hearts', '6-diamonds', '7-spades', '7-clubs', '7-hearts', '7-diamonds', '8-spades', '8-clubs', '8-hearts', '8-diamonds', '9-spades', '9-clubs', '9-hearts', '9-diamonds', '10-spades', '10-clubs', '10-hearts', '10-diamonds', 'jack-spades', 'jack-clubs', 'jack-hearts', 'jack-diamonds', 'queen-spades', 'queen-clubs', 'queen-hearts', 'queen-diamonds', 'king-spades', 'king-clubs', 'king-hearts', 'king-diamonds', 'ace-spades', 'ace-clubs', 'ace-hearts', 'ace-diamonds']
    if not bool(player1_card) or not bool(player2_card):
        raise ValueError(' Either You guys are drunk or one of you wants to run the race alone')
    for play_card in [player1_card, player2_card]:
        for cards in play_card:
            if cards not in valid_cards:
                raise ValueError(f' One of many of the cards not valid - check {cards}')

    rank_player1= None
    rank_player2= None

    player1_card=sorted(np.unique(player1_card),reverse=True) 
    player2_card=sorted(np.unique(player2_card),reverse=True)

    if len(player1_card) != len(player2_card):
        raise ValueError(' Please send equal cards for comparision')
    player1_digit_list, player1_suit_list= convert_card(player1_card)
    player2_digit_list, player2_suit_list= convert_card(player2_card)

    player1_sequence= check_sequence(player1_digit_list)
    player2_sequence= check_sequence(player2_digit_list)

    # Player1 Rank 
    if bool(player1_sequence):
        rank_player1= check_for_sequence_rank(player1_digit_list, player1_suit_list)
    if not bool(rank_player1):
        rank_player1= check_non_sequence_rank(player1_digit_list, player1_suit_list)
    if not bool(rank_player1):
        card_sum_player1 = sum(player1_digit_list)

    # Player2 Rank
    if bool(player2_sequence):
        rank_player2= check_for_sequence_rank(player2_digit_list, player2_suit_list)
    if not bool(rank_player2):
        rank_player2= check_non_sequence_rank(player2_digit_list, player2_suit_list)
    if not bool(rank_player2):
        card_sum_player2 = sum(player2_digit_list)

    # See who won 
    if bool(rank_player1) and bool(rank_player2):
        print(rank_player1, rank_player2)
        if rank_player1 < rank_player2:
            return 'player1 won as his rank number is low'
        elif rank_player1 == rank_player2:
            who_won = suit_rank(player1_suit_list,player2_suit_list)
            return who_won
        else:
            return 'player2 won as his rank number is low'
    elif bool(rank_player1) and not bool(rank_player2):
        return 'player1 won'
    elif bool(rank_player2) and not bool(rank_player1):
        return 'player2 won'
    elif card_sum_player1 > card_sum_player2:
        return 'player1 won'
    elif card_sum_player1 < card_sum_player2:
        return 'player2 won'
    else:
        who_won = suit_rank(player1_suit_list,player2_suit_list)
        #return 'it is a tie as both digits are same '
        return (f'{who_won} - but thats due to last suit comparision- both have a beer each and celebrate')
