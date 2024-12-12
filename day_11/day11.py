import collections

file = open('day_11/day_11_input.txt', 'r')
data_from_file = file.read().split()

data_hmap = collections.defaultdict(int)
for d in data_from_file: 
    data_hmap[d] += 1

def get_sol(): 
    global data_hmap
    total = 0
    for inter in range(25): 
        temp_data_map = collections.defaultdict(int)

        for num, count in data_hmap.items(): 
            if num == '0': 
                temp_data_map['1'] += count
            elif len(num) % 2 == 0:
                mid = len(num) // 2
                left = str(int(num[:mid]))
                right = str(int(num[mid:]))
                temp_data_map[left] += count
                temp_data_map[right] += count
            else: 
                num = int(num)
                new_num = str(num * 2024)
                temp_data_map[new_num] += count
        
        data_hmap = temp_data_map
        print(f"Cur interations {inter} and curr num arr {sum(data_hmap.values())}")

get_sol()