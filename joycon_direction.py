import os, time
from pyjoycon import ButtonEventJoyCon, get_L_id, get_R_id

x = 1800
y = 1800
turnL = False
turnR = False
stopLoop = False
light = -1

#Get connected Joycons and attempt to set LEDs
joycon_l_id = get_L_id()
joycon_l = ButtonEventJoyCon(*joycon_l_id)

joycon_r_id = get_R_id()
joycon_r = ButtonEventJoyCon(*joycon_r_id)
for i in range(5):
    joycon_r.set_player_lamp_on(15)

time.sleep(0.2)

def bool_out(bool):
    if bool:
        return 1
    else:
        return -1

while True:
    x = joycon_l.get_stick_left_horizontal()
    y = joycon_l.get_stick_left_vertical()

    for event_type, status in joycon_l.events():
        if event_type == "l":
            if status:
                turnL = True
                turnR = False
            else:
                turnL = False
    
    for event_type, status in joycon_r.events():
        if event_type == "r":
            if status:
                turnR = True
                turnL = False
            else:
                turnR = False
        if event_type == "home" and status:
            stopLoop = True

    if stopLoop:
        for i in range(5):
            joycon_l.set_player_lamp_on(15)
        for i in range(5):
            joycon_r.set_player_lamp_on(15)
        break
    dX = x - 1800
    dY = y - 1800
    distance = (dX**2 + dY**2)**0.5
    inBounds = distance <= 1800

    os.system("clear")
    print("x:", x, "\n")
    print("y:", y, "\n")
    print("Distance:", round(distance), "  inBounds:", inBounds, "\n")
    if turnL:
        print("Output FL:", -1, "Output FR:", 1, "\n")
        print("Output BL:", -1, "Output BR:", 1)
        if light != 1:
            for i in range(5):
                joycon_l.set_player_lamp_flashing(15)
            for i in range(5):
                joycon_r.set_player_lamp_on(0)
            light=1
    elif turnR:
        print("Output FL:", 1, "Output FR:", -1, "\n")
        print("Output BL:", 1, "Output BR:", -1)
        if light != 2:
            for i in range(5):
                joycon_l.set_player_lamp_on(0)
            for i in range(5):
                joycon_r.set_player_lamp_flashing(15)
            light=2
    elif distance > 360:
        print("Output FL:", bool_out(dY >= -dX), "Output FR:", bool_out(dY >= -dX), "\n")
        print("Output BL:", bool_out(dY >= dX), "Output BR:", bool_out(dY >= dX))
        if light != 3:
            for i in range(5):
                joycon_l.set_player_lamp_on(15)
            for i in range(5):
                joycon_r.set_player_lamp_on(15)
            light=3
    else:
        print("Output FL:", 0, "Output FR:", 0, "\n")
        print("Output BL:", 0, "Output BR:", 0)
        if light != 0:
            for i in range(5):
                joycon_l.set_player_lamp_on(0)
            for i in range(5):
                joycon_r.set_player_lamp_on(0)
            light=0
    print("\nTurnL:", turnL, "TurnR:", turnR)
    time.sleep(0.01)