from moves import possible_moves

def run(path='../instructions.txt'):
    file_data = open(path).read().strip().split('\n')
    moves = [(direction, int(amount)) for direction, amount in [line.split(' ') for line in file_data]]
    moves = ''.join([char*move for char, move in moves])
    
    print(run_trail(moves, 2))
    print(run_trail(moves, 10))
    
def update_position(piece, offset):
    py, px = piece
    oy, ox = offset
    return (oy+py, ox+px)

def update_tail(tail, head):
    row_offset = head[0] - tail[0]
    column_offset = head[1] - tail[1]

    if (abs(row_offset) <= 1) & (abs(column_offset) <= 1): return tail
    elif (row_offset != 0) and (column_offset != 0):
        diagonal_move = (1 if row_offset > 0 else -1, 1 if column_offset > 0 else -1)
        return update_position(tail, diagonal_move)
    else:
        direction = (
            ('U' if row_offset > 0 else 'D')
            if row_offset != 0 else
            ('R' if column_offset > 0 else 'L')
        )
        return update_position(tail, possible_moves[direction])

def run_trail(moves, tail_length):
    old_rope = tuple([(0, 0) for _ in range(tail_length)])
    history = [old_rope]

    for move in moves:
        new_rope = []
        new_rope.append(update_position(old_rope[0], possible_moves[move]))
        for i in range(1, tail_length):
            new_rope.append(update_tail(old_rope[i], new_rope[i-1]))
        history.append(tuple(new_rope))
        old_rope = new_rope
    
    return len(set(event[-1] for event in history))
