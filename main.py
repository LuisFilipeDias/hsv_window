#!/usr/bin/python
"""
    This is the main module.
    Luis Filipe Ribeiro Dias
            2016
"""

from gpio import MGPIO_H, MGPIO_S, MGPIO_V
from display import MDisplay

import time

def main():
    """
        main function
    :return: 0 on success
    """

    h_disp = MDisplay()
    gpio_h = MGPIO_H(h_disp)
    gpio_s = MGPIO_S(h_disp)
    gpio_v = MGPIO_V(h_disp)

    h_disp.loop()

if __name__ == '__main__':
    main()
