import copy

from stacks import stacks

def run():
    file_data = read_file('supply_stacks.txt')

    print(sort_stacks(file_data))
    print(rearrangement(file_data))

def read_file(path):
    with open(path) as file:
        return file.read().strip().split('\n')

def make_output(stack):
    output = ''

    for item in stack:
        output += item[0]

    return output

def sort_stacks(sorting_data):
    stack = copy.deepcopy(stacks)

    for line in sorting_data:
        instructions = line.split(' ')
        quantity, origin, destination = int(instructions[1]), int(instructions[3]) - 1, int(instructions[5]) - 1

        for _ in range(quantity):
            stack[destination].insert(0, stack[origin].pop(0))
            

    return make_output(stack)

def rearrangement(sorting_data):
    stack = copy.deepcopy(stacks)

    for line in sorting_data:
        instructions = line.split(' ')
        quantity, origin, destination = int(instructions[1]), int(instructions[3]) - 1, int(instructions[5]) - 1

        for item in reversed(range(quantity)):
            stack[destination].insert(0, stack[origin].pop(item))
            
    return make_output(stack)
    