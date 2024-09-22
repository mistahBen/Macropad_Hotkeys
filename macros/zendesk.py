# MACROPAD Hotkeys for Zendesk, Chrome

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Zendesk',
    'order' : 9,
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xA500FE, 'Views', [Keycode.CONTROL, Keycode.ALT, 'v']),  # go to Views
        (0xFEE111, 'Current', [Keycode.CONTROL, Keycode.ALT, 't']),
        (0x00FE87, 'NewTkt', [Keycode.CONTROL, Keycode.ALT, 'n']),  # make new ticket
        # 2nd row ----------
        (0x11FAFE, 'Reply', [Keycode.CONTROL, Keycode.ALT, 'c']),
        (0x11FAFE, 'Note', [Keycode.CONTROL, Keycode.ALT, 'x']),
        (0x11FAFE, 'Macro', [Keycode.CONTROL, Keycode.ALT, 'm']),                     # Scroll down
        # 3rd row ----------
        (0x0FFE00, 'Open', [Keycode.CONTROL, Keycode.ALT, 'o']),  # submit ticket as open
        (0xF2FE00, 'Pend', [Keycode.CONTROL, Keycode.ALT, 'p']),  # submit as pending
        (0xFE0000, 'Solve', [Keycode.CONTROL, Keycode.ALT, 's']),  # submit as solved
        # 4th row ----------
        (0x00FEEF, '< Prev', [Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.TAB]),  #prev ticket tab
        (0xE700FE, 'Next >', [Keycode.CONTROL, Keycode.ALT, Keycode.TAB]),  # next ticket tab
        (0x000000, 'close', [Keycode.CONTROL, Keycode.ALT, 'w']),  # close current tab
        # Encoder button ---
        (0xE700FE, 'search', [Keycode.CONTROL, Keycode.ALT, '/'])  # Open search
    ]
}

