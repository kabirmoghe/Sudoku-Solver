# Visually Clean Puzzle Printer

def printer(puzzle):
     
    print('\n        SOLUTION: \n')
    print('╔══════╦══════╦══════╗')
    for x in range(9):
        if x % 3 == 0 and x != 0:
            print('╠══════╬══════╬══════╣')
            
        for y in range(9):
            if y % 3 == 0:
                print(" \b║", end ="")
            
            print(str(puzzle[x][y])+" ", end="")
        print("║")
    
    print('╚══════╩══════╩══════╝')


# Function iterates through the puzzle from left to right and then row by row to find an empty spot

def empty(puzzle):
    
    for x in range(9):
        for y in range(9):
            if puzzle[x][y] == 0:
                return x,y

# Function that checks if a certain number fits into a certain spot   
    
def works(puzzle, num, loc):
    
    # ROW
    
    row = puzzle[loc[0]]
    
    column = [row[loc[1]] for row in puzzle]
    
    r_box = loc[0] //3
    
    c_box = loc[1] //3
    
    if num in row:
        return False
    
    # COLUMN    

    if num in column:
        return False
    
    box = [row[3*c_box:3*c_box + 3] for row in puzzle[3*r_box:3*r_box + 3]]
    
    for row in box:
        if num in row:
            return False
            
    
    return True

# Function works recursively to solve the puzzle using the above functions

def solver(puzzle):
    
    empty_spot = empty(puzzle) # finds the first empty spot 
    
    if not empty_spot: # if the output from 'empty' is none, 
        return True # returns the puzzle as is, because it is solved
    else:
        row, column = empty_spot # otherwise, it creates two variables, row and column, from the empty spot
        
    for test_value in range(1,10): # tests values from 1-9 using a for loop
        if works(puzzle, test_value, (row, column)): # tests if the value fits in the row and column from the empty function
            puzzle[row][column] = test_value # if it does, then it sets the value of the empty spot to test_value
            
            if solver(puzzle): # if everything is done 
                return puzzle  # return the solved puzzle
            
            puzzle[row][column] = 0 # resets the value of the spot to empty if it doesn't work
                
    return False # if none of the values work, it returns False to backtrack

# function that puts everything together and creates a copy of the original input puzzle to avoid editing the original

def solve(puzzle):
    unsolved = [row[:] for row in puzzle]
    solution = solver(unsolved)
    
    return printer(solution)

# Example Sudoku Puzzles

sudoku1 = [
   
    [2,0,0,0,0,0,0,6,0],
    [0,0,0,0,7,5,0,3,0],
    [0,4,8,0,9,0,1,0,0],
    [0,0,0,3,0,0,0,0,0],
    [3,0,0,0,1,0,0,0,9],
    [0,0,0,0,0,8,0,0,0],
    [0,0,1,0,2,0,5,7,0],
    [0,8,0,7,3,0,0,0,0],
    [0,9,0,0,0,0,0,0,4]

]

sudoku2 = [
   
    [6,0,0,0,0,3,0,0,1],
    [0,9,0,0,0,0,0,0,3],
    [4,0,3,0,0,0,6,0,0],
    [0,0,0,5,9,0,2,0,6],
    [0,0,0,0,0,0,0,0,0],
    [0,0,7,0,0,0,0,0,4],
    [0,0,0,0,0,0,1,7,0],
    [0,0,2,0,0,8,0,0,0],
    [0,0,8,0,0,0,0,4,2]

]

sudoku3 = [
    
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]

]
