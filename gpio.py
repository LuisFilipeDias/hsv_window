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


class MGPIO(object):
    """
        Handles gpio related operations
    """

    h = 0
    s = 0
    v = 0

    def __init__(self, disp):
        """
            the initializer
            GPIO's direction and event listeners are setup here
        """
        self.value = 0x00
        self.disp = disp
        GPIO.setmode(GPIO.BCM)

    def inc_value(self, foo):
        """
            increase value callback
        """
        if self.value < 0x0A:
            self.value += 1
        self.refresh()
        self.update_bg()

    def dec_value(self, foo):
        """
            decrease value callback
        """
        if self.value > 0x00:
            self.value -= 1
        self.refresh()
        self.update_bg()

    def update_bg(self):
        (r,g,b) = colorsys.hsv_to_rgb(MGPIO.h/10, MGPIO.s/10, MGPIO.v/10)
        self.disp.update_bg(r, g,b)
    
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
                              callback=self.inc_value, bouncetime=300)
        GPIO.add_event_detect(HUE_L, GPIO.FALLING,
                              callback=self.dec_value, bouncetime=300)

    def refresh(self):
        MGPIO.h = self.value

class MGPIO_S(MGPIO):
    def __init__(self, disp):
        """
            the initializer: configure ports and callbacks
        """
        super().__init__(disp)
        GPIO.setup(SATURATION_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(SATURATION_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(SATURATION_H, GPIO.FALLING,
                              callback=self.inc_value, bouncetime=300)
        GPIO.add_event_detect(SATURATION_L, GPIO.FALLING,
                              callback=self.dec_value, bouncetime=300)

    def refresh(self):
        MGPIO.s = self.value
    
class MGPIO_V(MGPIO):
    def __init__(self, disp):
        """
            the initializer: configure ports and callbacks
        """
        super().__init__(disp)
        GPIO.setup(VALUE_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(VALUE_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(VALUE_H, GPIO.FALLING,
                              callback=self.inc_value, bouncetime=300)
        GPIO.add_event_detect(VALUE_L, GPIO.FALLING,
                              callback=self.dec_value, bouncetime=300)
    
    def refresh(self):
        MGPIO.v = self.value
    
