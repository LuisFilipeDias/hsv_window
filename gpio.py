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
# GPIO_4 pin 16
SATURATION_L = 16
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
        self.colors = {'h': 0, 's': 0, 'v': 0}

        GPIO.setmode(GPIO.BCM)

        # GPIO's set up as inputs.
        # They should be pulled up to avoid false detections.
        # Both ports are wired to connect to GND on button press.
        # So we'll be setting up falling edge detection
        GPIO.setup(HUE_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(HUE_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(SATURATION_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(SATURATION_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(VALUE_H, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(VALUE_L, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Add event interrupt callbacks on falling edges
        GPIO.add_event_detect(HUE_H, GPIO.FALLING,
                              callback=self.press_hue_h, bouncetime=300)
        GPIO.add_event_detect(HUE_L, GPIO.FALLING,
                              callback=self.press_hue_l, bouncetime=300)
        GPIO.add_event_detect(SATURATION_H, GPIO.FALLING,
                              callback=self.press_saturation_h, bouncetime=300)
        GPIO.add_event_detect(SATURATION_L, GPIO.FALLING,
                              callback=self.press_saturation_l, bouncetime=300)
        GPIO.add_event_detect(VALUE_H, GPIO.FALLING,
                              callback=self.press_value_h, bouncetime=300)
        GPIO.add_event_detect(VALUE_L, GPIO.FALLING,
                              callback=self.press_value_l, bouncetime=300)

    def press_hue_h(self):
        """
            more hue callback
        """
        self.colors['h'] += 1

    def press_hue_l(self):
        """
            less hue callback
        """
        self.colors['h'] -= 1

    def press_saturation_h(self):
        """
            more saturation callback
        """
        self.colors['s'] += 1

    def press_saturation_l(self):
        """
            less saturation callback
        """
        self.colors['s'] -= 1

    def press_value_h(self):
        """
            less value callback
        """
        self.colors['v'] += 1

    def press_value_l(self):
        """
            less value callback
        """
        self.colors['v'] -= 1

    def get_hue(self):
        """
            return the hue
        """
        return self.colors['h']

    def get_saturation(self):
        """
            return the saturation
        """
        return self.colors['s']

    def get_value(self):
        """
            return the value
        """
        return self.colors['v']

    def __del__(self):
        """
            the terminator
        """
        pass
