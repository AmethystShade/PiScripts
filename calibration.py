from pyjoycon import ButtonEventJoyCon, get_L_id, get_R_id
import time, os, json

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

#Choose Joycon to calibrate
chosen = 0

while chosen == 0:
    for event_type, status in joycon_l.events():
        if status:
            chosen = 1
            break

    for event_type, status in joycon_r.events():
        if status:
            chosen = 2
            break
    
    os.system("clear")
    print("Press a button on the Joycon you want to calibrate")
    time.sleep(0.05)

if chosen == 1:
    joycon_c = joycon_l
else:
    joycon_c = joycon_r

for i in range(5):
    joycon_c.set_player_lamp_flashing(15)

time.sleep(0.2)

os.system("clear")
driftCheck = input("Does this controller drift? (y/n) ")
while driftCheck.lower() != "y" and driftCheck.lower() != "n":
    os.system("clear")
    driftCheck = input("Try again: Does this controller drift? (y/n) ")

if driftCheck.lower() == "y":
    doesDrift = True
else:
    doesDrift = False


os.system("clear")
print("Keep pushing the stick all the way up for this part\n")
input("(Press enter to continue...)")

count = 0
maxY = 0

while count < 200:
    os.system("clear")

    if chosen == 1:
        currentY = joycon_c.get_stick_left_vertical()
    else:
        currentY = joycon_c.get_stick_right_vertical()
    
    if currentY > maxY:
        maxY = currentY
    
    print("Current Y:", currentY, "\n")
    print("[", end="")
    
    for i in range(20):
        if (count+1)//10 > i:
            print("-", end="")
        else:
            print(" ", end="")
    
    print("]\n")

    count += 1
    time.sleep(0.05)

print("Done! Maximum Y:", maxY, "\n")
input("(Press enter to continue...)")

os.system("clear")
print("Keep pushing the stick all the way down for this part\n")
input("(Press enter to continue...)")

count = 0
minY = 99999

while count < 200:
    os.system("clear")

    if chosen == 1:
        currentY = joycon_c.get_stick_left_vertical()
    else:
        currentY = joycon_c.get_stick_right_vertical()
    
    if currentY < minY and currentY != 0:
        minY = currentY
    
    print("Current Y:", currentY, "\n")
    print("[", end="")
    
    for i in range(20):
        if (count+1)//10 > i:
            print("-", end="")
        else:
            print(" ", end="")
    
    print("]\n")

    count += 1
    time.sleep(0.05)

print("Done! Minimum Y:", minY, "\n")
input("(Press enter to continue...)")

os.system("clear")
print("Keep pushing the stick all the way left for this part\n")
input("(Press enter to continue...)")

count = 0
minX = 99999

while count < 200:
    os.system("clear")

    if chosen == 1:
        currentX = joycon_c.get_stick_left_horizontal()
    else:
        currentX = joycon_c.get_stick_right_horizontal()
    
    if currentX < minX and currentX != 0:
        minX = currentX
    
    print("Current X:", currentX, "\n")
    print("[", end="")
    
    for i in range(20):
        if (count+1)//10 > i:
            print("-", end="")
        else:
            print(" ", end="")
    
    print("]\n")

    count += 1
    time.sleep(0.05)

print("Done! Minimum X:", minX, "\n")
input("(Press enter to continue...)")

os.system("clear")
print("Keep pushing the stick all the way right for this part\n")
input("(Press enter to continue...)")

count = 0
maxX = 0

while count < 200:
    os.system("clear")

    if chosen == 1:
        currentX = joycon_c.get_stick_left_horizontal()
    else:
        currentX = joycon_c.get_stick_right_horizontal()
    
    if currentX > maxX:
        maxX = currentX
    
    print("Current X:", currentX, "\n")
    print("[", end="")
    
    for i in range(20):
        if (count+1)//10 > i:
            print("-", end="")
        else:
            print(" ", end="")
    
    print("]\n")

    count += 1
    time.sleep(0.05)

print("Done! Maximum X:", maxX, "\n")
input("(Press enter to continue...)")

meanX = (minX + maxX)//2
meanY = (minY + maxY)//2

driftDirX = 0
driftDirY = 0

if doesDrift:
    detectDrift = True
    while detectDrift:

        minDriftX = 99999
        maxDriftX = 0
        minDriftY = 99999
        maxDriftX = 0

        os.system("clear")
        print("Leave the stick centred, this will try to detect the direction of drift.\n")
        input("(Press enter to continue...)")

        count = 0

        while count < 200:
            os.system("clear")

            if chosen == 1:
                currentX = joycon_c.get_stick_left_horizontal()
                currentY = joycon_c.get_stick_left_vertical()
            else:
                currentX = joycon_c.get_stick_right_horizontal()
                currentY = joycon_c.get_stick_right_vertical()
            
            
            print("Current X:", currentX, "\n")
            print("Current Y:", currentY, "\n")
            print("[", end="")

            if currentX < minDriftX:
                minDriftX = currentX
            if currentX > maxDriftX:
                maxDriftX = currentX
            if currentY < minDriftY:
                minDriftY = currentY
            if currentY > maxDriftX:
                maxDriftY = currentY
            
            for i in range(20):
                if (count+1)//10 > i:
                    print("-", end="")
                else:
                    print(" ", end="")
            
            print("]\n")

            count += 1
            time.sleep(0.05)
        
        
        if meanX - minDriftX > 150:
            driftDirX = -1
        elif maxDriftX - meanX > 150:
            driftDirX = 1
        if meanY - minDriftY > 150:
            driftDirY = -1
        elif maxDriftY - meanY > 150:
            driftDirY = 1
        
        os.system("clear")
        if driftDirX != 0 or driftDirY != 0:
            print("Drift detected:\n")
            print("Horizontal drift direction:", driftDirX)
            print("Vertical drift direction:", driftDirY)
            detectDrift = False
        else:
            driftAnswer = input("Drift not detected, try again? (y/n) ")
            if driftAnswer.lower() != "y":
                detectDrift = False

calibrationData = {
    "x" : {
        "min" : minX,
        "max" : maxX,
        "mean" : meanX
    },
    "y" : {
        "min" : minY,
        "max" : maxY,
        "mean" : meanY
    },
    "drift" : doesDrift
}

if doesDrift:
    calibrationData["x"]["drift"] = driftDirX
    calibrationData["y"]["drift"] = driftDirY

if chosen == 1:
    f = open("calibration_l.json", "w")
else:
    f = open("calibration_r.json", "w")

json.dump(calibrationData, f)
f.close()

for i in range(5):
    joycon_c.set_player_lamp_on(15)
time.sleep(0.2)