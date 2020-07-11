import random

from sense_hat import SenseHat

RED   = [255, 000, 000]
GREEN = [000, 255, 000]
BLUE  = [000, 000, 255]
BLACK = [000, 000, 000]
WHITE = [255, 255, 255]


def clean_led():
    def decorate(func):
        def call(*args, **kwargs):
            SenseHat().clear()
            result = func(*args, **kwargs)
            SenseHat().clear()
            return result
        return call
    return decorate


def random_color():
    return [
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    ]

