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
            user.single_letter_input()
            if not word.check_guessed_list(user.user_letter):
                word.update_word(user.user_letter)
                if not word._letter_in_word:
                    parachute.add_mistake()
        else:
            user.output(word.stitched_word)
            parachute.create_stickman()
            user.output("^^^^^^^^")
            user.output(f"Better luck next time!\nWord was: {word._word}")
            return
        
    user.output(word.stitched_word)
    parachute.create_stickman()
    user.output("^^^^^^^^")
    user.output("Congrats!\n")

def main():
    user = Terminal_Service()
    play = ["y","n"]
    play_again = "y"

    while play_again == "y":
        game(user)
        play_again = input("Play again? (y/n) ").lower()
        while play_again not in play:
            play_again = input("Play again? (y/n) ").lower()

        if play_again == "n":
            print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    main()