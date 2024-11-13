import keyboard
from gpiozero import OutputDevice, PWMOutputDevice
from time import sleep

# Pin Definitions for each motor
# Front Left Motor
FL_IN1 = OutputDevice(27)
FL_IN2 = OutputDevice(17)
FL_EN = PWMOutputDevice(22)

# Back Left Motor
BL_IN1 = OutputDevice(26)
BL_IN2 = OutputDevice(19)
BL_EN = PWMOutputDevice(13)

# Front Right Motor
FR_IN1 = OutputDevice(20)
FR_IN2 = OutputDevice(21)
FR_EN = PWMOutputDevice(16)

# Back Right Motor
BR_IN1 = OutputDevice(24)
BR_IN2 = OutputDevice(23)
BR_EN = PWMOutputDevice(25)

def set_all_motors(direction):
    """Sets the direction for all motors."""
    if direction == 1:  # Forward
        FL_IN1.value, FL_IN2.value = 1, 0
        BL_IN1.value, BL_IN2.value = 1, 0
        FR_IN1.value, FR_IN2.value = 1, 0
        BR_IN1.value, BR_IN2.value = 1, 0
    elif direction == -1:  # Backward
        FL_IN1.value, FL_IN2.value = 0, 1
        BL_IN1.value, BL_IN2.value = 0, 1
        FR_IN1.value, FR_IN2.value = 0, 1
        BR_IN1.value, BR_IN2.value = 0, 1

def enable_all_motors(state):
    """Enables or disables all motors."""
    FL_EN.value = BL_EN.value = FR_EN.value = BR_EN.value = state

try:
    print("Control the robot using 'W' (up arrow) for forward and 'S' (down arrow) for backward.")
    print("Press 'Q' to quit.")

    while True:
        if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
            print("Moving forward")
            set_all_motors(1)
            enable_all_motors(1)
            sleep(0.1)  # Add a small delay to avoid rapid toggling
        elif keyboard.is_pressed('s') or keyboard.is_pressed('down'):
            print("Moving backward")
            set_all_motors(-1)
            enable_all_motors(1)
            sleep(0.1)
        elif keyboard.is_pressed('q'):
            print("Stopping the robot.")
            enable_all_motors(0)
            break
        else:
            enable_all_motors(0)  # Stop motors when no key is pressed
            sleep(0.1)
except KeyboardInterrupt:
    print("Program stopped by user")
    enable_all_motors(0)  # Disable all motors
    # Set all control pins to 0 to safely stop motors
    FL_IN1.value = FL_IN2.value = 0
    BL_IN1.value = BL_IN2.value = 0
    FR_IN1.value = FR_IN2.value = 0
    BR_IN1.value = BR_IN2.value = 0
