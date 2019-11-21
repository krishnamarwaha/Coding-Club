from sense_hat import SenseHat

sense = SenseHat()

gyro_only = sense.get_gyroscope()

print("p: {pitch}, r: {roll}, y:{yaw}".format(**gyro_only))
