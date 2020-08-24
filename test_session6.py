import pytest
import session6
import os
import inspect
import re

README_CONTENT_CHECK_FOR = [
    'lambda',
    'ValueError',
    'map',
    'zip',
    'for',
    'spades',
    'hearts',
    'clubs',
    'diamonds',
    'bool'    
]

CHECK_FOR_THINGS_NOT_ALLOWED = [
    
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 400, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 6

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    line_no =1
    for space in spaces:
        line_no +=1
        print('=====', line_no, space)
        #print(lines)
        #assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        #assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 
        assert re.search('[a-zA-Z#@=1234\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@=1234\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_inconsistent_list_valueerror():
    with pytest.raises(ValueError):
        l1 = ['king-hearts', 'king-clubs','9-diamonds', '8-spades']
        l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
        session6.card_game(l1,l2)

def test_duplicate_value_list_valueerror():
    with pytest.raises(ValueError):
        l1 = ['king-hearts', 'king-clubs','9-diamonds', '8-spades','king-clubs']
        l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
        session6.card_game(l1,l2)

def test_empty_list_valueerror():
    with pytest.raises(ValueError):
        l1 = []
        l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
        session6.card_game(l1,l2)
    with pytest.raises(ValueError):
        l1 = ['king-hearts', 'king-clubs','9-diamonds', '8-spades','king-clubs']
        l2 = []
        session6.card_game(l1,l2)

def test_invalid_value_valueerror():
    with pytest.raises(ValueError):
        l1 = ['1-hearts', 'king-clubs','9-diamonds', '8-spades','king-clubs']
        l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
        session6.card_game(l1,l2)
def test_invalid_suit_valueerror():
    with pytest.raises(ValueError):
        l1 = ['7-hearts', 'king-clubs','9-diamond', '8-spades','king-clubs']
        l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
        session6.card_game(l1,l2)

def test_lambda_func():
    output= session6.lambda_func()
    assert(len(set(output))) == 52, f'Your lambda function is not giving correct result '
def test_lambda_doc_string():
    assert bool(session6.lambda_func.__doc__),f"doc string does not exist"
def test_lambda_annotation():
    assert bool(session6.lambda_func.__annotations__),f"doc string does not exist"

def test_card_combination_func():
    output= session6.card_combination()
    assert(len(set(output))) == 52, f'Your lambda function is not giving correct result '
def test_card_combination_doc_string():
    assert bool(session6.card_combination.__doc__),f"doc string does not exist"
def test_card_combination_annotation():
    assert bool(session6.card_combination.__annotations__),f"doc string does not exist"

def test_rank1_rank2():
    l1 = ['10-spades', '9-spades','8-spades', '7-spades','6-spades']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the ranking"

def test_handle_order():
    l1 = ['10-spades', '9-spades','8-spades', '7-spades','6-spades']
    l2 = ['ace-hearts', 'king-hearts','queen-hearts', 'jack-hearts','10-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the input order"

def test_rank1_rank3():
    l1 = ['queen-spades', 'queen-hearts','queen-clubs', 'queen-diamonds','6-spades']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the ranking"
def test_rank1_rank4():
    l1 = ['ace-spades', 'ace-hearts','ace-clubs', 'king-diamonds','king-spades']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the ranking"

def test_rank1_rank5():
    l1 = ['king-hearts', '8-hearts','6-hearts', '4-hearts','2-hearts']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the ranking"
def test_rank1_rank5_other_case():
    l1 = ['king-hearts', '8-hearts','7-hearts', '4-hearts','2-hearts']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the ranking"

def test_rank1_rank6():
    l1 = ['8-hearts', '7-spades','6-clubs', '5-diamonds','4-hearts']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the ranking"

def test_rank1_rank6_handles_all_combo():
    l1 = ['9-spades', '8-spades','7-clubs', '6-diamonds','5-hearts']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the ranking"

def test_rank1_rank7():
    l1 = ['queen-hearts', 'queen-spades','queen-clubs', '5-diamonds','4-hearts']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the ranking"

def test_rank1_rank8():
    l1 = ['jack-hearts', 'jack-spades','9-clubs', '9-diamonds','4-hearts']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the ranking"
def test_rank1_rank8_work_for_lower_numbers():
    l1 = ['5-hearts', '5-spades','4-clubs', '4-diamonds','3-hearts']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the ranking"

def test_rank1_rank9():
    l1 = ['king-hearts', 'king-spades','4-clubs', '2-diamonds','3-hearts']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the ranking"

def test_rank1_rank10():
    l1 = ['king-hearts', 'queen-spades','4-clubs', '2-diamonds','3-hearts']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the ranking"

def test_rank1_rank10_works_for_other_combination():
    l1 = ['ace-hearts', 'jack-spades','4-clubs', '2-diamonds','3-hearts']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle the ranking"

def test_one_rank_another_nonrank():
    l1 = ['ace-hearts', 'jack-spades','4-clubs', '2-diamonds','3-hearts']
    l2 = ['10-hearts', '2-clubs','3-diamonds', '5-hearts','7-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player1 won'), f"Your program is not able to handle rank and non rank "

def test_both_nonrank():
    l1 = ['10-hearts', '2-clubs','6-diamonds', '5-hearts','7-hearts']
    l2 = ['10-hearts', '2-clubs','3-diamonds', '5-hearts','7-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player1 won'), f"Your program is not able to handle the non ranking"
def test_both_same_rank():
    l1 = ['10-clubs','ace-clubs', 'jack-clubs','queen-clubs', 'king-clubs']
    l2 = ['10-hearts', 'jack-hearts','queen-hearts', 'king-hearts','ace-hearts']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player 2 won'), f"Your program is not able to handle same rank"

def test_both_same_rank_suit_decider():
    l1 = ['10-clubs','8-hearts', '7-spades','5-diamonds', '4-clubs']
    l2 = ['10-hearts','8-hearts', '7-spades','5-diamonds', '4-clubs']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player 2 won - but thats due to last suit comparision- both have a beer each and celebrate'), f"Your program is not able to handle suit"

def test_handles_suit_comparision_till_last():
    l1 = ['10-hearts','8-hearts', '7-spades','5-diamonds', '4-hearts']
    l2 = ['10-hearts','8-hearts', '7-spades','5-diamonds', '4-clubs']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player 1 won - but thats due to last suit comparision- both have a beer each and celebrate'), f"Your program is not able to handle suit"

def test_handles_three_cards():
    l1 = ['ace-hearts','king-hearts', 'queen-hearts']
    l2 = ['ace-spades','queen-spades', 'king-spades']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player 1 won'), f"Your program is not able to handle 3 cards"
def test_handles_three_different_cards():
    l1 = ['10-hearts','9-spades', '6-clubs']
    l2 = ['ace-spades','queen-spades', 'king-spades']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won'), f"Your program is not able to handle 3 different type cards"

def test_handles_four_cards():
    l1 = ['ace-hearts','king-hearts', 'queen-hearts','jack-hearts']
    l2 = ['ace-spades','queen-spades', 'king-spades','jack-spades']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player 1 won'), f"Your program is not able to handle 3 cards"
def test_handles_four_different_cards():
    l1 = ['10-hearts','9-spades', '6-clubs','jack-hearts']
    l2 = ['ace-spades','queen-spades', 'king-spades','jack-spades']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle 3 different type cards"
def test_handles_duplicates():
    l1 = ['10-hearts','9-spades', '6-clubs','jack-hearts','9-spades']
    l2 = ['ace-spades','queen-spades', 'king-spades','jack-spades']
    winner= session6.card_game(l1,l2)
    print(winner)
    assert (winner == 'player2 won as his rank number is low'), f"Your program is not able to handle 3 different type cards"
def test_doc_string():
    assert bool(session6.card_game.__doc__),f"doc string does not exist"
def test_annotation():
    assert bool(session6.card_game.__annotations__),f"doc string does not exist"
   
def test_3_royalflush_straightflush():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts']
    l2= ['10-spades', '9-spades','8-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_royalflush_straightflush_same_suite():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts']
    l2= ['10-hearts', '9-hearts','8-hearts']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
def test_3_royalflush_full_house():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts']
    l2= ['ace-spades', 'king-spades','king-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_royalflush_flush():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts']
    l2= ['10-hearts', '8-hearts','6-hearts']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_royalflush_flush_diff_suite():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts']
    l2= ['king-spades', '10-spades','8-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_royalflush_straight():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts']
    l2= ['8-hearts', '7-spades','6-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won'  , "Player1 should win"

def test_3_royalflush_three_of_a_kind():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts']
    l2= ['queen-hearts', 'queen-spades','queen-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_royalflush_one_pair():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts']
    l2= ['queen-hearts', 'queen-spades','8-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
   
def test_3_royalflush_one_pair_1():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts']
    l2= ['7-spades','8-spades','8-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
    
def test_3_royalflush_high_card():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts']
    l2= ['ace-hearts', '8-spades','9-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_straightflush_full_house():
    l1 = ['10-spades', '9-spades','8-spades']
    l2= ['ace-spades', 'king-spades','king-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_straightflush_flush():
    l1 = ['10-spades', '9-spades','8-spades']
    l2= ['10-hearts', '8-hearts','6-hearts']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
 
def test_3_straightflush_flush_same_suite():
    l1 = ['10-spades', '9-spades','8-spades']
    l2= ['10-spades', '8-spades','6-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
 
def test_3_straightflush_straight():
    l1 = ['10-spades', '9-spades','8-spades']
    l2= ['8-hearts', '7-spades','6-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won' , "Player1 should win"

def test_3_straightflush_three_of_a_kind():
    l1 = ['10-spades', '9-spades','8-spades']
    l2= ['queen-hearts', 'queen-spades','queen-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_straightflush_high_card():
    l1 = ['10-spades', '9-spades','8-spades']
    l2= ['ace-hearts', '8-spades','9-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_full_house_flush():
    l1 = ['ace-spades', 'king-spades','king-clubs']
    l2= ['10-spades', '8-spades','6-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player2 won as his rank number is low' , "Player1 should win"

def test_3_full_house_straight():
    l1 = ['ace-spades', 'king-spades','king-clubs']
    l2= ['8-hearts', '7-spades','6-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won' , "Player1 should win"

def test_3_full_house_three_of_a_kind():
    l1 = ['ace-spades', 'king-spades','king-clubs']
    l2= ['queen-hearts', 'queen-spades','queen-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player2 won as his rank number is low' , "Player1 should win"
    
def test_3_full_house_high_card():
    l1 = ['ace-spades', 'king-spades','king-clubs']
    l2= ['ace-hearts', '8-spades','9-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_flush_straight():
    l1 = ['10-hearts', '8-hearts','6-hearts']
    l2= ['8-hearts', '7-spades','6-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won' , "Player1 should win"

def test_3_flush_three_of_a_kind():
    l1 = ['10-hearts', '8-hearts','6-hearts']
    l2= ['queen-hearts', 'queen-spades','queen-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_flush_one_pair():
    l1 = ['10-hearts', '8-hearts','6-hearts']
    l2= ['queen-hearts', 'queen-spades','8-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_flush_high_card():
    l1 = ['10-hearts', '8-hearts','6-hearts']
    l2= ['ace-hearts', '8-spades','9-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_straight_three_of_a_kind():
    l1 = ['8-hearts', '7-spades','6-diamonds']
    l2= ['5-hearts', '5-spades','5-diamonds']
    print("The print is",session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player2 won' , "Player1 should win"    

def test_3_straight_high_card():
    l1 = ['8-hearts', '7-spades','6-diamonds']
    l2= ['ace-hearts', '8-spades','9-diamonds']
    print("The print is",session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player2 won' , "Player1 should win"    

#def test_3_highcard_high_card():
    #l1 = ['ace-hearts', '8-spades','9-diamonds']
    #l2= ['ace-hearts', '8-spades','9-diamonds']
    #print("The print is",session6.card_game(l1,l2))
    #assert session6.card_game(l1,l2) == ' It is a tie based on suit rank' , "Player1 should win"    

def test_4_royalflush_straightflush():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts']
    l2= ['10-spades', '9-spades','8-spades','7-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
   
def test_4_royalflush_straightflush_same_suite():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts']
    l2= ['10-hearts', '9-hearts','8-hearts','7-hearts']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
 
def test_4_royalflush_full_house():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts']
    l2= ['ace-spades', 'ace-diamonds','king-spades','king-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_4_royalflush_flush():
    l1 = l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts']
    l2= ['10-hearts', '8-hearts','6-hearts','5-hearts']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_4_royalflush_flush_diff_suite():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts']
    l2= ['king-spades', '10-spades','8-spades','6-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
 
def test_4_royalflush_straight():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts']
    l2= ['8-hearts', '7-spades','6-diamonds','5-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won'  , "Player1 should win"

def test_4_royalflush_three_of_a_kind():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts']
    l2= ['queen-clubs', 'queen-spades','queen-diamonds','10-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_4_royalflush_one_pair():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts']
    l2= ['queen-clubs', 'queen-spades','8-diamonds','7-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
 
def test_4_royalflush_two_pair():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts']
    l2= ['queen-clubs', 'queen-spades','8-diamonds','8-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
    
def test_4_royalflush_high_card():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts']
    l2= ['ace-hearts', '8-spades','9-diamonds','7-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
  
def test_4_straightflush_full_house():
    l1 = ['10-spades', '9-spades','8-spades','7-spades']
    l2= ['ace-spades', 'ace-diamonds','king-spades','king-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_4_straightflush_flush():
    l1 = ['10-spades', '9-spades','8-spades','7-spades']
    l2= ['10-hearts', '8-hearts','6-hearts','4-hearts']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
  
def test_4_straightflush_flush_same_suite():
    l1 = ['10-spades', '9-spades','8-spades','7-spades']
    l2= ['ace-spades', '8-spades','6-spades','4-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
  
def test_4_straightflush_straight():
    l1 = ['10-spades', '9-spades','8-spades','7-spades']
    l2= ['8-hearts', '7-clubs','6-diamonds','5-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_4_straightflush_three_of_a_kind():
    l1 = ['10-spades', '9-spades','8-spades','7-spades']
    l2= ['queen-hearts', 'queen-spades','queen-diamonds','5-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
  
def test_4_straightflush_high_card():
    l1 = ['10-spades', '9-spades','8-spades','7-spades']
    l2= ['ace-hearts', '8-spades','9-diamonds','5-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_4_full_house_straight():
    l1 = ['ace-spades', 'ace-diamonds','king-spades','king-clubs']
    l2= ['8-hearts', '7-clubs','6-diamonds','5-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player2 won as his rank number is low' , "Player1 should win"

def test_4_full_house_three_of_a_kind():
    l1 = ['ace-spades','ace-diamonds', 'king-spades','king-clubs']
    l2= ['queen-hearts', 'queen-spades','queen-diamonds','5-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player2 won as his rank number is low' , "Player1 should win"
    
def test_4_full_house_high_card():
    l1 = ['ace-spades', 'ace-diamonds','king-spades','king-clubs']
    l2= ['ace-hearts', '8-spades','9-diamonds','5-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_4_flush_straight():
    l1 = ['10-hearts', '8-hearts','6-hearts','4-hearts']
    l2= ['8-hearts', '7-spades','6-diamonds','5-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won' , "Player1 should win"

def test_3_flush_three_of_a_kind_1():
    l1 = ['10-hearts', '8-hearts','6-hearts','4-hearts']
    l2= ['queen-hearts', 'queen-spades','queen-diamonds','5-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_flush_one_pair_1():
    l1 = ['10-hearts', '8-hearts','6-hearts']
    l2= ['queen-hearts', 'queen-spades','8-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_4_flush_high_card():
    l1 = ['10-hearts', '8-hearts','6-hearts','4-hearts']
    l2= ['ace-hearts', '8-spades','9-diamonds','5-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_4_straight_high_card():
    l1 = ['8-hearts', '7-spades','6-diamonds','5-clubs']
    l2= ['ace-hearts', '8-spades','9-diamonds','2-spades']
    print("The print is",session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player2 won' , "Player1 should win"    
 
def test_5_royalflush_straightflush():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts','10-hearts']
    l2= ['10-spades', '9-spades','8-spades','7-spades','6-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_5_royalflush_straightflush_same_suite():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts','10-hearts']
    l2= ['9-hearts', '8-hearts','7-hearts','6-hearts','5-hearts']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_5_royalflush_full_house():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts','10-hearts']
    l2= ['ace-spades','ace-diamonds','ace-clubs','king-spades','king-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_5_royalflush_flush():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts','10-hearts']
    l2= ['10-hearts', '8-hearts','6-hearts','4-hearts','2-hearts']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_5_royalflush_flush_diff_suite():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts','10-hearts']
    l2= ['king-spades', '10-spades','8-spades','6-spades','4-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_5_royalflush_straight():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts','10-hearts']
    l2= ['8-hearts', '7-spades','6-diamonds','5-clubs','4-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low'  , "Player1 should win"

def test_5_royalflush_three_of_a_kind():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts','10-hearts']
    l2= ['queen-clubs', 'queen-spades','queen-diamonds','4-clubs','2-hearts']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_5_royalflush_one_pair():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts','10-hearts']
    l2= ['queen-clubs', 'queen-spades','8-diamonds','7-clubs','2-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
   
def test_5_royalflush_two_pair():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts','10-hearts']
    l2= ['queen-clubs', 'queen-spades','8-spades','8-diamonds','2-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
    
def test_5_royalflush_high_card():
    l1 = ['ace-hearts', 'king-hearts','queen-hearts','jack-hearts','10-hearts']
    l2= ['ace-hearts', '8-spades','9-diamonds','5-clubs','4-hearts']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_5_straightflush_full_house():
    l1 = ['10-spades', '9-spades','8-spades','7-spades','6-spades']
    l2= ['ace-spades','ace-diamonds','ace-clubs','king-spades','king-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_5_straightflush_flush():
    l1 = ['10-spades', '9-spades','8-spades','7-spades','6-spades']
    l2= ['10-hearts', '8-hearts','6-hearts','4-hearts','2-hearts']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_5_straightflush_flush_same_suite():
    l1 = ['10-spades', '9-spades','8-spades','7-spades','6-spades']
    l2= ['ace-spades', '8-spades','4-spades','3-spades','2-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
 
def test_5_straightflush_straight():
    l1 = ['10-spades', '9-spades','8-spades','7-spades','6-spades']
    l2= ['8-hearts', '7-clubs','6-diamonds','5-clubs','4-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_4_straightflush_three_of_a_kind_1():
    l1 = ['10-spades', '9-spades','8-spades','7-spades']
    l2= ['queen-hearts', 'queen-spades','queen-diamonds','5-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_5_straightflush_high_card():
    l1 = ['10-spades', '9-spades','8-spades','7-spades','6-spades']
    l2= ['ace-hearts', '8-spades','9-diamonds','5-clubs','4-hearts']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"
  
def test_5_full_house_high_card():
    l1 = ['ace-spades','ace-diamonds','ace-clubs','king-spades','king-clubs']
    l2= ['ace-hearts', '8-spades','9-diamonds','5-clubs','4-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_5_flush_straight():
    l1 = ['ace-spades', '8-spades','4-spades','3-spades','2-spades']
    l2= ['8-hearts', '7-spades','6-diamonds','5-clubs','4-spades']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_flush_three_of_a_kind_1():
    l1 = ['10-hearts', '8-hearts','6-hearts','4-hearts']
    l2= ['queen-hearts', 'queen-spades','queen-diamonds','5-clubs']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_3_flush_one_pair_1():
    l1 = ['10-hearts', '8-hearts','6-hearts']
    l2= ['queen-hearts', 'queen-spades','8-diamonds']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_5_flush_high_card():
    l1 = ['ace-spades', '8-spades','4-spades','3-spades','2-spades']
    l2= ['ace-hearts', '8-spades','9-diamonds','5-clubs','4-hearts']
    print(session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win"

def test_5_straight_high_card():
    l1 = ['8-hearts', '7-spades','6-diamonds','5-clubs','4-spades']
    l2= ['ace-hearts', '8-spades','9-diamonds','5-clubs','4-hearts']
    print("The print is",session6.card_game(l1,l2))
    assert session6.card_game(l1,l2) == 'player1 won as his rank number is low' , "Player1 should win" 

def test_things_not_allowed():
    code_lines = inspect.getsource(session6)
    for word in CHECK_FOR_THINGS_NOT_ALLOWED:
        assert word not in code_lines, 'Have you heard of Pinocchio?'
