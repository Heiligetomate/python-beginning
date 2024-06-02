import os


def print_board(chess_board):
    for i in chess_board:
        chess_row = ""
        for f in i:
            chess_row += f"{f} "
        print(chess_row)


board = [["1", "2", "3", "4", "5", "6", "7", "8"],
         ["1", "2", "3", "4", "5", "6", "7", "8"],
         ["1", "2", "3", "4", "5", "6", "7", "8"],
         ["1", "2", "3", "4", "5", "6", "7", "8"],
         ["1", "2", "3", "4", "5", "6", "7", "8"],
         ["1", "2", "3", "4", "5", "6", "7", "8"],
         ["1", "2", "3", "4", "5", "6", "7", "8"],
         ["1", "2", "3", "4", "5", "6", "7", "8"]]

roes_chars = {
    "a": board[0],
    "b": board[1],
    "c": board[2],
    "d": board[3],
    "e": board[4],
    "f": board[5],
    "g": board[6],
    "h": board[7],
}

cols = ["a", "b", "c", "d", "e", "f", "g", "h"]

while True:
    field_will_move = input("Which figure would you like to move? ")
    try:
        row = int(field_will_move[1]) - 1
        col = field_will_move[0]
        if 0 < row < 9 and col in cols:
            break
        print("NENE")
    except ValueError:
        print("NENE")

print_board(board)
roes_chars[col][row] = "X"
os.system("cls")
print_board(board)