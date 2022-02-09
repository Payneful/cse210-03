class Terminal_Service:
    def __init__(self):
        user_letter = ""

    def input(self, message="Enter a letter: "):
        text = input(message)
        user_letter = text[0]
        return user_letter

    def output(self, message=""):
        print(f"{message}\n")

