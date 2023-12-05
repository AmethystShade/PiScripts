# JoyconScripts

Scripts to get data from Nintendo Joycons. Requires [joycon-python](https://pypi.org/project/joycon-python/).

## Current scripts:

- `joycon_test.py`: Displays basic Joycon input, including buttons pressed and data from the left joystick.
- `calibration.py`: (WIP) Generates data about Joycon joysticks.
- `direction_test.py`: A test for getting angles and distance from coordinates. (1800, 1800) is the centre. Requires [getkey](https://pypi.org/project/getkey/).
    - Now also gives outputs for the motors based on angle (and optionally distance). 1 and -1 are the maximum and minimum values.
- `get_speed.py`: Calculates robot speed based on wheel RPM. (Todo: move to other repo)