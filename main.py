#!/usr/bin/python
"""
    This is the main module.
    Luis Filipe Ribeiro Dias
            2016
"""

from gpio import MGPIO_H, MGPIO_S, MGPIO_V
from display import MDisplay
# import colorsys


def main():
    """
        main function
    :return: 0 on success
    """
    gpio_h = MGPIO_H()
    gpio_s = MGPIO_S()
    gpio_v = MGPIO_V()
    h_disp = MDisplay()


    while True:
        pass
        # colorsys.hsv_to_rgb(h, s, v)
        # h_disp.update_bg()

        # get h, s and v
        # define the steps of each (10?)


if __name__ == '__main__':
    main()
