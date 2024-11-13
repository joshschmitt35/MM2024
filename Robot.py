from gpiozero import OutputDevice, PWMOutputDevice
from time import sleep

# Pin Definitions for Motor 1
IN1_1 = OutputDevice(14)
IN1_2 = OutputDevice(15)
ENA = PWMOutputDevice(17)  # Enable for Motor 1

# Pin Definitions for Motor 2
IN2_1 = OutputDevice(18)
IN2_2 = OutputDevice(23)
ENB = PWMOutputDevice(27)  # Enable for Motor 2

# Pin Definitions for Motor 3
IN3_1 = OutputDevice(24)
IN3_2 = OutputDevice(25)
ENC = PWMOutputDevice(22)  # Enable for Motor 3

# Pin Definitions for Motor 4
IN4_1 = OutputDevice(5)
IN4_2 = OutputDevice(6)
END = PWMOutputDevice(13)  # Enable for Motor 4

def set_direction(motor, direction):
    """Sets the direction of a specified motor."""
    if motor == 1:
        if direction == 1:  # Forward
            IN1_1.value = 1
            IN1_2.value = 0
        elif direction == -1:  # Backward
            IN1_1.value = 0
            IN1_2.value = 1
    elif motor == 2:
        if direction == 1:
            IN2_1.value = 1
            IN2_2.value = 0
        elif direction == -1:
            IN2_1.value = 0
            IN2_2.value = 1
    elif motor == 3:
        if direction == 1:
            IN3_1.value = 1
            IN3_2.value = 0
        elif direction == -1:
            IN3_1.value = 0
            IN3_2.value = 1
    elif motor == 4:
        if direction == 1:
            IN4_1.value = 1
            IN4_2.value = 0
        elif direction == -1:
            IN4_1.value = 0
            IN4_2.value = 1

try:
    while True:
        motor = int(input("Enter motor number (1-4): "))
        direction = int(input("Enter direction (1 for forward, -1 for backward): "))
        
        if motor == 1:
            ENA.value = 1  # Enable Motor 1
        elif motor == 2:
            ENB.value = 1  # Enable Motor 2
        elif motor == 3:
            ENC.value = 1  # Enable Motor 3
        elif motor == 4:
            END.value = 1  # Enable Motor 4
        
        set_direction(motor, direction)
        
        sleep(0.1)  # Small delay to keep motors running
except KeyboardInterrupt:
    print("Program stopped by user")
    
    # Disable all motors
    ENA.value = 0
    ENB.value = 0
    ENC.value = 0
    END.value = 0
    IN1_1.value = 0
    IN1_2.value = 0
    IN2_1.value = 0
    IN2_2.value = 0
    IN3_1.value = 0
    IN3_2.value = 0
    IN4_1.value = 0
    IN4_2.value = 0
