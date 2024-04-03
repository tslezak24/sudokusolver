from collections import defaultdict
class Solver: 
    def find_open_space(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    return (row, col)
        return None
        
    def solve(board):
        space = Solver.find_open_space(board)
        
        if space is None and Solver.verify_currently_valid(board):
            return True
        
        for i in range(1, 10):
            if Solver.verify_currently_valid(board):
                board[space[0]][space[1]] = f"{i}"
                
                if Solver.solve(board):
                    return True 
                
                board[space[0]][space[1]] = "."
        
        return False
        
    
    def verify_currently_valid(board):
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
       
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (
                    board[row][col] in rows[row]
                    or board[row][col] in cols[col]
                    or board[row][col] in squares[(row // 3, col // 3)]
                ):
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        
        return True