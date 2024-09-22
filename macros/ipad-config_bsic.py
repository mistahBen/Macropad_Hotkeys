from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values


def spotlight_search(search):
    """Case sensitive"""

    _keys = [Keycode.COMMAND, Keycode.SPACE, 0.2, f"{search}", 0.2, Keycode.RETURN]
    return _keys


app = {  # REQUIRED dict, must be named 'app'
    "name": "iPad Controls",  # Application name
    "order": 2,
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x54FF04, ">>Setngs", spotlight_search("Settings")),
        (0x000000, ">Drive", spotlight_search("Google drive")),
        (0x33D7FF, "[TAB]", [Keycode.TAB]),
        # 2nd row ----------
        (0x33D7FF, "Clever", spotlight_search("Clever")),
        (0x33D7FF, "", []),
        (0x33D7FF, "[RETURN]", [Keycode.RETURN]),
        # 3rd row ----------
        (0x54FF04, "", []),
        (0x33D7FF, "", []),
        (0xD904FF, "", []),
        # 4th row ----------
        (0xFF1304, "", []),
        (0x000000, "", []),
        (0xFF1304, "", []),
        # Encoder button ---
        (0x000000, "", []),  # Close window/tab
    ],
}
# strings for commands
cfg = "cfgutil "  # note the trailing space
allIpads = cfg + " -f "  #  applies to all attached devices
getSerial = "get serialNumber | pbcopy && echo $(pbpaste)\n"
updateIpad = "update\n"
eraseIpad = "erase\n"
instProf = "bash /Users/alexanderb/Documents/scripting/ipad_utilities/wifi_dep.sh\n"  #  does NOT require a cfgutil command!
pair = "pair\n"
listIpads = "list\n"
getType = "get deviceType\n"
# app = {                    # REQUIRED dict, must be named 'app'
#     'name' : 'iPad Controls',  # Application name
#     'order' : 2,
#     'macros' : [           # List of button macros...
#         # COLOR    LABEL    KEY SEQUENCE
#         # 1st row ----------
#         (0x54FF04, '[Single]', [str(cfg)]),
#         (0xF0FF04, '[All]', [str(allIpads)]),
#         (0x000000, '', []),
#         # 2nd row ----------
#         (0x33D7FF, 'Serial#', [str(getSerial)]),
#         (0x33D7FF, 'List', [str(listIpads)]),
#         (0x33D7FF, 'getType', [str(getType)]),
#         # 3rd row ----------
#         (0x54FF04, 'Pair', [str(pair)]),
#         (0x33D7FF, 'Update', [str(updateIpad)]),
#         (0xD904FF, 'Profile', [str(instProf)]),
#         # 4th row ----------
#
#         (0xFF1304, 'Erase', [str(eraseIpad)]),
#         (0x000000, '', []),
#         (0xFF1304, 'STOP', [Keycode.CONTROL, 'c']),
#         # Encoder button ---
#         (0x000000, '', [Keycode.CONTROL, 'w']),  # Close window/tab
#     ]
# }
