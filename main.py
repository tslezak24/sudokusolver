from solver import verify_currently_valid, solve 
from webhandler import get_board, update_board

def main():
    board = get_board()
    if verify_currently_valid(board):
        if solve(board):
            formatted_print(board)
            if update_board(board):
                print("Your html output is ready.") 
        else:
            print("Unsolvable Board")

def formatted_print(board):
    for row in range(9):
        row_string = ""
        for col in range(9):
            if len(row_string) == 0:
                row_string += "|"
            row_string += board[row][col] + "|"
        print(row_string)
    
    
main()
