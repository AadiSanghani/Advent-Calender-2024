import collections
import math

def parse_file_to_grid():
    with open('day_8\\day_8_input.txt') as file: 
        data = file.read().splitlines()
        grid = [list(line) for line in data]
    
    return grid

def get_locations(grid): 
    hmap = collections.defaultdict(list)
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows): 
        for c in range(cols): 
            if grid[r][c] != '.': 
                hmap[grid[r][c]].append((r, c))
    
    return hmap

def find_antinodes():
    grid = parse_file_to_grid()
    rows = len(grid)
    cols = len(grid[0])
    antennas_by_freq = get_locations(grid)

    antinode_positions = set()

    for _, positions in antennas_by_freq.items():
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                r1, c1 = positions[i]
                r2, c2 = positions[j]

                p1r = 2*r1 - r2
                p1c = 2*c1 - c2

                p2r = 2*r2 - r1
                p2c = 2*c2 - c1

                if 0 <= p1r < rows and 0 <= p1c < cols:
                    antinode_positions.add((p1r, p1c))

                if 0 <= p2r < rows and 0 <= p2c < cols:
                    antinode_positions.add((p2r, p2c))

    return antinode_positions

def find_antinodes_part_two():
    grid = parse_file_to_grid()
    rows = len(grid)
    cols = len(grid[0])
    antennas_by_freq = get_locations(grid)

    antinode_positions = set()

    for _, positions in antennas_by_freq.items():
        if len(positions) < 2:
            continue

        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                r1, c1 = positions[i]
                r2, c2 = positions[j]

                dr = r2 - r1
                dc = c2 - c1

                g = math.gcd(dr, dc)
                step_r = dr // g
                step_c = dc // g

                rr, cc = r1, c1

                while 0 <= rr < rows and 0 <= cc < cols:
                    antinode_positions.add((rr, cc))
                    rr += step_r
                    cc += step_c

                rr, cc = r1, c1
                while 0 <= rr < rows and 0 <= cc < cols:
                    antinode_positions.add((rr, cc))
                    rr -= step_r
                    cc -= step_c

    return antinode_positions

print(len(find_antinodes_part_two()))