from outcomes import outcomes, desired_outcomes

def run(): 
    stratergy_guide = read_file_spaceless('rps.txt')

    stratergy_points = calculate_score(stratergy_guide)
    print(stratergy_points)
    desired_stratergy_points = calculate_desired_score(stratergy_guide)
    print(desired_stratergy_points)

def read_file(path):
    output = []

    with open(path) as file:
        for line in file:
            output.append(line.strip())

    return output

def read_file_spaceless(path):
    output = []

    with open(path) as file:
        for line in file:
            output.append(line.strip().replace(" ", ""))

    return output

def calculate_score(game):
    total = 0;

    for round in game:
        total += outcomes[round]

    return total

def calculate_desired_score(game):
    total = 0;

    for round in game:
        total += desired_outcomes[round]

    return total
