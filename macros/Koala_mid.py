# Koala MIDI controller
# from adafruit_macropad import MacroPad
from adafruit_macropad import MacroPad
# from adafruit_midi import Midi
# from rainbowio import colorwheel

# CC_NUM = 10
#
#
# midi_pads = ["n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n9", "n10", "n11", "n12"]
#
# midi_notes = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
#
# note_dict = dict(zip(list(reversed(midi_pads)), list(reversed(midi_notes))))
# # lists are reversed because pads are mapped from top left to bottom right
# macropad = MacroPad()  # create the macropad object, rotate orientation
# macropad.display.auto_refresh = False
#
# app = {
#     "name": "Koala Kontrol",
#     "order": 10,
#     "macros": [],
# }
#
# for k, v in note_dict.values():
#     note = Midi.press(v, macropad)
#     app["macros"].append((0x540908, f"{k}", note, 120))
#
# while True:
#     while macropad.keys.events:  # check for key press or release
#         key_event = macropad.keys.events.get()
#         if key_event:
#             if key_event.pressed:
#                 key = key_event.key_number
#                 macropad.midi.send(
#                     macropad.NoteOn(midi_notes[key], 120)
#                 )  # send midi noteon
#                 macropad.pixels[key] = colorwheel(90)  # light up green
#                 text_lines[1].text = "NoteOn:{}".format(midi_notes[key])
#
#             if key_event.released:
#                 key = key_event.key_number
#                 macropad.midi.send(macropad.NoteOff(midi_notes[key], 0))
#                 macropad.pixels[
#                     key
#                 ] = key_color  # return to color set by encoder bank value
#                 text_lines[1].text = "NoteOff:{}".format(midi_notes[key])
#
#     macropad.encoder_switch_debounced.update()  # check the knob switch for press or release
#     if macropad.encoder_switch_debounced.pressed:
#         mode = (mode + 1) % 3
#         if mode == 0:
#             text_lines[0].text = "Mode: %s %d" % (
#                 mode_text[mode],
#                 midi_values[mode] + 1,
#             )
#         elif mode == 1:
#             text_lines[0].text = "Mode: %s %d" % (
#                 mode_text[mode],
#                 int(midi_values[mode] * 4.1),
#             )
#         else:
#             text_lines[0].text = "Mode: %s %d" % (
#                 mode_text[mode],
#                 midi_values[mode] - 8,
#             )
#         macropad.red_led = macropad.encoder_switch
#         text_lines[1].text = " "  # clear the note line
#
#     if macropad.encoder_switch_debounced.released:
#         macropad.red_led = macropad.encoder_switch
#
# ### OLD Macros list
# # # 1st row ----------
# # (0x540908, "Welcome", [Keycode.SPACE, 2]),
# # (0x544408, "ENRL", ["enroll", 1, Keycode.ENTER]),
# # (0x04541B, "Agree", [Keycode.SPACE]),
# # # (0x04541B, 'Agree', [Keycode.ALT, Keycode.V, -Keycode.ALT]),
# # # # 2nd row ----------
# # (0x000754, "S_Out*2", [Keycode.CONTROL, Keycode.SHIFT, Keycode.Q]),
# # (
# #     0x000754,
# #     " rmAcct",
# #     [
# #         Keycode.TAB,
# #         0.2,
# #         -Keycode.TAB,
# #         0.1,
# #         Keycode.ENTER,
# #         0.3,
# #         -Keycode.ENTER,
# #         0.3,
# #         Keycode.ENTER,
# #     ],
# # ),
# # (0x000754, "Close", [Keycode.CONTROL, "w"]),
# # # # 3rd row ----------
# # (0x095E06, "STwifi", ["A8wRdCXf2kN)Dy7Z\n"]),
# # BLANK,
# # (0x095E06, "hotspot", ["0987654321\n"]),
# # # # 4th row ----------
# # (0x080F54, "", []),
# # (0x540908, "[ENTER]", [Keycode.RETURN]),
# # (0x080F54, "Wspot", ["12345678\n"]),
# # # # Encoder button ---
# # # (0x544408, '', [])
