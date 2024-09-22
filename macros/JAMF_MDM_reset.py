# For running Jamf MDM devices on laptops
from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

## strings for commands
checkPolicy = "sudo jamf policy\n"
removeMDM = "sudo jamf removemdmprofile\n"
jamfRenew = "sudo profiles renew -type enrollment\n"

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Jamf MDM',
    'order' : 3,
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x27B1E0, 'Policychk', [str(checkPolicy)]),
        (0x27B1E0, 'Rm MDM', [str(removeMDM)]),
        (0x400000, 'Renew', [str(jamfRenew)]),
        # 2nd row ----------
        (0x202000, 'Remind', ['less renew.txt']),
        (0x202000, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (0x400000, 'Down', ' '),  # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', [Keycode.CONTROL, 'r']),
        (0x000040, 'Home', [Keycode.CONTROL, 'H']),
        (0x000040, 'Private', [Keycode.CONTROL, 'N']),
        # 4th row ----------
        (0x800000, '', []),
        (0x000000, '', []),
        (0x101010, '', []),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w'])  # Close window/tab
    ]
}
