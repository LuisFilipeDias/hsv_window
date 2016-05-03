"""
    This is the display class.
    Luis Filipe Ribeiro Dias
            2016
"""
from tkinter import *

myFont = ('Times', 24, 'bold')

#################################

class MDisplay(object):
    """
        Handles display related operations
    """

    def __init__(self):
        """
            the initializer sets up some display parameters
        """
        self.window = Tk()
        # initialize window as black
        self.window.configure(bg='#000000')
        # give it a title
        self.window.title("HSV Exercise")
        # and a geometry
        self.window.geometry('800x480')

        # close button is always handy
        exitButton = Button(self.window, text="Exit", font=myFont,
                            command=self.exitProgram, height=2, width=6)
        exitButton.pack(pady=20, padx=20)

    def update_bg(self, r, g, b):
        """
            update the background according to H, S & V
        """
        # initialize window as black
        r = format(int(r * 0xFF), '02x')
        g = format(int(g * 0xFF), '02x')
        b = format(int(b * 0xFF), '02x')
        background = '#' + str(r) + str(g) + str(b)
        self.window.configure(bg=background)

    def loop(self):
        self.window.mainloop()

    def exitProgram(self):
        """
            called when exit button is pressed
        """
        print("Goodbye, cruel world...")
        self.window.quit()

    def __del__(self):
        """
            the terminator
        """
        pass
