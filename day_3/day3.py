import re

def part1(): 
    muls = []
    with open('day_3\day_3_input.txt', 'r') as f: 

        for line in f.readlines(): 
            line = line.strip()
            line_muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)

            muls.append(line_muls)
    return muls

def flatten_array(): 
    arr = part1()
    output = []

    for element in arr: 
        for e in element: 
            output.append(e)

    return output

def parse_mul_to_digits(): 
    regex = r'\d+'
    output = []
    arr = flatten_array()
    
    for a in arr: 
        
        if a == 'don\'t()' or a == 'do()':
            output.append((a, "dummy"))
        
        else: 
            digits = re.findall(regex, a)
            output.append(digits)
    
    return output

def find_real_mul(): 
    digits = parse_mul_to_digits()
    ans = 0
    flag = True
    
    for a, b in digits:
        if a == 'don\'t()':
            flag = False
        
        elif a == 'do()':
            flag = True
        
        elif flag:
            ans += int(a) * int(b)

    return ans

print(find_real_mul())
