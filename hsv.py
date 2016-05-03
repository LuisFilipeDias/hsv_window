"""
    This is the GPIO class.
    Luis Filipe Ribeiro Dias
            2016
"""
import RPi.GPIO as GPIO
import colorsys

# define the pins of each HSV controller
HUE_H = 17
HUE_L = 18
SATURATION_H = 27
SATURATION_L = 22
VALUE_H = 23
VALUE_L = 24


class HSV(object):
    """
        The HSV GPIO class
    """

    # these static values hold the current HSV value
    H = 0
    S = 0
    V = 0

    def __init__(self, window):
        """
            the initializer
            GPIO's direction and event listeners are setup here
        """
        self.value = 0x00
        self.window = window
        GPIO.setmode(GPIO.BCM)

    def increase(self, foo):
        """
            increase value callback
        """
        # lets use 10-steps for each parameter
        if self.value < 0x0A:
            self.value += 1
        # save the value on the class
        self.save_value()
        # convert to rgb and update window
        self.update()

    def decrease(self, foo):
        """
            decrease value callback
        """
        # value doesn't make sense below 0
        if self.value > 0x00:
            self.value -= 1
        # save the value on the class
        self.save_value()
        # convert to rgb and update window
        self.update()

    def update(self):
        """
            convert hsv to rgb and call window update background
        """
        # convert hsv to rgb using colorsys
        (r, g, b) = colorsys.hsv_to_rgb(HSV.H / 10, HSV.S / 10, HSV.V / 10)
        # the update operation itself
        self.window.update_background(r, g, b)

    def save_value(self):
        """
            save value on the class - for warning purposes
        """
        pass

    def __del__(self):
        """
            the terminator
        """
        pass


class Hue(HSV):
    """
        The Hue GPIO class
    """
    def __init__(self, disp):
        """
            the initializer: configure ports and callbacks
        """
        super().__init__(disp)
        # GPIO's set up as inputs.
        # They should be pulled up to avoid false detections.
        # All ports are wired to connect to GND on button press.
        GPIO.setup(HUE_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(HUE_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Add event interrupt callbacks on falling edges
        GPIO.add_event_detect(HUE_H, GPIO.FALLING,
                              callback=self.increase, bouncetime=300)
        GPIO.add_event_detect(HUE_L, GPIO.FALLING,
                              callback=self.decrease, bouncetime=300)

    def save_value(self):
        """
            save value on the class
        """
        HSV.H = self.value


class Saturation(HSV):
    """
        The Saturation GPIO class
    """
    def __init__(self, disp):
        """
            the initializer: configure ports and callbacks
        """
        super().__init__(disp)
        GPIO.setup(SATURATION_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(SATURATION_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(SATURATION_H, GPIO.FALLING,
                              callback=self.increase, bouncetime=300)
        GPIO.add_event_detect(SATURATION_L, GPIO.FALLING,
                              callback=self.decrease, bouncetime=300)

    def save_value(self):
        """
            save value on the class
        """
        HSV.S = self.value


class Value(HSV):
    """
        The Value GPIO class
    """
    def __init__(self, disp):
        """
            the initializer: configure ports and callbacks
        """
        super().__init__(disp)
        GPIO.setup(VALUE_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(VALUE_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(VALUE_H, GPIO.FALLING,
                              callback=self.increase, bouncetime=300)
        GPIO.add_event_detect(VALUE_L, GPIO.FALLING,
                              callback=self.decrease, bouncetime=300)

    def save_value(self):
        """
            save value on the class
        """
        HSV.V = self.value
