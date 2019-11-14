from sense_hat import SenseHat
import time

sense = SenseHat()

number = [
    0,1,1,1,#Zero
    0,1,0,1,
    0,1,0,1,
    0,1,1,1,
    0,0,1,0,#One
    0,1,1,0,
    0,0,1,0,
    0,1,1,1,
    0,1,1,1,#Twon
    0,0,1,1,
    0,1,1,0,
    0,1,1,1,
    0,1,1,1,#Three
    0,0,1,1,
    0,0,1,1,
    0,1,1,1,
    0,1,0,1,#Four
    0,1,1,1,
    0,0,0,1,
    0,0,0.1,
    0,1,1,1,#Five
    0,1,1,0,
    0,0,1,1,
    0,1,1,1,
    0,1,0,0,#Six
    0,1,1,1,
    0,1,0,1,
    0,1,1,1,
    0,1,1,1,#Seven
    0,0,0,1,
    0,0,1,0,
    0,1,0,0,
    0,1,1,1,#Eight
    0,1,1,1,
    0,1,1,1,
    0,1,1,1,
    0,1,1,1,#Nine
    0,1,0,1,
    0,1,1,1,
    0,0,0,1
    ]
hour_color = [255,0,0] #Red
minute_color = [0,255,255] #Cyan
empty = [0,0,0] #Black

clock_image = [
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0
        ]

while True:
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    

    for index in range(0,64):
        if (clock_image[index]):
            if index < 32:
                clock_image[index] = hour_color
            else:
                clock_image[index] = minute_color
        else:
            clock_image[index] = empty
    
    sense.low_light = True#Optinal
    sense.set_pixels(clock_image)
    time.sleep(0.1)
    
    
    
    
