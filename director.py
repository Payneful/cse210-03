from msvcrt import kbhit
from parachute import Parachute
from terminal_service import Terminal_Service
from word import Word
import json

def get_words():
    '''get filename as list'''
    with open("words.json") as w:
        words = json.load(w)
        
    return words["words"]
    
def game(user):
    '''Function to run game'''
    word = Word(get_words())
    parachute = Parachute()
    word.setup_word()
    
    while "_" in word.stitched_word:
        user.output(word.stitched_word)
        parachute.create_stickman()
        user.output("^^^^^^^^")
        print(word._word)
        if parachute.get_mistakes() < 4:
            if not word.check_guessed_list():
                user.single_letter_input()
                word.update_word(user.user_letter)
                if not word._letter_in_word:
                    parachute.add_mistake()
        else:
            return
          
    user.output("Congrats\n")
    play_again(user)
     
def play_again(user):
    choices = ["y","n"]
    if user.user_letter == "n":
        user.user_letter == ""
    
    while user.user_letter not in choices:
        user.single_letter_input("Play again? (y/n) ")
        
    if user.user_letter == "y":
        return True

    return False

def main():
    user = Terminal_Service()
    
    game(user)
    
    while play_again(user):
        game(user)

if __name__ == "__main__":
    main()