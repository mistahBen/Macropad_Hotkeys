# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Linux Firefox', # Application 
    'order' : 4,
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.CONTROL, '[']),
        (0x004000, 'Fwd >', [Keycode.CONTROL, ']']),
        (0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x202000, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x202000, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', [Keycode.CONTROL, 'r']),
        (0x000040, 'Home', [Keycode.CONTROL, 'h']),
        (0x000040, 'Private', [Keycode.CONTROL, Keycode.SHIFT, 'p']),
        # 4th row ----------
        (0xCD1E27, 'Notion', [Keycode.CONTROL, 'n', -Keycode.COMMAND,
                           'notion.so\n']),
        (0x000000, '', []),
        (0xCD1E27, 'Reddit', [Keycode.CONTROL, 'n', -Keycode.COMMAND,
                             'www.reddit.com\n']),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close window/tab
    ]
}
