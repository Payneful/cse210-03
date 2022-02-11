class Terminal_Service:
    def __init__(self):
        user_letter = ""

    def single_letter_input(self, message="Enter a letter: "):
        text = input(message).lower()
        self.user_letter = text[0]

    def output(self, message=""):
        print(f"{message}\n")