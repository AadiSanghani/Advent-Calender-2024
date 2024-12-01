import collections

list1, list2 = [], []
def parse_data():
    with open('day1_input.csv', 'r') as file: 
        flag = False
        for line in file.readlines(): 
            if not flag:
                flag = True 
                continue

            row = line.split()
            list1.append(int(row[0]))
            list2.append(int(row[1]))
    
    list1.sort()
    list2.sort()

def get_distance(): 
    distance = 0
    for a, b in zip(list1, list2): 
        distance += abs(abs(a) - abs(b))
    
    return distance

def get_similiarty_score(): 
    count = collections.Counter(list2)
    score = 0

    for n in list1:
        score += n * count[n]

    return score  


def main(): 
    parse_data()
    print(get_distance())
    print(get_similiarty_score())

main()