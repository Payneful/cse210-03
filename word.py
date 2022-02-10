# THis is the Word class
import random

word_list = ["apple", "pear", "grape"]

class Word:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = ""
        self.letters_list =[]
        

    def _start_game(self):
        self.choose_word()
        self.split_word()
        self.check_letter('p')

    def choose_word(self):
        """chooses a random word.
        Paramaeters
            self-- an instance of the Word class"""

        word = random.choice(self.word_list)
        self.word = word
        

    def split_word(self):
        """Splits a word into an array. Each element is one letter
        in order
        Parameters:
            self-- an instance of the Word class"""

        letters_list = []
        for letter in range (0, len(self.word)):
            letters_list.append(self.word[letter])
        
        self.letters_list = letters_list
    
    def check_letter(self, input_letter):
        """Checks if input letter is in the word
        Parameters:
            self-- an instance of the Word class"""
        correct_letter_indexes = []
        for i in range(0, len(self.letters_list)):
            correct_letter_indexes.append(0)

        for letter_index in range(0, len(self.letters_list)):
            if input_letter == self.letters_list[letter_index]:
                correct_letter_indexes[letter_index] = input_letter
        
        print(correct_letter_indexes)




director = Word(word_list)
director._start_game()


# word = "twilight"
# word_array = []
# word_length = len(word)
# for i in range(0, word_length):
#     word_array[i] = word[i]
# word_array.append(word[i])
# if letter in word: