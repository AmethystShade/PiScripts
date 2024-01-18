import os, time, getkey, threading, math

x = 1800
y = 1800
turnL = False
turnR = False

def input_check():
    global x
    global y
    global turnL
    global turnR

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
        if key == getkey.keys.Q:
            turnL = True
            turnR = False
        elif key == getkey.keys.E:
            turnR = True
            turnL = False
        else:
            turnL = False
            turnR = False
        time.sleep(0.01)

def bool_out(bool):
    if bool:
        return 1
    else:
        return -1

input_thread = threading.Thread(target=input_check, args=())
input_thread.start()

while True:
    dX = x - 1800
    dY = y - 1800
    distance = math.sqrt(dX**2 + dY**2)
    inBounds = distance <= 1800

    os.system("clear")
    print("x:", x, "\n")
    print("y:", y, "\n")
    print("Distance:", round(distance), "  inBounds:", inBounds, "\n")
    if turnL:
        print("Output FL:", -1, "Output FR:", 1, "\n")
        print("Output BL:", -1, "Output BR:", 1)
    elif turnR:
        print("Output FL:", 1, "Output FR:", -1, "\n")
        print("Output BL:", 1, "Output BR:", -1)
    elif distance > 360:
        print("Output FL:", bool_out(dY >= -dX), "Output FR:", bool_out(dY >= -dX), "\n")
        print("Output BL:", bool_out(dY >= dX), "Output BR:", bool_out(dY >= dX))
    else:
        print("Output FL:", 0, "Output FR:", 0, "\n")
        print("Output BL:", 0, "Output BR:", 0)
    print(turnL,turnR)
    time.sleep(0.01)