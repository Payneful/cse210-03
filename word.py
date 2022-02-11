# This is the Word class
import random
word_list = ['apple', 'banana', 'pear']

class Word:
    def __init__(self, word_list):
        # stitched_word and guessed_letters are the only attributes 
        # accessable outside the Word class.
        self.stitched_word = ""
        self.guessed_letters = []
        self._word_list = word_list
        self._word = ""
        self._letters_list =[]
        self._letter_spaces = []
        self._letter_in_word = False

    # This function is called only once at the start of the game.
    def setup_word(self):
        """Sets up the word for the game.
        Parameters:
            self-- an instance of Word"""

        self._choose_word()
        self._split_word()
        self._setup_word_display()
        self._setup_guessed_list_english()
        self._stitch_letters()

    # This function is called repeatedly in the game loop.
    def update_word(self, input_letter):
        """Updates the word after a user guesses a letter
        Parameters:
            self-- an instance of Word
            inpout_letter-- the letter that was guessed"""

        self._check_letter(input_letter)
        if self._letter_in_word == True:
            self._letter_placement(input_letter)
        self._stitch_letters()
        self._update_guessed_letters(input_letter)
        
    def _choose_word(self):
        """chooses a random word.
        Paramaeters
            self-- an instance of the Word class"""

        _word = random.choice(self._word_list)
        self._word = _word
        
    def _split_word(self):
        """Splits a word into an array. Each element is one letter
        in order
        Parameters:
            self-- an instance of the Word class"""

        _letters_list = []
        for _letter in range (0, len(self._word)):
            _letters_list.append(self._word[_letter])
        
        self._letters_list = _letters_list
    
    def _check_letter(self, input_letter):
        """Checks if input letter is in the word
        Parameters:
            self-- an instance of the Word class
            input_letter-- the letter being checked"""

        if input_letter in self._word:
            self._letter_in_word = True
        
        else:
            self._letter_in_word = False

    def _letter_placement(self, input_letter):
        """Places the letters in the proper spots
        Parameters:
            self-- an instance of Word
            input_letter-- the letter guessed"""
        
        for _letter_index in range(0, len(self._letters_list)):
            _letter_element = self._letters_list[_letter_index]

            if _letter_element.lower() == input_letter.lower():
                self._letter_spaces[_letter_index] = input_letter.lower()
  
    def _stitch_letters(self):
        """Puts the letters and underscores together
        Parameters:
            self-- and instance of Word"""
        
        for _letter in self._letter_spaces:
            self.stitched_word += (_letter + " ")

    def _setup_word_display(self):
        """Generates an array to contain underscores (_)
        for each unguessed letter.
        Parameters:
            self-- an instance of Word"""
        
        for _space in range(0, len(self._word)):
            self._letter_spaces.append("_")
    
    def _setup_guessed_list_english(self):
        """sets up the guessed list with false elements
        A letter has been guessed if its index element is True
        Parameters:
            self-- an instance of Word"""

        for letter in range(0, 26):
            self.guessed_letters.append(False)

    def _update_guessed_letters(self, input_letter):
        """Updates the list of letters that have already been 
        guessed
        Parameters:
            self-- an instance of Word
            input_letter-- the letter to be added to the list
            of guessed letters"""
        
        _letter = input_letter.upper()
        _ascii_val = ord(_letter)
        _index_val = _ascii_val - 65
        self.guessed_letters[_index_val] = True

director = Word(word_list)
director.setup_word()
not_done = True
print(director.stitched_word)
while not_done:
    letter = input("letter: ")
    director.update_word(letter)
    print(director.stitched_word)
    