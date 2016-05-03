"""
    This is the GPIO class.
    Luis Filipe Ribeiro Dias
            2016
"""
import RPi.GPIO as GPIO

# define the pins of each HSV controller
HUE_H = 12
HUE_L = 13
SATURATION_H = 11
SATURATION_L = 7
VALUE_H = 18
VALUE_L = 22


class MGPIO(object):
    """
        Handles gpio related operations
    """

    def __init__(self):
        """
            the initializer
            GPIO's direction and event listeners are setup here
        """
        self.value = 0x00
        GPIO.setmode(GPIO.BCM)

    def inc_value(self):
        """
            increase value callback
        """
        if self.value < 0xFF:
            self.value += 1

    def dec_value(self):
        """
            decrease value callback
        """
        if self.value > 0x00:
            self.value -= 1

    def get_value(self):
        """
            return the value
        """
        return self.value

    def __del__(self):
        """
            the terminator
        """
        pass


class MGPIO_H(MGPIO):
    def __init__(self):
        """
            the initializer: configure ports and callbacks
        """
        super().__init__()

        # GPIO's set up as inputs.
        # They should be pulled up to avoid false detections.
        # All ports are wired to connect to GND on button press.
        GPIO.setup(HUE_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(HUE_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Add event interrupt callbacks on falling edges
        GPIO.add_event_detect(HUE_H, GPIO.FALLING,
                              callback=self.inc_value, bouncetime=300)
        GPIO.add_event_detect(HUE_L, GPIO.FALLING,
                              callback=self.dec_value, bouncetime=300)


class MGPIO_S(MGPIO):
    def __init__(self):
        """
            the initializer: configure ports and callbacks
        """
        super().__init__()

        GPIO.setup(SATURATION_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(SATURATION_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(SATURATION_H, GPIO.FALLING,
                              callback=self.inc_value, bouncetime=300)
        GPIO.add_event_detect(SATURATION_L, GPIO.FALLING,
                              callback=self.dec_value, bouncetime=300)
        self.value = 0


class MGPIO_V(MGPIO):
    def __init__(self):
        """
            the initializer: configure ports and callbacks
        """
        super().__init__()

        GPIO.setup(VALUE_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(VALUE_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(VALUE_H, GPIO.FALLING,
                              callback=self.inc_value, bouncetime=300)
        GPIO.add_event_detect(VALUE_L, GPIO.FALLING,
                              callback=self.dec_value, bouncetime=300)
        self.value = 0
