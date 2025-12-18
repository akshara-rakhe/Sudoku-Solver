# Sudoku Solver using Backtracking in Python

This project implements a Sudoku solver using a recursive backtracking algorithm.
The solver fills a partially completed 9×9 Sudoku grid while satisfying all Sudoku
constraints.

Sudoku is a constraint satisfaction problem where:
- Each row must contain numbers 1 to 9 once
- Each column must contain numbers 1 to 9  once
- Each 3×3 subgrid must contain numbers 1 to 9  once

The objective is to fill empty cells which are represented by 0, while following all constraints.

# Approach

The solution uses recursive backtracking with following steps:

1. Find an empty cell in the grid
2. Try numbers from 1 to 9
3. Check if number placement is valid by:
   - Row constraint
   - Column constraint
   - 3×3 subgrid constraint
4. Recursively solve the remaining grid
5. Backtrack if a number leads to an invalid state
