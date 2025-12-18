def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid(board, number, position):
    row = position[0]
    col = position[1]

    for r in range (9):
        if board[r][col] == number and r != row:
            return False
        
    for c in range (9):
        if board[row][c] == number and c != col:
            return False
            
    grid_row = (row//3)*3
    grid_col = (col//3)*3

    for r in range (grid_row, grid_row+3):
        for c in range (grid_col, grid_col+3):
            if board[r][c] == number and (r, c) != position:
                return False    
            
    return True        

def solve_sudoku(board):
    find = find_empty_cell(board)
    if not find :
        return True
    row, col = find
    for number in range (1, 10):
        if is_valid(board, number, (row, col)):
            board[row][col] = number

            if solve_sudoku(board) :
                return True
            board [row][col] = 0

    return False       

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if board[i][j] == 0:
                print(".", end=" ")
            else:
                print(board[i][j], end=" ")

        print()

def main() :
    
    board = [                                               #Add the input sudoku
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

    print("Sudoku before solving:\n")
    print_board(board)

    solve_sudoku(board)

    print("\nSudoku after solving:\n")
    print_board(board)    

if __name__ == "__main__":

    main()
