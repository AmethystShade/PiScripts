import math

#All units in SI
radius = 0.025
circumference = radius*2*math.pi

rpm = float(input("Enter RPM: "))
metresPerMin = circumference * rpm
speed = metresPerMin / 60


print("Speed:", speed, "m/s")