import tkinter as tk
from PIL import Image, ImageTk


class ChessPiece:
    # Base class for chess pieces
    def __init__(self, color):
        self.color = color

    def valid_moves(self, board, x, y):
        # Override in subclasses to return valid moves from position (x, y)
        pass

    def __str__(self):
        return self.color + " " + str(type(self))


class Pawn(ChessPiece):
    def valid_moves(self, board, x, y):
        # Implement pawn-specific logic
        pass

# Similarly, create classes for Rook, Knight, Bishop, Queen, King

class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        super().__init__(color)
        image_path = 'sprites/b.pawn.png'  # Use the correct path for the bishop image
        image = Image.open(image_path)
        self.image = ImageTk.PhotoImage(image)


    def valid_moves(self, board, x, y):
        direction = 1 if self.color == "white" else -1
        start_row = 1 if self.color == "white" else 6
        valid_moves = []

        # Forward move
        if board[x + direction][y] is None:
            valid_moves.append((x + direction, y))
            # Double move on first move
            if x == start_row and board[x + 2 * direction][y] is None:
                valid_moves.append((x + 2 * direction, y))

        # Diagonal captures
        for dy in [-1, 1]:
            if 0 <= y + dy < 8 and board[x + direction][y + dy] is not None:
                if board[x + direction][y + dy].color != self.color:
                    valid_moves.append((x + direction, y + dy))

        return valid_moves



class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        super().__init__(color)
        image_path = 'sprites/b.knight.png'  # Use the correct path for the bishop image
        image = Image.open(image_path)
        self.image = ImageTk.PhotoImage(image)

    def valid_moves(self, board, x, y):
        # Generate potential moves for the knight
        potential_moves = [
            (x + 2, y + 1), (x + 2, y - 1),
            (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2),
            (x - 1, y + 2), (x - 1, y - 2)
        ]

        # Filter out moves that are off the board or occupied by a piece of the same color
        valid_moves = []
        for move in potential_moves:
            mx, my = move
            if 0 <= mx < 8 and 0 <= my < 8:
                target_square = board[mx][my]
                if target_square is None or target_square.color != self.color:
                    valid_moves.append(move)

        return valid_moves


class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        super().__init__(color)
        image_path = 'sprites/b.rook.png'  # Use the correct path for the bishop image
        image = Image.open(image_path)
        self.image = ImageTk.PhotoImage(image)

    def valid_moves(self, board, x, y):
        valid_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in directions:
            mx, my = x, y
            while True:
                mx, my = mx + dx, my + dy
                if 0 <= mx < 8 and 0 <= my < 8:
                    target_square = board[mx][my]
                    if target_square is None:
                        valid_moves.append((mx, my))
                    elif target_square.color != self.color:
                        valid_moves.append((mx, my))
                        break
                    else:
                        break
                else:
                    break

        return valid_moves


class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        super().__init__(color)
        image_path = 'sprites/b.bishop0.png'  # Use the correct path for the bishop image
        image = Image.open(image_path)
        self.image = ImageTk.PhotoImage(image)

    def valid_moves(self, board, x, y):
        valid_moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            mx, my = x, y
            while True:
                mx, my = mx + dx, my + dy
                if 0 <= mx < 8 and 0 <= my < 8:
                    target_square = board[mx][my]
                    if target_square is None:
                        valid_moves.append((mx, my))
                    elif target_square.color != self.color:
                        valid_moves.append((mx, my))
                        break
                    else:
                        break
                else:
                    break

        return valid_moves


class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        super().__init__(color)
        image_path = 'sprites/b.queen.png'  # Use the correct path for the bishop image
        image = Image.open(image_path)
        self.image = ImageTk.PhotoImage(image)


    def valid_moves(self, board, x, y):
        # Combines the logic of rook and bishop
        return Rook(self.color).valid_moves(board, x, y) + Bishop(self.color).valid_moves(board, x, y)


class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        super().__init__(color)
        image_path = 'sprites/b.king.png'  # Use the correct path for the bishop image
        image = Image.open(image_path)
        self.image = ImageTk.PhotoImage(image)

    def valid_moves(self, board, x, y):
        valid_moves = []
        directions = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]

        for dx, dy in directions:
            mx, my = x + dx, y + dy
            if 0 <= mx < 8 and 0 <= my < 8:
                target_square = board[mx][my]
                if target_square is None or target_square.color != self.color:
                    valid_moves.append((mx, my))

        return valid_moves

