class Terminal_Service:
    def __init__(self):
        user_letter = ""

    def single_letter_input(self, message="Enter a letter: "):
        """Gets a single letter from the user.
        Parameters:
            self-- an instance of Terminal_Service
            message-- the letter input by the user"""
        text = input(message).lower()
        self.user_letter = text[0]

    def output(self, message=""):
        """Writes output to the user on the screen.
        Parameters:
            self-- an instance of Terminal_Service
            message-- the desired characters to output"""
        print(f"{message}\n")