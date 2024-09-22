# MACROPAD Hotkeys: Chromebook controls
from adafruit_hid.keycode import Keycode

# Keycode.APPLICATION = 'meta' key for CB search/super 
BLANK = (0x000000, '    ', [])
# SIGNOUT = Keycode.CONTROL, Keycode.SHIFT, Keycode.Q, -Keycode.CONTROL, -Keycode.SHIFT, -Keycode.Q
app = {
    'name' : '_CB_deploy',
    'order' : 0,
    'macros' : [
        # # 1st row ----------
        (0x540908, 'Welcome', [Keycode.SPACE,2]),
        (0x544408, 'ENRL', ['enroll',1,Keycode.ENTER]),
        (0x04541B, 'Agree', [Keycode.SPACE]),
        # (0x04541B, 'Agree', [Keycode.ALT, Keycode.V, -Keycode.ALT]),
        # # 2nd row ----------
        (0x000754, 'S_Out*2', [Keycode.CONTROL, Keycode.SHIFT, Keycode.Q]),
        (0x000754, ' rmAcct', [Keycode.TAB, 0.2, -Keycode.TAB, 0.1, Keycode.ENTER, 0.3, -Keycode.ENTER, 0.3, Keycode.ENTER]),
        (0x000754, 'Close', [Keycode.CONTROL, 'w']),
        # # 3rd row ----------
        (0x095E06, 'STwifi', ['A8wRdCXf2kN)Dy7Z\n']),
        BLANK,
        (0x095E06, 'hotspot', ['0987654321\n']),
        # # 4th row ----------
        (0x080F54, '', []),
        (0x540908, '[ENTER]', [Keycode.RETURN]),
        (0x080F54, 'Wspot', ['12345678\n']),

        # # Encoder button ---
        # (0x544408, '', [])
    ]
}
