"""
    This is the display class.
    Luis Filipe Ribeiro Dias
            2016
"""
from tkinter import *

myFont = ('Times', 24, 'bold')


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
                            command=self.exitProgram, height=2, width=6)
        exitButton.pack(pady=20, padx=20)

    def update_bg(self, r, g, b):
        """
            update the background according to H, S & V
        """
        # initialize window as black
        background = '#' + str(r) + str(g) + str(b)
        self.win.configure(bg=background)

    def loop(self):
        self.win.mainloop()

    def exitProgram(self):
        """
            called when exit button is pressed
        """
        pass

    def __del__(self):
        """
            the terminator
        """
