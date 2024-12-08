import collections

def parse_page_ordering(): 
    dict = collections.defaultdict(list)

    with open('day_5\\page_ordering.txt', 'r') as file: 
        for line in file.readlines():
            line = line.strip()
            left, right = line.split('|')
            dict[left.strip()].append(right.strip())
    
    return dict
# 47 has to come before ['53', '13', '61', '29']

def parse_page():
    dict = parse_page_ordering()
    mid_point_sum = 0
    with open('day_5\\page.txt', 'r') as file: 
        for line in file.readlines():
            arr = [a.strip() for a in line.split(',')]
            flag = True
            seen = set()
            for a in arr: 
                # 75,97,47,61,53
                # 97|75
                for element in dict[a]:
                    # print(a, element)
                    if element in seen:
                        flag = False
                        break
                # print(flag)
                if not flag: 
                    break
                seen.add(a)
            
            if flag: 
                midpoint = len(arr) // 2
                mid_point_sum += int(arr[midpoint])
    
    return mid_point_sum

# Incomplete
def parse_part_2():
    dict = parse_page_ordering()
    mid_point_sum = 0
    with open('Day_5/pages.txt', 'r') as file: 
        for line in file.readlines():
            arr = [a.strip() for a in line.split(',')]
            flag = True
            seen = {}
            for i, a in enumerate(arr): 
               
                for element in dict[a]:
                    # print(a, element)
                    # 75,97,47,61,53 -> 97,75,47,61,53
                    # 97,13,75,29,47 -> 97,75,47,29,13
                    if element in seen:
                        new_index = seen[element]
                        print(arr[seen[element]],arr[i] )
                        arr[new_index], arr[i] = arr[i], arr[new_index]
                        flag = False

                seen[a] = i
            
            if not flag: 
                print(arr)
                midpoint = len(arr) // 2
                mid_point_sum += int(arr[midpoint])
    
    return mid_point_sum

print(parse_page())