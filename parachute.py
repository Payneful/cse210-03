from terminal_service import Terminal_Service

class parachute:
    def __init__(self):
        self._mistakes = 0
        console = Terminal_Service()

    def add_mistake(self):
        self._mistakes += 1

    def create_stickman(self):
        picture = "\n"
        if self._mistakes == 0:
            picture = picture + "  ___\n"
        if self._mistakes < 2:
            picture = picture + " /___\ \n"
        if self._mistakes < 3:
            picture = picture + " \   / \n"
        if self._mistakes < 4:
            picture = picture + "  \ / \n"
        if self._mistakes == 4:
            picture = picture + "   X \n"
        else:
            picture = picture + "   O \n"
        picture = picture + "  /|\ \n  / \ \n"
        #send picture to terminal
        self.console.output(picture)




"""
    Word

     ____   0 mistakes
    /____\    1 mistakes
    \    /   2 mistakes
     \  /   3 mistakes
      O     4 mistakes O -> X
     /|\ 
     / \ 

^^^^^^^^^^^
"""