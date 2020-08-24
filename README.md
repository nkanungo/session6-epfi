
Lamda Function Usage  
======================
The Following function List down all the combinations of a Playing card using lambda function , map and zip 

def lambda_func(vals : 'list of values'= vals,suits :'List containing suits'= suits):

    '''Lambda function for listing down all the cards '''

Normal Function
================

The below function performs the same task without lambda function

def card_combination(vals : 'list of values'= vals,suits :'List containing suits'= suits):
    ''' This is a simple function which creates a combination that includes all the cards in a pack from 2 lists
    

The Poker Type Game 
======================

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

Helper Functions
===================

def convert_card(player_card: 'list'= None) -> 'returns two lists which contains the digits and suit of the card':

    ''' In Poker type game not only the digits are important but also the suits . So it needs to be analyzed in case of a tie.so this
    function separates this out and converts the strings to integer for comarision.

    input  : The cards 
    output : 2 lists . one with the digits after sorted and another with suits 

    '''
def check_sequence(player_list:'the list of cards ')-> 'returns if the cards in sequence or not': 
    ''' Decides if the cards been given is in sequence or not 
    input : the list of cards 
    output : True - for in sequence , False- Not in sequence 
    Benefit : This helps decides Rank No 1, 2 and 6

    '''

def check_for_sequence_rank(player_digit_list: 'the list containing the digits' = None , player_suit_list: 'the list with suits' = None)-> 'returns rank':
    ''' if the Cards are in sequence then this function decides the rank 
    input : List of Card digits and List of card suits 
    output : The rank of the cards . If no rank matches then it sends None 

    '''
def check_non_sequence_rank(player_digit_list: 'the list containing the digits' = None, player_suit_list: 'the list with suits' = None)-> 'returns rank':
    ''' if the Cards are not in sequence then this function decides the rank 
    input : List of Card digits and List of card suits 
    output : The rank of the cards . If no rank matches then it sends None 
    Processing : It checks each condition for the list of cards received . It also matches the cards in the high_card dictionary to
    find out if any of the cards are the highest cards in which case it can also assume a rank 
    '''
def suit_rank(player1_suite_list,player2_suite_list)-> 'returns winner':
    ''' This function decides who wins if the ranks are same . This decision is based on the rank of the suits 
    input     : the list of suits for both the players
    output    : The winner based on ranking dictionary
    Exception : Returns tie if the first two also matches.Can we conditioned to check all the cards  
    '''
#'lambda', #'ValueError', #'map', #'zip', #'for',#'spades',#'hearts',#'clubs',#'diamonds',#'bool'
