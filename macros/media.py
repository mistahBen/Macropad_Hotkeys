
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode
from consumer import Toolbar


app = {
    'name' : 'Media',
    'order' : 1,
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x27B1E0, 'Bright+', [[ConsumerControlCode.BRIGHTNESS_INCREMENT]]),
        (0x00FC04, 'ShwAll', [Keycode.CONTROL, Keycode.UP_ARROW]),
        (0xF1C309, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 2nd row ----------
        (0x27B1E0, 'Bright-', [[ConsumerControlCode.BRIGHTNESS_DECREMENT]]),
        (0x5EE860, 'Desktp', [Keycode.F11]),
        (0xF1C309, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        # 3rd row ----------
        (0xFC0400, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0x9229FC, '< WS', [Keycode.CONTROL, Keycode.LEFT_ARROW]),
        (0x9229FC, 'WS >', [Keycode.CONTROL, Keycode.RIGHT_ARROW]),
        # 4th row ----------
        (0x00FCF8, '<<', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
        (0xD8FE00, 'Play/Pause', [[ConsumerControlCode.PLAY_PAUSE]]),
        (0x00FCF8, '>>', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
