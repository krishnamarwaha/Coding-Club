from sense_hat import SenseHat
from time import sleep
import time

sense = SenseHat()

number = [
[[0,1,1,1], # Zero
[0,1,0,1],
[0,1,0,1],
[0,1,1,1]],
[[0,0,1,0], # One
[0,1,1,0],
[0,0,1,0],
[0,1,1,1]],
[[0,1,1,1], # Two
[0,0,1,1],
[0,1,1,0],
[0,1,1,1]],
[[0,1,1,1], # Three
[0,0,1,1],
[0,0,1,1],
[0,1,1,1]],
[[0,1,0,1], # Four
[0,1,1,1],
[0,0,0,1],
[0,0,0,1]],
[[0,1,1,1], # Five
[0,1,1,0],
[0,0,1,1],
[0,1,1,1]],
[[0,1,0,0], # Six
[0,1,1,1],
[0,1,0,1],
[0,1,1,1]],
[[0,1,1,1], # Seven
[0,0,0,1],
[0,0,1,0],
[0,1,0,0]],
[[0,1,1,1], # Eight
[0,1,1,1],
[0,1,1,1],
[0,1,1,1]],
[[0,1,1,1], # Nine
[0,1,0,1],
[0,1,1,1],
[0,0,0,1]]
]

noNumber = [0,0,0,0]
hour_color = [255,0,0] #Red
minute_color = [0,255,255] #Cyan
empty = [0,0,0] #Black


while True:
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    clockImage = []

    for index in range(0, 4):
        if (hour >= 10):
            clockImage.extend(number[int(hour/10)][index])
        else:
            clockImage.extend(noNumber)
        clockImage.extend(number[int(hour%10)][index])

    for index in range(0, 4):
        clockImage.extend(number[int(minute/10)][index])
        clockImage.extend(number[int(minute%10)][index])

    for index in range(0, 64):
        if (clockImage[index]):
            if index < 32:
                clockImage[index] = hour_color
            else:
                clockImage[index] = minute_color
        else:
            clockImage[index] = empty

    sense.set_rotation(90) # Optional
    sense.low_light = True # Optional
    sense.set_pixels(clockImage)
    sleep(60)