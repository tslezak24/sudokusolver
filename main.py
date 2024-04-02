from solver import Solver
def main():
    board = [[""]*9]*9
    board = [
        [".", "6", ".", "8", ".", ".", "5", ".", "."],
        [".", ".", "5", ".", ".", ".", "3", "6", "7"],
        ["3", "7", ".", ".", "6", "5", "8", ".", "9"],
        ["6", ".", "9", ".", ".", "2", "1", ".", "."],
        [".", ".", "1", "4", "8", "9", "2", ".", "."],
        [".", ".", ".", "3", ".", "6", "9", ".", "."],
        [".", "5", ".", ".", ".", ".", "4", ".", "."],
        [".", "1", ".", "5", "4", "7", ".", ".", "3"],
        [".", "9", "6", ".", "3", "8", ".", "5", "1"]
        ]
    solved_board = Solver.solve(board)
    formatted_print(solved_board)
#    for row in range(9):
#        for col in range(9):
#            board[row][col] = input(f"Please enter number for position ({row}, {col})")

def formatted_print(board):
    for row in range(9):
        row_string = ""
        for col in range(9):
            if len(row_string) == 0:
                row_string += "|"
            row_string += board[row][col] + "|"
        print(row_string)
    
    
main()
