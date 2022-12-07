def run():
    all_cal = read_file('../calorie_counter.txt')
    print(all_cal)

    largest_cal = get_largest_cal(all_cal)
    print(largest_cal)

    top_three = get_top_three(all_cal)
    print(top_three)

def read_file(path):
    output = []

    with open(path) as file:
        for line in file:
            output.append(line.strip())

    return output

def get_largest_cal(all_cal):
    calories = []
    total = 0

    for cal in all_cal:
        if not cal == '':
            total += int(cal)
        else:
            calories.append(total)
            total = 0
    
    return max(calories)

def get_top_three(all_cal):
    calories = []
    top_three = []
    total = 0

    for cal in all_cal:
        if not cal == '':
            total += int(cal)
        else:
            calories.append(total)
            total = 0
    
    for i in range(3):
        top_three.append(max(calories))
        calories.remove(max(calories))

    return sum(top_three)
