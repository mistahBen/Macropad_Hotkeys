from adafruit_hid.keycode import Keycode

macro_order = {
    'chrmbk': 0,
    'zendesk': 1,
    'FF_browser': 2,
    'Jamf': 3,
    'Zendesk': 4,
    'Media': 5,
    'Zoom': 6,
}

class FF_browser():

    cName = __class__.name
    order = macro_order.get(f"{cName}") 

    app =    {                       
    'name' : 'Linux Firefox', # Application 
    'order' : order,
    'macros' : [              
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

class Chrmbk:

    cName = __class__.name
    order = macro_order.get(f"{cName}") 
    app = {
        'name' : 'CB ctrls',
        'order' : order,
        'macros' : [
            # # 1st row ----------
            (0x540908, 'Sign_in', ['alexanderb@district65.net', Keycode.ENTER]),
            (0x544408, 'Pass', ['Plague12monkeys.', Keycode.ENTER]),
            (0x04541B, 'Version', [Keycode.ALT, Keycode.V, -Keycode.ALT]),
            # # 2nd row ----------
            (0x000754, 'S_Out*2', [Keycode.CONTROL, Keycode.SHIFT, Keycode.Q]),
            (0x000754, ' rmAcct', [Keycode.TAB, 0.2, -Keycode.TAB, 0.1, Keycode.ENTER, 0.3, -Keycode.ENTER, 0.3, Keycode.ENTER]),
            (0x000754, 'Close', [Keycode.CONTROL, 'w']),
            # # 3rd row ----------
            (0x095E06, 'STwifi', ['A8wRdCXf2kN)Dy7Z\n']),
            BLANK,
            (0x095E06, 'hotspot', ['0987654321\n']),
            # # 4th row ----------
            (0x080F54, 'Update', [Keycode.ALT, Keycode.SHIFT, 'L',  Keycode.ENTER, -Keycode.ALT, -Keycode.SHIFT, 0.2, -Keycode.ENTER, 'chrome://os-settings/help\n', Keycode.RETURN]),
            (0x540908, '[ENTER]', [Keycode.RETURN]),
            (0x080F54, 'Wspot', ['12345678\n']),

            # # Encoder button ---
            # (0x544408, '', [])
        ]
    }

class Ipad_cfg:

    cName = __class__.name
    order = macro_order.get(f"{cName}") 

    app = {                    
        'name' : 'iPad Controls',  # Application name
        'order' : order,
        'macros' : [           
            # COLOR    LABEL    KEY SEQUENCE
            # 1st row ----------
            (0x54FF04, '[Single]', [str(cfg)]),
            (0xF0FF04, '[All]', [str(allIpads)]),
            (0x000000, '', []),
            # 2nd row ----------
            (0x33D7FF, 'Serial#', [str(getSerial)]),
            (0x33D7FF, 'List', [str(listIpads)]),
            (0x33D7FF, 'getType', [str(getType)]),
            # 3rd row ----------
            (0x54FF04, 'Pair', [str(pair)]),
            (0x33D7FF, 'Update', [str(updateIpad)]),
            (0xD904FF, 'Profile', [str(instProf)]),
            # 4th row ----------

            (0xFF1304, 'Erase', [str(eraseIpad)]),
            (0x000000, '', []),
            (0xFF1304, 'STOP', [Keycode.CONTROL, 'c']),
            # Encoder button ---
            (0x000000, '', [Keycode.CONTROL, 'w']),  # Close window/tab
        ]
    }

class Jamf:
    cName = __class__.name
    order = macro_order.get(f"{cName}") 

    checkPolicy = "sudo jamf policy\n"
    removeMDM = "sudo jamf removemdmprofile\n"
    jamfRenew = "sudo profiles renew -type enrollment\n"

    app  = {                    
        'name' : 'Jamf MDM',
        'order' : order,
        'macros' : [           
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

class Zendesk:

    cName = __class__.name
    order = macro_order.get(f"{cName}") 
    zendesk  = {                    
        'name' : 'Zendesk',
        'order' : order,
        'macros' : [           
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

class Zoom:
    cName = __class__.name
    order = macro_order.get(f"{cName}")

    app = {
        'name' : 'Zoom',
        'order' : order,
        'macros' : [
            # COLOR    LABEL    KEY SEQUENCE
            # 1st row ----------
            (0x540908, 'Audio  ', [Keycode.COMMAND, Keycode.SHIFT, Keycode.A]),
            (0x544408, 'Screen ', [Keycode.COMMAND, Keycode.SHIFT, Keycode.S]),
            (0x04541B, 'Video  ', [Keycode.COMMAND, Keycode.SHIFT, Keycode.V]),
            # 2nd row ----------
            (0x000754, 'Control', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, Keycode.H]),
            (0x000000, '       ', []),
            (0x000754, 'Leave  ', [Keycode.COMMAND, Keycode.W]),
            # 3rd row ----------
            (0x000000, '       ', []),
            (0x095E06, 'Play/Pause', [Toolbar(ConsumerControlCode.PLAY_PAUSE)]),
            (0x000000, '       ', []),
            # 4th row ----------
            (0x080F54, 'Vol-   ', [Toolbar(ConsumerControlCode.VOLUME_DECREMENT)]),
            (0x000000, '       ', []),
            (0x080F54, 'Vol+   ', [Toolbar(ConsumerControlCode.VOLUME_INCREMENT)])
        ]
    }
