#possible_moves = {
#    'U' => (1, 0),
#    'D' => (-1, 0),
#    'R' => (0, 1), 
#    'L' => (0, -1)
#}

def run(path = "../instructions.txt")
    coord = (1, 2)
    puts coord
end

def run_instr(moves, move_length)

end

def update_position(piece, offset)
    py, px = piece
    oy, ox = offset
    return (oy + py, ox + px)
end

def update_tail(tail, head)
    row_off, col_off = head[0] - tail[0], head[1] - tail[1]

    
end