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
        if key == getkey.keys.A and y > 0:
            x -= 10
        time.sleep(0.01)

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
    print("Angle:", angle)
    time.sleep(0.01)