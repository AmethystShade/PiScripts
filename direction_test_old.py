import os, time, getkey, threading, math

x = 1800
y = 1800

def input_check():
    global x
    global y

    while True:
        key = getkey.getkey()
        if key == getkey.keys.W and y < 3600:
            y += 10
        if key == getkey.keys.S and y > 0:
            y -= 10
        if key == getkey.keys.D and x < 3600:
            x += 10
        if key == getkey.keys.A and x > 0:
            x -= 10
        time.sleep(0.01)

def calc_L(a, d):
    if a != "N/A":
        a -= 90
        if a < 0: a += 360
    return calc_R(a,d)

def calc_R(a, d):
    if a != "N/A" and d <= 1800:
        D = d / 1800
        A = a % 180
        if a >= 180: mult = 1 #Ternary operations are so much cooler in C#...
        else: mult = -1

        out = ((A-45) / 45)
        if out > 1: out = 1
        return out * mult * D
    else:
        return 0


input_thread = threading.Thread(target=input_check, args=())
input_thread.start()

while True:
    dX = x - 1800
    dY = y - 1800
    distance = math.sqrt(dX**2 + dY**2)
    inBounds = distance <= 1800
    if dX == 0 and dY == 0:
        angle = "N/A"
    elif dY == 0:
        if dX > 0:
            angle = 90.0
        else:
            angle = -90.0
    else:
        angle = round(math.atan(dX/dY)*180/math.pi, 1)
    
    if dY < 0:
        angle += 180
    elif dX < 0:
        angle += 360
    
    

    os.system("clear")
    print("x:", x, "\n")
    print("y:", y, "\n")
    print("Distance:", round(distance), "  inBounds:", inBounds, "\n")
    print("Angle:", angle, "\n")
    print("output_L:", calc_L(angle, 1800), "output_R:", calc_R(angle, 1800), "\n")
    print("output_L_dist:", calc_L(angle, distance), "output_R_dist:", calc_R(angle, distance))
    time.sleep(0.01)