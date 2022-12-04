def run():
    assignments = read_file_edited('assignments.txt')

    overlaps = calculate_overlap(assignments)
    print(overlaps)

    pair_overlaps = calculate_overlap_pairs(assignments)
    print(pair_overlaps)

def read_file(path):
    output = []

    with open(path) as file:
        for line in file:
            output.append(line.strip())

    return output

def read_file_edited(path):
    with open(path, 'r') as file:
        data = file.read().strip()

    output = data.split('\n')
    return output
    
def calculate_overlap(assignments):
    overlaps = 0

    for item in assignments:
        item_one, item_two = item.split(',')
        start_one, end_one = map(int, item_one.split('-'))
        start_two, end_two = map(int, item_two.split('-'))
        
        if start_one <= start_two and end_two <= end_one or start_two <= start_one and end_one <= end_two:
            overlaps += 1

    return overlaps

def calculate_overlap_pairs(assignments):
    overlaps = 0

    for item in assignments:
        item_one, item_two = item.split(',')
        start_one, end_one = map(int, item_one.split('-'))
        start_two, end_two = map(int, item_two.split('-'))
        
        if end_one >= start_two and start_one <= end_two:
            overlaps += 1

    return overlaps