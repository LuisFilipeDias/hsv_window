#!/usr/bin/python
"""
    This is the main module.
    Luis Filipe Ribeiro Dias
            2016
"""

from gpio import MGPIO_H, MGPIO_S, MGPIO_V
from display import MDisplay


# import colorsys
import time

def main():
    """
        main function
    :return: 0 on success
    """
    gpio_h = MGPIO_H()
    gpio_s = MGPIO_S()
    gpio_v = MGPIO_V()

#    (r,g,b) = colorsys.hsv_to_rgb(gpio_h.get_value(), gpio_s.get_value(), gpio_v.get_value())
#    h_disp.update_bg(r,g,b)
#    h_disp = MDisplay()
#    h_disp.loop()

    while True:
        print("H: " + str(gpio_h.get_value()))
        print("S: " + str(gpio_s.get_value()))
        print("S: " + str(gpio_v.get_value()))
        # colorsys.hsv_to_rgb(h, s, v)
        # h_disp.update_bg()

        time.sleep(1)
        # get h, s and v
        # define the steps of each (10?)


if __name__ == '__main__':
    main()
