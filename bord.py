import tkinter as tk

from pieces import Rook, Knight, Bishop


def on_square_clicked(x, y):
    # Handle the logic when a square is clicked
    # Check if it's a valid move, move the piece, switch turns, etc.
    pass

# Initialize the board with pieces
board = [[None for _ in range(8)] for _ in range(8)]
# board[0][0] = Rook("black")
# board[0][1] = Knight("black")
# ... Initialize the rest of the board

# Tkinter GUI code to create the board and bind click events
# ...





def create_board(window, board_data):
    board_frame = tk.Frame(window)
    colors = ["white", "gray"]

    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            square = tk.Frame(board_frame, bg=color, width=60, height=60)
            square.grid(row=row, column=col)

            piece = board_data[row][col]
            if piece is not None:
                label = tk.Label(square, image=piece.image)
                label.pack()

    board_frame.pack()

def main():
    window = tk.Tk()
    window.title("Chess Game")

    # Initialize the board with pieces
    board_data = [[None for _ in range(8)] for _ in range(8)]
    board_data[0][0] = Rook("black")
    # board_data[0][1] = Knight("black")
    board_data[0][2] = Bishop("black")
    # board_data[0][2] = Bishop("black")
    # board_data[0][2] = Bishop("black")
    # board_data[0][2] = Bishop("black")
    # board_data[0][2] = Bishop("black")
    # board_data[0][2] = Bishop("black")
    # board_data[0][2] = Bishop("black")
    create_board(window, board_data)
    window.mainloop()

if __name__ == "__main__":
    main()
