"""
    This is the GPIO class.
    Luis Filipe Ribeiro Dias
            2016
"""
import RPi.GPIO as GPIO

# GPIO_1 pin 12
HUE_H = 12
# GPIO_2 pin 13
HUE_L = 13
# GPIO_3 pin 11
SATURATION_H = 11
# GPIO_4 pin 7
SATURATION_L = 7
# GPIO_5 pin 18
VALUE_H = 18
# GPIO_6 pin 22
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
        GPIO.setmode(GPIO.BCM)


    def __del__(self):
        """
            the terminator
        """
        pass

class MGPIO_H(MGPIO):

    def __init__(self):
        super().__init__()

        # GPIO's set up as inputs.
        # They should be pulled up to avoid false detections.
        # Both ports are wired to connect to GND on button press.
        # So we'll be setting up falling edge detection
        GPIO.setup(HUE_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(HUE_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Add event interrupt callbacks on falling edges
        GPIO.add_event_detect(HUE_H, GPIO.FALLING,
                              callback=self.inc_value, bouncetime=300)
        GPIO.add_event_detect(HUE_L, GPIO.FALLING,
                              callback=self.dec_value, bouncetime=300)
        self.value = 0

    def inc_value(self):
        self.value += 1

    def dec_value(self):
        self.value -= 1

    def get_value(self):
        return self.value

    def __del__(self):
        """
            the terminator
        """
        pass

class MGPIO_S(MGPIO):

    def __init__(self):
        super().__init__()

        # GPIO's set up as inputs.
        # They should be pulled up to avoid false detections.
        # Both ports are wired to connect to GND on button press.
        # So we'll be setting up falling edge detection
        GPIO.setup(SATURATION_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(SATURATION_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Add event interrupt callbacks on falling edges
        GPIO.add_event_detect(SATURATION_H, GPIO.FALLING,
                              callback=self.inc_value, bouncetime=300)
        GPIO.add_event_detect(SATURATION_L, GPIO.FALLING,
                              callback=self.dec_value, bouncetime=300)
        self.value = 0

    def inc_value(self):
        self.value += 1

    def dec_value(self):
        self.value -= 1

    def get_value(self):
        return self.value

    def __del__(self):
        """
            the terminator
        """
        pass

class MGPIO_V(MGPIO):

    def __init__(self):
        super().__init__()

        # GPIO's set up as inputs.
        # They should be pulled up to avoid false detections.
        # Both ports are wired to connect to GND on button press.
        # So we'll be setting up falling edge detection
        GPIO.setup(VALUE_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(VALUE_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Add event interrupt callbacks on falling edges
        GPIO.add_event_detect(VALUE_H, GPIO.FALLING,
                              callback=self.inc_value, bouncetime=300)
        GPIO.add_event_detect(VALUE_L, GPIO.FALLING,
                              callback=self.dec_value, bouncetime=300)
        self.value = 0

    def inc_value(self):
        self.value += 1

    def dec_value(self):
        self.value -= 1

    def get_value(self):
        return self.value

    def __del__(self):
        """
            the terminator
        """
        pass

