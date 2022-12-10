def run(path='../input.txt'):
    file_data = open(path).read().strip().split('\n')
    
    values = get_values(file_data)
    sum_signal_strength = sum([cycle * values[cycle-1] for cycle in [20, 60, 100, 140, 180, 220]])
    print(sum_signal_strength)

    make_crt(file_data)

def get_values(data):
    values, x = [0], 1
    for line in data:
        if line.startswith('noop'):
            values.append(x)
        else:
            line = line.split(' ')
            values.append(x)
            x += int(line[1])
            values.append(x)
    return values

def make_crt(data, line=40):
    values = get_values(data)
    crt = ['#' if abs(index - (i % line)) <= 1 else ' ' for i, index in enumerate(values)]
    for i in range(0, len(values) // line):
        print(''.join(crt[i * line:(i+1) * line]))
