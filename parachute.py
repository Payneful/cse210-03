from terminal_service import Terminal_Service

class Parachute:
    def __init__(self):
        self._mistakes = 0

    def add_mistake(self):
        self._mistakes += 1

    def create_stickman(self):
        picture = ""
        terminal = Terminal_Service()
        
        if self._mistakes == 0:
            picture = picture + "  ___\n"
        if self._mistakes <= 1:
            picture = picture + " /___\ \n"
        if self._mistakes <= 2:
            picture = picture + " \   / \n"
        if self._mistakes <= 3:
            picture = picture + "  \ / \n"
        if self._mistakes == 4:
            picture = picture + "   X \n"
        else:
            picture = picture + "   O \n"
        picture = picture + "  /|\ \n  / \ "
        #send picture to terminal
        terminal.output(picture)
        
    def get_mistakes(self):
        '''Returns the amount of mistakes'''
        return self._mistakes

"""
    Word
     ___    0 mistakes
    /___\   1 mistakes
    \   /   2 mistakes
     \ /    3 mistakes
      O     4 mistakes O -> X
     /|\ 
     / \ 
^^^^^^^^^^^
"""