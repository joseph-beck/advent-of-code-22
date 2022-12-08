def run(path='../map.txt'):
    file_data = open(path).read().strip().split('\n')
    grid = [list(map(int, line)) for line in file_data]

    visible_trees, tree_scores = treetop_tree_house(grid)
    print(visible_trees)
    print(tree_scores)

def treetop_tree_house(grid):
    total, tree_values = (4*len(grid)) - 4, []
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            item = grid[i][j]
            up = [grid[k][j] for k in range(0, i)]
            down = [grid[k][j] for k in range(i+1, len(grid[i]))]
            left = grid[i][0:j]
            right = grid[i][j+1:len(grid[j])]
            if check_visible(item, [up[::-1], down, left[::-1], right]): total += 1
            tree_values.append(view_distance(item, up[::-1]) * view_distance(item, down) * view_distance(item, left[::-1]) * view_distance(item, right))

    return total, max(tree_values)

def check_visible(item, directions):
    for direction in directions:
        row_val = 0
        for i in range(0, len(direction)):
            if item <= direction[i]: row_val = 1
        if row_val == 0: return True
    return False

def view_distance(item, direction):
    v_distance = 0
    for i in range(0, len(direction)):
        v_distance += 1
        if item <= direction[i]: break
    return v_distance
