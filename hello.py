import time
from sense_hat import SenseHat

from .utils import clean_led, random_color


@clean_led()
def app(text):
    sense = SenseHat()

    for letter in text:
        sense.show_letter(letter, text_colour=random_color())
        time.sleep(0.4)

    sense.show_message(text, scroll_speed=0.05, text_colour=random_color())


if __name__ == '__main__':
    app(text="IPA Ky Ky!")
