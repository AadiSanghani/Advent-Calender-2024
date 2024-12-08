def parse():
    grid = []
    start = None
    row_i = 0
    col_i = 0
    with open('day_6\\day_6_input.txt', 'r') as file: 

        for line in file.readlines(): 
            line = line.strip()
            row = []
            col_i = 0
            for char in line: 
                char = char.strip()
                row.append(char)

                if char == '^':
                    start = (row_i, col_i)
                
                col_i += 1
        
            grid.append(row)
            row_i += 1
    
    return (grid, start)

def inside_grid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def move(): 
    grid, start = parse()

    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<':(0, -1)}
    count = 0
    cur_x, cur_y = start
    cur_dir = grid[cur_x][cur_y]
    print("start", start, "curdir", cur_dir)
    visited = set()

    while True: 
        new_x, new_y = cur_x + dirs[cur_dir][0], cur_y + dirs[cur_dir][1]

        if inside_grid(new_x, new_y, grid):
            if grid[new_x][new_y] == '#': 
                
                if cur_dir == '^': 
                    cur_dir = '>'
                elif cur_dir == '>':
                    cur_dir = 'v'
                elif cur_dir == 'v':
                    cur_dir = '<'
                elif cur_dir == '<':
                    cur_dir = '^'
                continue
            else: 
                cur_x = new_x
                cur_y = new_y
            
            if (cur_x,cur_y) not in visited: 
                count += 1
                visited.add((cur_x,cur_y))
        
        else:
            break
    
    return count
# ------------------- Part 2 -----------------
def is_cycle(grid, start):
    
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<':(0, -1)}
    
    cur_x, cur_y = start
    cur_dir = grid[cur_x][cur_y]
    
    visited = set()
    visited.add((cur_x, cur_y, cur_dir))
    
    while True: 
        new_x, new_y = cur_x + dirs[cur_dir][0], cur_y + dirs[cur_dir][1]

        if inside_grid(new_x, new_y, grid):
            if grid[new_x][new_y] == '#': 
                
                if cur_dir == '^': 
                    cur_dir = '>'
                elif cur_dir == '>':
                    cur_dir = 'v'
                elif cur_dir == 'v':
                    cur_dir = '<'
                elif cur_dir == '<':
                    cur_dir = '^'
                continue
            
            else: 
                cur_x = new_x
                cur_y = new_y
            
            if (cur_x,cur_y,cur_dir) in visited: 
                return True
        
            visited.add((cur_x,cur_y,cur_dir))
        
        else:
            return False
    
def find_number_of_loops():

    grid, start = parse()
    rows = len(grid)
    cols = len(grid[0])
    
    count = 0
    
    for r in range(rows):
        for c in range(cols): 
            if (r, c) == start or grid[r][c] == '#': 
                continue

            grid[r][c] = '#'

            if is_cycle(grid, start): 
                count += 1
            
            grid[r][c] = '.'
    
    return count

print(find_number_of_loops())