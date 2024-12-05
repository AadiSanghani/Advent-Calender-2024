def parse():
    grid = [] 
    with open('day_4\day_4_input.txt', 'r') as file:
        

        for sentence in file.readlines():
            sentence = sentence.strip()
            row = []

            for char in sentence: 
                row.append(char)
        
            grid.append(row)
    
    return grid

def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) 

# XMAS
def part_1(): 
    grid = parse()
    count = 0

    UP = [(0, 0), (0, 1), (0, 2), (0, 3)]
    DOWN = [(0, 0), (0, -1), (0, -2), (0, -3)]
    RIGHT = [(0, 0), (1, 0), (2, 0), (3, 0)]
    LEFT = [(0, 0), (-1, 0), (-2, 0), (-3, 0)]
    UP_RIGHT = [(0, 0), (1, 1), (2, 2), (3, 3)]
    UP_LEFT = [(0, 0), (-1, 1), (-2, 2), (-3, 3)]
    DOWN_RIGHT = [(0, 0), (1, -1), (2, -2), (3, -3)]
    DOWN_LEFT = [(0, 0), (-1, -1), (-2, -2), (-3, -3)]

    dirs = [UP, DOWN, RIGHT, LEFT, UP_RIGHT, UP_LEFT, DOWN_LEFT, DOWN_RIGHT]

    ROWS = len(grid)
    COLS = len(grid[0])

    for r in range(ROWS): 
        for c in range(COLS): 
            if grid[r][c] == 'X': 
                
                for dir in dirs: 
                    
                    cur_str = ""
                    for x, y in dir: 
                        if is_valid(x + r, y + c, grid):
                            cur_str += grid[x + r][y + c]
                        else:
                            break
                    
                    if cur_str == "XMAS": 
                        count += 1
    
    return count

def part_2(): 
    grid = parse()
    x_shape = [(0, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
    words = ["ASMSM", "AMSMS", "AMSSM", "ASMMS"]
    ROWS = len(grid)
    COLS = len(grid[0])
    count = 0
    for r in range(ROWS): 
        for c in range(COLS): 
            if grid[r][c] == "A": 
                
                cur_str = ""
                for x, y in x_shape: 
                    if is_valid(r + x, c + y, grid): 
                        cur_str += grid[r + x][c + y]
                    else: 
                        break
                
                if cur_str in words: 
                    count += 1
    
    return count

print(part_2())



