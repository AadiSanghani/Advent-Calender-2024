import collections
def parse():
    grid = []
    starting_points = []
    
    with open('day_10/day_10_input.txt', 'r') as file:
        for row_idx, line in enumerate(file):
            stripped_line = line.strip()
            row = []
            
            for col_idx, char in enumerate(stripped_line):
                value = int(char)
                row.append(value)
                
                if value == 0:
                    starting_points.append((row_idx, col_idx))
            
            grid.append(row)
    
    return grid, starting_points

grid = parse()[0]

def is_valid(x, y, visited): 
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited

def bfs(starting): 
    visited = set()
    q = collections.deque()
    q.append((starting[0], starting[1], 0))
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    count = 0

    while q: 
        cur_x, cur_y, cur_height = q.popleft()
        
        if cur_height == 9: 
            count += 1
            continue

        for x, y in dirs: 
            new_x, new_y = cur_x + x, cur_y + y

            if is_valid(new_x, new_y, visited) and grid[new_x][new_y] == cur_height + 1: 
                q.append((new_x, new_y, cur_height + 1))

                # uncomment this line for part 1 answer
                # visited.add((new_x, new_y))
    
    return count

def run_bfs(): 
    starting_points = parse()[1]
    count = 0

    # count += bfs(starting_points[0])

    for p in starting_points: 
        count += bfs(p)
    
    return count 

print(run_bfs())