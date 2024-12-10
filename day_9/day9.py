def parse(): 
    file = open('day_9\\day_9_input.txt', 'r')
    data = ''.join(file.read().splitlines())

    return data

def make_str_with_dots(): 
    input = parse()
    s = []
    id = 0
    for index, char in enumerate(input): 
        if index % 2 == 0: 
            s.extend([str(id)] * int(char))
            id +=1 
        else: 
            s.extend(['.'] * int(char)) 
    
    return s

def move_blocks(): 
    s = make_str_with_dots()
    l = 0
    r = len(s) - 1

    while l < r: 
        while l <= r and s[l] != '.':
            l += 1
        while l <= r and s[r] == '.':
            r -= 1
        
        if l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    
    return s

def get_check_sum(): 
    blocks = move_blocks()
    check_sum = 0

    for index, block in enumerate(blocks):
        if block != '.':
            check_sum += index * int(block)
    
    return check_sum


