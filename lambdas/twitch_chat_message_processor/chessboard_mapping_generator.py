def generate_mappings():
    # Define the size of the chessboard square
    square_size = 28.125
    half_square = square_size / 2

    # Define columns and rows of the chessboard
    columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
    rows = ["1", "2", "3", "4", "5", "6", "7", "8"]

    # Create a mapping dictionary
    mapping = {}

    # Loop through each square and calculate the midpoint
    for col_idx, col in enumerate(columns):
        for row_idx, row in enumerate(rows):
            x = (col_idx * square_size) + half_square
            y = (row_idx * square_size) + half_square
            mapping[col + row] = (x, y)

    return mapping


chessboard_mapping = generate_mappings()
print(chessboard_mapping)
