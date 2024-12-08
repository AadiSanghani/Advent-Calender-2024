def parse(): 
    file = open('day_7\\day_7_input.txt', 'r')
    data = file.read().splitlines()

    return data

def get_split_arr(d): 
    arr = d.split()

    for i in range(len(arr)): 
        if i == 0: 
            arr[i] = int(arr[i][i:-1])
        else: 
            arr[i] = int(arr[i])
    
    return arr

def run_recursive(target, arr, cur=0, i=0):
    if i == len(arr):
        return cur == target
    
    cur_sum = cur + arr[i]
    cur_mul = cur * arr[i] if cur != 0 else arr[i]  
    concat = int(str(cur) + str(arr[i])) if i != 0 else arr[i]
    
    return (run_recursive(target, arr, cur_sum, i + 1) or
            run_recursive(target, arr, cur_mul, i + 1) or
            run_recursive(target, arr, concat, i + 1))

def find_total_calibration():
    data = parse()
    total = 0
    for d in data: 
        arr = get_split_arr(d)

        if run_recursive(arr[0], arr[1:]): 
            total += arr[0]
    return total

print(find_total_calibration())