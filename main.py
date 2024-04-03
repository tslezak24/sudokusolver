from solver import verify_currently_valid, solve 
def main():
    board = [[""]*9]*9
    board = [
        [".", ".", "8", "1", ".", ".", "5", ".", "."],
        ["7", ".", ".", "9", ".", ".", ".", ".", "."],
        [".", ".", "4", ".", "5", "7", ".", "6", "."],
        ["2", ".", ".", ".", "4", "5", "8", ".", "."],
        [".", "8", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", ".", "1", ".", ".", ".", "."],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        ["4", ".", ".", ".", "8", "2", "9", ".", "."],
        [".", ".", "6", ".", ".", ".", ".", ".", "3"]
        ]
    if verify_currently_valid(board):
        if solve(board):
            formatted_print(board)
        else:
            print("Unsolvable Board")
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
