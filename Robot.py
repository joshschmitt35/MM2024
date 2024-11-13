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
    while True:
        # Ask the user for the direction
        direction = int(input("Enter direction for all motors (1 for forward, -1 for backward): "))
        set_all_motors(direction)
        enable_all_motors(1)  # Enable all motors

        # Keep motors running until the user wants to stop or change direction
        while True:
            command = input("Enter 'stop' to stop all motors or 'change' to change direction: ").strip().lower()
            if command == 'stop':
                enable_all_motors(0)  # Disable all motors
                print("All motors stopped.")
                break
            elif command == 'change':
                break  # Break to the outer loop to change direction
            else:
                print("Invalid command. Please enter 'stop' or 'change'.")
except KeyboardInterrupt:
    print("Program stopped by user")
    enable_all_motors(0)  # Disable all motors
    # Set all control pins to 0 to safely stop motors
    FL_IN1.value = FL_IN2.value = 0
    BL_IN1.value = BL_IN2.value = 0
    FR_IN1.value = FR_IN2.value = 0
    BR_IN1.value = BR_IN2.value = 0
