from pyjoycon import ButtonEventJoyCon, get_L_id, get_R_id
import time, os

#Get connected Joycons and attempt to set LEDs
joycon_l_id = get_L_id()
joycon_l = ButtonEventJoyCon(*joycon_l_id)
for i in range(5):
    joycon_l.set_player_lamp_on(15)

time.sleep(0.2)

joycon_r_id = get_R_id()
joycon_r = ButtonEventJoyCon(*joycon_r_id)
for i in range(5):
    joycon_r.set_player_lamp_on(15)

time.sleep(0.2)

minX = 9999
maxX = 0
minY = 9999
maxY = 0

buttonsPressed = []

while True:

    #Handle button presses/releases in left and right controllers
    for event_type, status in joycon_l.events():
        if status:
            buttonsPressed.append(event_type)
        else:
            buttonsPressed.remove(event_type)
    
    for event_type, status in joycon_r.events():
        if status:
            buttonsPressed.append(event_type)
        else:
            buttonsPressed.remove(event_type)

    #Get data from left joystick
    x = joycon_l.get_stick_left_horizontal()
    y = joycon_l.get_stick_left_vertical()

    if x < minX and x != 0: minX = x
    if x > maxX: maxX = x
    if y < minY and y != 0: minY = y
    if y > maxY: maxY = y

    #Output data
    os.system("clear")
    print("Current X:", x, "        Min X:", minX, "        Max X:", maxX, "\n")
    print("Mean X:", (minX+maxX)//2, "        X Range:", maxX-minX, "\n\n")
    print("Current Y:", y, "        Min Y:", minY, "        Max Y:", maxY, "\n")
    print("Mean Y:", (minY+maxY)//2, "        Y Range:", maxY-minY, "\n\n")
    print("Buttons Pressed:", ", ".join(i[0].upper() + i[1:] for i in sorted(buttonsPressed)))
    time.sleep(0.05)