def create_grid(rows, cols):
    return [[0 for _ in range(cols)]  for _ in range(rows)]

def add_column(new_col, grid):
    if len(new_col) == len(grid):
        for i in range(len(grid)):
            grid[i].append(new_col[i])
        
def add_row(new_row, grid):
    if len(new_row) == len(grid[0]):
        grid.append(new_row)
            
def sum_grid(grid):
    total_sum = 0
    for row in grid:
        total_sum += sum(row)
    return total_sum

def display_grid(grid):
    for row in grid:
        print(row)
        
        
grid = create_grid(3, 3)
print(grid)
add_row([2,2,2], grid)  
add_column([1,1,1], grid)
print(sum_grid(grid))

display_grid(grid)