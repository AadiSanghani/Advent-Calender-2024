import re, collections

def parse(): 
    with open('day_14\\day_14_input.txt', 'r') as file:
        s = file.read().strip()
    
    return s

def find_robots():
    quads = [0, 0, 0, 0]
    input = parse()
    total = len(input.split('\n'))
    pattern = re.compile(r'-?\d+')
    
    for steps in range(1, 100000): 
        seen = set()
        for line in input.split('\n'): 
            
            x, y, vx, vy = pattern.findall(line)

            nx = (int(x) + steps * int(vx)) % 101
            ny = (int(y) + steps * int(vy)) % 103

            # if nx < 50 and ny < 51: 
            #     quads[0] += 1
            # elif nx > 50 and ny < 51: 
            #     quads[1] += 1
            # elif nx < 50 and ny > 51:
            #     quads[2] += 1
            # elif nx > 50 and ny > 51: 
            #     quads[3] += 1

            seen.add((nx, ny))
        
        if len(seen) == total:
            return steps

    
    # return quads[0] * quads[1] * quads[2] * quads[3]


print(find_robots())