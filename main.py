#!/usr/bin/python
"""
    This is the main module.
    Luis Filipe Ribeiro Dias
            2016
"""

from gpio import MGPIO_H, MGPIO_S, MGPIO_V
from display import MDisplay


import colorsys


def main():
    """
        main function
    :return: 0 on success
    """
    gpio_h = MGPIO_H()
    gpio_s = MGPIO_S()
    gpio_v = MGPIO_V()
    h_disp = MDisplay()

    (r,g,b) = colorsys.hsv_to_rgb(gpio_h.get_value(), gpio_s.get_value(), gpio_v.get_value())
    h_disp.update_bg(r,g,b)
    h_disp.loop()


if __name__ == '__main__':
    main()
