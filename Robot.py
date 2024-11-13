import curses
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

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking keyboard input
    stdscr.clear()
    stdscr.addstr("Control the robot using 'W' (up arrow) for forward and 'S' (down arrow) for backward.\n")
    stdscr.addstr("Press 'Q' to quit.\n")

    try:
        while True:
            key = stdscr.getch()
            if key in [curses.KEY_UP, ord('w')]:
                stdscr.addstr(3, 0, "Moving forward        ")
                set_all_motors(1)
                enable_all_motors(1)
            elif key in [curses.KEY_DOWN, ord('s')]:
                stdscr.addstr(3, 0, "Moving backward       ")
                set_all_motors(-1)
                enable_all_motors(1)
            elif key in [ord('q'), ord('Q')]:
                stdscr.addstr(3, 0, "Stopping the robot.   ")
                enable_all_motors(0)
                break
            else:
                enable_all_motors(0)  # Stop motors when no key is pressed

            sleep(0.1)  # Small delay to avoid rapid toggling
    except KeyboardInterrupt:
        enable_all_motors(0)  # Disable all motors
    finally:
        # Cleanup
        enable_all_motors(0)
        FL_IN1.value = FL_IN2.value = 0
        BL_IN1.value = BL_IN2.value = 0
        FR_IN1.value = FR_IN2.value = 0
        BR_IN1.value = BR_IN2.value = 0

# Run the curses application
curses.wrapper(main)
