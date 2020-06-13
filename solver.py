import random


def get_board():
    board = [[0, 0, 0, 0, 0, 7, 6, 5, 0],
             [0, 8, 0, 0, 0, 0, 4, 0, 0],
             [0, 0, 4, 0, 8, 0, 0, 0, 7],
             [0, 7, 9, 1, 0, 2, 0, 0, 0],
             [0, 0, 0, 0, 6, 0, 0, 2, 9],
             [1, 0, 0, 5, 9, 0, 0, 0, 0],
             [7, 2, 0, 0, 4, 9, 5, 0, 0],
             [0, 0, 0, 0, 0, 0, 2, 0, 6],
             [8, 9, 1, 0, 0, 0, 7, 0, 3]]
    return board



#  Work-in-progess: generating sudoku boards
# def get_board():
#     emptyBoard = [[] for i in range(9)]
#     for i in range(9):
#         emptyBoard[i] = [0 for i in range(9)]
#     counter = 0
#     # Fill blank grid with n numbers (1-9)
#     while counter <= 9:
#         i = random.randint(0, 8)
#         j = random.randint(0, 8)
#         x = random.randint(1, 9)
#         if valid(emptyBoard,x,(i, j)):
#             emptyBoard[i][j] = x
#             counter += 1
#     solve(emptyBoard)
#
#     return emptyBoard


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0]!= i:
            return False

    # Check box
    boxX = pos[1] // 3
    boxY = pos[0] // 3

    for i in range(boxY * 3, boxY*3+3):
        for j in range(boxX * 3, boxX * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len((bo)[0])):
            if bo[i][j] == 0:
                return i, j  #row, col (y,x)
    return None

print(get_board())


