import tkinter as tk
from PIL import Image, ImageTk

from pieces import Rook, Bishop, Knight, Pawn


class Chessboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chessboard")
        self.geometry("400x400")

        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()

        # Load images for all pieces
        self.images = {
            'b_rook': ImageTk.PhotoImage(Image.open('sprites/b.rook.png')),
            'b_knight': ImageTk.PhotoImage(Image.open('sprites/b.knight.png')),
            'b_bishop': ImageTk.PhotoImage(Image.open('sprites/b.bishop.png')),
            'b_queen': ImageTk.PhotoImage(Image.open('sprites/b.queen.png')),
            'b_king': ImageTk.PhotoImage(Image.open('sprites/b.king.png')),
            'b_pawn': ImageTk.PhotoImage(Image.open('sprites/b.pawn.png')),
            'w_rook': ImageTk.PhotoImage(Image.open('sprites/w.rook.png')),
            'w_knight': ImageTk.PhotoImage(Image.open('sprites/w.knight.png')),
            'w_bishop': ImageTk.PhotoImage(Image.open('sprites/w.bishop.png')),
            'w_queen': ImageTk.PhotoImage(Image.open('sprites/w.queen.png')),
            'w_king': ImageTk.PhotoImage(Image.open('sprites/w.king.png')),
            'w_pawn': ImageTk.PhotoImage(Image.open('sprites/w.pawn.png'))
        }

        for row in range(8):
            for col in range(8):
                x0 = col * 50
                y0 = row * 50
                color = "light grey" if (row + col) % 2 == 0 else "white"
                self.canvas.create_rectangle(x0, y0, x0+50, y0+50, fill=color)

        # Place all pieces
        self.place_pieces()
        self.create_data_board()

        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def place_pieces(self):
        # Place black pieces
        for col in range(8):
            self.canvas.create_image(col * 50 + 25, 1 * 50 + 25, image=self.images['b_pawn'])
        self.canvas.create_image(0 * 50 + 25,  25, image=self.images['b_rook'])
        self.canvas.create_image(7 * 50 + 25,  25, image=self.images['b_rook'])
        self.canvas.create_image(1 * 50 + 25,  25, image=self.images['b_knight'])
        self.canvas.create_image(6 * 50 + 25,  25, image=self.images['b_knight'])
        self.canvas.create_image(2 * 50 + 25,  25, image=self.images['b_bishop'])
        self.canvas.create_image(5 * 50 + 25,  25, image=self.images['b_bishop'])
        self.canvas.create_image(3 * 50 + 25,  25, image=self.images['b_queen'])
        self.canvas.create_image(4 * 50 + 25,  25, image=self.images['b_king'])

        # Place white pieces
        for col in range(8):
            self.canvas.create_image(col * 50 + 25, 6 * 50 + 25, image=self.images['w_pawn'])
        self.canvas.create_image(0 * 50 + 25, 7 * 50 + 25, image=self.images['w_rook'])
        self.canvas.create_image(7 * 50 + 25, 7 * 50 + 25, image=self.images['w_rook'])
        self.canvas.create_image(1 * 50 + 25, 7 * 50 + 25, image=self.images['w_knight'])
        self.canvas.create_image(6 * 50 + 25, 7 * 50 + 25, image=self.images['w_knight'])
        self.canvas.create_image(2 * 50 + 25, 7 * 50 + 25, image=self.images['w_bishop'])
        self.canvas.create_image(5 * 50 + 25, 7 * 50 + 25, image=self.images['w_bishop'])
        self.canvas.create_image(3 * 50 + 25, 7 * 50 + 25, image=self.images['w_queen'])
        self.canvas.create_image(4 * 50 + 25, 7 * 50 + 25, image=self.images['w_king'])


    def create_data_board(self):
        global board_data
        board_data = [[None for _ in range(8)] for _ in range(8)]
        board_data[0][0] = Rook("black")
        board_data[0][1] = Knight("black")
        board_data[0][2] = Bishop("black")
        # board_data[1][0] = Pawn("black")
        # board_data[0][2] = Bishop("black")
        # board_data[0][2] = Bishop("black")
        # board_data[0][2] = Bishop("black")
        # board_data[0][2] = Bishop("black")
        # board_data[0][2] = Bishop("black")

    def on_canvas_click(self, event):
        col = event.x // 50
        row = event.y // 50
        print(f"Clicked on square: Row {row}, Column {col}")
        print(str(type(board_data[row][col])))
        valids = board_data[row][col].valid_moves(board_data,row,col)
        print(valids)
        for x, y in valids:
            color = "light blue"
            self.canvas.create_rectangle(x*50, y*50, x*50 + 50, y*50 + 50, fill=color)


if __name__ == "__main__":
    app = Chessboard()
    app.mainloop()