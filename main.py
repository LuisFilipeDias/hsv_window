#!/usr/bin/python
"""
    This is the main module.
    Luis Filipe Ribeiro Dias
            2016
"""

import sys
assert sys.version_info[0] >= 3

from window import Window
from hsv import Hue, Saturation, Value


def main():
    """
        main function
    :return: 0 on success
    """

    # create window object
    window = Window()

    # create the HSV objects, no need to
    # keep the instance, everything is handled
    # via interruptions inside
    Hue(window)
    Saturation(window)
    Value(window)

    # start window loop
    window.loop()

if __name__ == '__main__':
    main()
