import time
from sense_hat import SenseHat

from utils import clean_led, RED, BLACK

heart_large = [
  0,0,0,0,0,0,0,0,
  0,1,1,0,0,1,1,0,
  1,1,1,1,1,1,1,1,
  1,1,1,1,1,1,1,1,
  1,1,1,1,1,1,1,1,
  0,1,1,1,1,1,1,0,
  0,0,1,1,1,1,0,0,
  0,0,0,1,1,0,0,0,
]

heart_small = [
  0,0,0,0,0,0,0,0,
  0,0,0,0,0,0,0,0,
  0,0,1,0,0,1,0,0,
  0,1,1,1,1,1,1,0,
  0,1,1,1,1,1,1,0,
  0,0,1,1,1,1,0,0,
  0,0,0,1,1,0,0,0,
  0,0,0,0,0,0,0,0,
]


@clean_led()
def app(beats):
    sense = SenseHat()

    h_large = [RED if i == 1 else BLACK for i in heart_large]
    h_small = [RED if i == 1 else BLACK for i in heart_small]

    for i in range(beats):
        heart = h_large if i % 2 else h_small
        sense.set_pixels(heart)
        time.sleep(0.8)


if __name__ == '__main__':
    app(beats=15)
