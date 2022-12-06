def run(path = 'signal_data.txt'):
    with open(path) as file:
        file_data = file.read()

    print(f'1. {signal_position(file_data, 4)}')
    print(f'2. {signal_position(file_data, 14)}')

def signal_position(data, size):
    for i in range(len(data)):
        char_buffer = [char for char in ''.join(data[i:i+size])]
        if len(set(char_buffer)) == len(char_buffer) : return i + size 
        