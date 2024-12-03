def parse_input_part1():
    count = 0
    with open('day_2\day2_input.txt', 'r') as file: 
        
        for line in file.readlines():
            line = line.strip().split()
            is_increasing = False if int(line[0]) >= int(line[1]) else True
            flag = True

            
            for i in range(len(line) - 1): 
                if not (1 <= abs(int(line[i]) - int(line[i + 1])) <= 3): 
                    flag = False

                if is_increasing and int(line[i]) > int(line[i + 1]): 
                    flag = False
                elif not is_increasing and int(line[i]) < int(line[i + 1]): 
                    flag = False

            if flag: 
                count += 1
            

    return count

def is_safe(seq):
    if len(seq) < 2:
        return False 

    is_increasing = False if int(seq[0]) >= int(seq[1]) else True

    for i in range(len(seq) - 1):
        current_level = int(seq[i])
        next_level = int(seq[i + 1])
        diff = abs(current_level - next_level)

        if not (1 <= diff <= 3):
            return False

        if is_increasing and current_level > next_level:
            return False
        elif not is_increasing and current_level < next_level:
            return False

    return True

def parse_input_part2():
    count = 0
    with open('day_2\day2_input.txt', 'r') as file: 
        for line in file:
            line = line.strip().split()

            if is_safe(line):
                count += 1
                continue 

            safe = False
            for i in range(len(line)):

                new_line = line[:i] + line[i+1:]
                if len(new_line) < 2:
                    continue  
                if is_safe(new_line):
                    count += 1
                    safe = True
                    break  

    return count

print(parse_input_part2())