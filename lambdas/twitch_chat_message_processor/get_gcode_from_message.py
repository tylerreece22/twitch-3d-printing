command_to_chessboard_map = {
    "A1": (14.0625, 14.0625),
    "A2": (14.0625, 42.1875),
    "A3": (14.0625, 70.3125),
    "A4": (14.0625, 98.4375),
    "A5": (14.0625, 126.5625),
    "A6": (14.0625, 154.6875),
    "A7": (14.0625, 182.8125),
    "A8": (14.0625, 210.9375),
    "B1": (42.1875, 14.0625),
    "B2": (42.1875, 42.1875),
    "B3": (42.1875, 70.3125),
    "B4": (42.1875, 98.4375),
    "B5": (42.1875, 126.5625),
    "B6": (42.1875, 154.6875),
    "B7": (42.1875, 182.8125),
    "B8": (42.1875, 210.9375),
    "C1": (70.3125, 14.0625),
    "C2": (70.3125, 42.1875),
    "C3": (70.3125, 70.3125),
    "C4": (70.3125, 98.4375),
    "C5": (70.3125, 126.5625),
    "C6": (70.3125, 154.6875),
    "C7": (70.3125, 182.8125),
    "C8": (70.3125, 210.9375),
    "D1": (98.4375, 14.0625),
    "D2": (98.4375, 42.1875),
    "D3": (98.4375, 70.3125),
    "D4": (98.4375, 98.4375),
    "D5": (98.4375, 126.5625),
    "D6": (98.4375, 154.6875),
    "D7": (98.4375, 182.8125),
    "D8": (98.4375, 210.9375),
    "E1": (126.5625, 14.0625),
    "E2": (126.5625, 42.1875),
    "E3": (126.5625, 70.3125),
    "E4": (126.5625, 98.4375),
    "E5": (126.5625, 126.5625),
    "E6": (126.5625, 154.6875),
    "E7": (126.5625, 182.8125),
    "E8": (126.5625, 210.9375),
    "F1": (154.6875, 14.0625),
    "F2": (154.6875, 42.1875),
    "F3": (154.6875, 70.3125),
    "F4": (154.6875, 98.4375),
    "F5": (154.6875, 126.5625),
    "F6": (154.6875, 154.6875),
    "F7": (154.6875, 182.8125),
    "F8": (154.6875, 210.9375),
    "G1": (182.8125, 14.0625),
    "G2": (182.8125, 42.1875),
    "G3": (182.8125, 70.3125),
    "G4": (182.8125, 98.4375),
    "G5": (182.8125, 126.5625),
    "G6": (182.8125, 154.6875),
    "G7": (182.8125, 182.8125),
    "G8": (182.8125, 210.9375),
    "H1": (210.9375, 14.0625),
    "H2": (210.9375, 42.1875),
    "H3": (210.9375, 70.3125),
    "H4": (210.9375, 98.4375),
    "H5": (210.9375, 126.5625),
    "H6": (210.9375, 154.6875),
    "H7": (210.9375, 182.8125),
    "H8": (210.9375, 210.9375),
}
command_list = command_to_chessboard_map.keys()

import math

# scaling factor
scale_factor = 0.0833
retraction = 6
prepare_extrusion = 12


def get_gcode_from_message(message: str):
    # Extracting keys present in the message
    keys_in_message = [key for key in command_list if key in message.upper()]

    # If less than 2 keys, ignore the message
    if len(keys_in_message) != 2:
        return None

    # Calculate positions and distance
    start_x, start_y = command_to_chessboard_map[keys_in_message[0]]
    end_x, end_y = command_to_chessboard_map[keys_in_message[1]]

    distance = math.sqrt((end_x - start_x) ** 2 + (end_y - start_y) ** 2)

    # Calculate E value based on the distance
    E_value = distance * scale_factor + prepare_extrusion

    gcode_commands = [
        f"G92 E0",  # First extruder reset
        f"G1 X{start_x:.4f} Y{start_y:.4f} Z0.3 F3000",  # Move to start position
        f"G1 E{prepare_extrusion} F300",  # Move filament to position
        f"G1 X{end_x:.4f} Y{end_y:.4f} F3000 E{E_value:.4f}",  # Draw the line to the end position
        f"G1 E{E_value - retraction:.4f} F2700",  # Retract before move
        f"G1 X0 Y230.0 Z30",  # Move to rest position
    ]

    # Not sure if i want string yet
    # Return G-code commands
    # gcode_commands = f"G92 E0\n"  # First extruder reset
    # gcode_commands += (
    #     f"G1 X{start_x:.4f} Y{start_y:.4f} Z0.3 F3000\n"  # Move to start position
    # )
    # gcode_commands += f"G1 E{prepare_extrusion} F300\n"  # Move filament to position
    # gcode_commands += f"G1 X{end_x:.4f} Y{end_y:.4f} F3000 E{E_value:.4f}\n"  # Draw the line to the end position
    # gcode_commands += f"G1 E{E_value - retraction:.4f} F2700\n"  # Retract before move
    # gcode_commands += f"G1 X0 Y230.0 Z30"  # Move to rest position

    return gcode_commands
