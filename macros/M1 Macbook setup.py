# MACROPAD Hotkeys: M1 Macbooko setup
from adafruit_hid.keycode import Keycode
from consumer import Toolbar

class Open:
    touchID = 'open -b com.apple.systempreferences /System/Library/PreferencePanes/TouchID.prefPane'
    
    sound = 'open -b com.apple.systempreferences /System/Library/PreferencePanes/Sound.prefPane'

    new_terminal = r"Keycode.COMMAND, Keycode.SPACE, 'terminal', Keycode.RETURN"
    
    google = "open 'https://gmail.com' -a /Applications/Google\ Chrome.app; open /Applications/Google\ Drive.app"
    
    onepass = "open https://essd65.1password.com -a /Applications/Google\ Chrome.app; "
    
    zoom = "open https://district65.zoom.us -a /Applications/Google\ Chrome.app; open /Applications/zoom.us.app"
    
app = {
    'name' : 'M1 welcome',
    'order' : 12,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x540908, 'Terminal', [Open.new_terminal]),
        (0x544408, 'Screen ', [Keycode.COMMAND, Keycode.SHIFT, Keycode.S]),
        (0x04541B, '/Window ', [Keycode.COMMAND, Keycode.TAB]),
        # 2nd row ----------
        (0x000754, 'TouchID', [Open.touchID, Keycode.RETURN]),
        (0x000000, 'Sound', [Open.new_terminal, Open.sound]),
        (0x000754, 'closeWin', [Keycode.COMMAND, Keycode.W]),
        # 3rd row ----------
        (0x000000, 'Google', [Open.google, Keycode.RETURN]),
        (0x095E06, '1Password', [Open.onepass, Keycode. RETURN]),
        (0x000000, 'Zoom', [Open.zoom, Keycode.RETURN]),
        # 4th row ----------
        (0x080F54, '  ', []),
        (0x000000, '       ', []),
        (0x080F54, '   ', [])
    ]
}
