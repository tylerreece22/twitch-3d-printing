import unittest

from lambdas.twitch_chat_message_processor import get_gcode_from_message


class TestGetGcodeFromMessage(unittest.TestCase):
    def test_gcode_returned_if_message_has_2_commands_with_lower(self):
        gcode = get_gcode_from_message("move from a1 to g8")
        self.assertEquals(gcode,['G92 E0',
                         'G1 X14.0625 Y14.0625 Z0.3 F3000',
                         'G1 E12 F300',
                         'G1 X182.8125 Y210.9375 F3000 E33.5997',
                         'G1 E27.5997 F2700',
                         'G1 X0 Y230.0 Z30'])

    def test_gcode_returned_if_message_has_2_commands_with_upper(self):
        gcode = get_gcode_from_message("MOVE FROM A1 TO G8")
        self.assertEquals(gcode,['G92 E0',
                                 'G1 X14.0625 Y14.0625 Z0.3 F3000',
                                 'G1 E12 F300',
                                 'G1 X182.8125 Y210.9375 F3000 E33.5997',
                                 'G1 E27.5997 F2700',
                                 'G1 X0 Y230.0 Z30'])

    def test_return_None_if_more_than_2_commands(self):
        gcode = get_gcode_from_message("move from a1 to g8 to d3")
        self.assertEquals(gcode, None)

    def test_return_None_if_less_than_2_commands(self):
        gcode = get_gcode_from_message("move to a1")
        self.assertEquals(gcode, None)

if __name__ == "__main__":
    unittest.main()
