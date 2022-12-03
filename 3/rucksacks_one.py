from priorities import priorities

def run_one():
    rucksacks = read_file('rucksacks.txt')

    sum_rucksack = rucksack_sum(rucksacks)
    print(sum_rucksack)

def read_file(path):
    output = []

    with open(path) as file:
        for line in file:
            output.append(line.strip())

    return output

def split_compartment(compartment):
    half = len(compartment)//2
    return compartment[:half], compartment[half:]

def rucksack_sum(rucksack):
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
        

