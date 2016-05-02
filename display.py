"""
    This is the display class.
    Luis Filipe Ribeiro Dias
            2016
"""
from Tkinter import *

myFont = tkFont.Font(familit='Helvetica', size=36, weight='bold')


class MDisplay(object):
    """
        Handles display related operations
    """

    def __init__(self):
        """
            the initializer sets up some display parameters
        """
        self.win = Tk()
        # initialize window as black
        self.win.configure(bg='#000000')
        # give it a title
        self.win.title("HSV Exercise")
        # and a geometry
        self.win.geometry('800x480')

        # close button is always handy
        exitButton = Button(self.win, text="Exit", font=myFont,
                            command=exitProgram, height=2, width=6)
        exitButton.pack(side=Bottom)

    def update_bg(self, h, s, v):
        """
            update the background according to H, S & V
        """
        pass

    def exitProgram(self):
        """
            called when exit button is pressed
        """
        pass

    def __del__(self):
        """
            the terminator
        """
        self.win.quit()
