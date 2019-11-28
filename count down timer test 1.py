#!/bin/python3

from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

g = (0,255,0)
r = (255,0,0)

for i in range(1,6):
  sense.show_letter( str(i), r)
  sleep(1)
