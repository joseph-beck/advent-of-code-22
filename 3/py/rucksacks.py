from priorities import priorities

def run():
    rucksacks = read_file('rucksacks.txt')

    rucksack_sum = sum_compartments(rucksacks)
    print(rucksack_sum)

    badge_sum = sum_badges(rucksacks)
    print(badge_sum)

def read_file(path):
    output = []

    with open(path) as file:
        for line in file:
            output.append(line.strip())

    return output

def split_compartment(compartment):
    half = len(compartment)//2
    return compartment[:half], compartment[half:]

def sum_compartments(rucksack):
    total = 0

    for compartment in rucksack:
        left_compartment, right_compartment = split_compartment(compartment)
        common_type = None

        for left_item in left_compartment:
            if not common_type == None:
                break
            for right_item in right_compartment:
                if right_item == left_item:
                    common_type = right_item
                    break
        
        total += priorities[common_type]

    return total
        
def sum_badges(rucksack):
    total = 0

    for i in range(0, len(rucksack), 3):
        comp_one = rucksack[i + 0]
        comp_two = rucksack[i + 1]
        comp_three = rucksack[i + 2]

        common_type = None
        
        for item_one in comp_one:
            if common_type is not None:
                break
            for item_two in comp_two:
                if common_type is not None:
                    break
                for item_three in comp_three:
                    if item_one == item_two and item_two == item_three:
                        common_type = item_one
                        break

        if common_type is not None:
            total += priorities[common_type]

    return total
