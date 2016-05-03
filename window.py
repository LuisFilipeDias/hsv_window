"""
    This is the display class.
    Luis Filipe Ribeiro Dias
            2016
"""
from tkinter import *

window_font = ('Times', 24, 'bold')


class Window(object):
    """
        Handles display related operations
    """

    def __init__(self):
        """
            the initializer sets up some display parameters
        """
        # instantiate TK
        self.window = Tk()
        # initialize window as black
        self.window.configure(bg='#000000')
        # give it a title
        self.window.title("HSV Exercise")
        # and a geometry
        self.window.geometry('800x480')

        # close button is always handy
        exit_button = Button(self.window, text="Exit", font=window_font,
                            command=self.exit, height=2, width=6)
        exit_button.pack(pady=0, padx=0)

    def update_background(self, r, g, b):
        """
            update the background according to H, S & V
        """
        # save value to byte-length hex
        r = format(int(r * 0xFF), '02x')
        g = format(int(g * 0xFF), '02x')
        b = format(int(b * 0xFF), '02x')
        # save rgb into string
        background = '#' + str(r) + str(g) + str(b)
        # configure background
        self.window.configure(bg=background)

    def loop(self):
        """
            the loop of the gui
        """
        self.window.mainloop()

    def exit(self):
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
