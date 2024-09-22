import board
import digitalio
import storage

# Mount the CIRCUITPY drive as read-only unless
# the encoder switch is held down
encoder_switch = digitalio.DigitalInOut(board.BUTTON)
encoder_switch.switch_to_input(pull=digitalio.Pull.UP)
# if(encoder_switch.value):
#     print(f"Mounting Read-Only\n _    _____ / _______  __ _ ___\n| |/|/ / -_/ / __/ _ \/  ' / -_)\n|__,__/\__/_/\__/\___/_/_/_\__/\n ")
# else:
#     print("Mounting Read/Write")
storage.remount("/", not encoder_switch.value)
