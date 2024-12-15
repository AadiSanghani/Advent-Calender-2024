def make_grid(s): 
    grid = []
    for line in s.split('\n'): 
        grid.append(list(line))
    return grid

def parse():
    with open('day_15\\day_15_input.txt', 'r') as file: 
        grid, moves = file.read().strip().split("\n\n")
    
    return make_grid(grid), moves

def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'


def find_start(grid):
    for i in range(len(grid)): 
        for j in range(len(grid[0])):
            if grid[i][j]=='@':
                return i, j 

def pretty_print(grid):
    for row in grid:
        print(' '.join(row))

def find_gps(grid): 
    total = 0
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            if grid[i][j] == 'O':
                total += 100 * i + j
    
    return total


def run_simulation(): 
    grid, moves = parse()
    directions = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}

    cx, cy = find_start(grid)  

    for move in moves.replace('\n', ''):
        dx, dy = directions[move]
        new_x, new_y = cx + dx, cy + dy

        if is_valid(new_x, new_y, grid):
            if grid[new_x][new_y] == '.':
                grid[cx][cy] = '.'
                grid[new_x][new_y] = '@'
                cx, cy = new_x, new_y

            elif grid[new_x][new_y] == 'O':
                box_positions = [(new_x, new_y)]
                box_x, box_y = new_x, new_y
                
                while True:
                    next_x, next_y = box_x + dx, box_y + dy
                    if not is_valid(next_x, next_y, grid) or grid[next_x][next_y] in ('#', '@'):
                        break  

                    if grid[next_x][next_y] == '.':
                        
                        for bx, by in reversed(box_positions):
                            grid[next_x][next_y] = 'O'
                            grid[bx][by] = '.'
                            next_x, next_y = bx, by
                        
                        # Move robot into position
                        grid[cx][cy] = '.'
                        grid[new_x][new_y] = '@'
                        cx, cy = new_x, new_y
                        break
                    
                    elif grid[next_x][next_y] == 'O':
                        
                        box_positions.append((next_x, next_y))
                        box_x, box_y = next_x, next_y

    
    return find_gps(grid)

print(run_simulation())
