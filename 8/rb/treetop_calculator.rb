def run(path = "../map.txt")
    data = File.read(path).split("\n")
    grid = make_grid(data)
    
    puts tree_house(grid)
end

def make_grid(data, grid = [])
    data.each_with_index do |line, i|
        grid.append([])
        chars = line.chars
        chars.each do |num|
            grid[i].append(num.to_i)
        end
    end
    return grid
end

def tree_house(grid)
    total, tree_values = (4 * grid.length) - 4, []
    for i in 1..grid.length-2 do
        for j in 1..grid[i].length-2 do
            item = grid[i][j]

            up, down, left, right = [], [], grid[i][0..j-1], grid[i][j+1..grid[j].length]
            for k in 0..i-1 do up.append(grid[k][j]) end
            for k in i+1..grid[i].length-1 do down.append(grid[k][j]) end
            
            total += 1 if check_visible?(item, [up, down, left, right])
            tree_values.append(view_distance(item, up.reverse()) * view_distance(item, down) * view_distance(item, left.reverse()) * view_distance(item, right))
        end
    end
    return total, tree_values.max()
end

def check_visible?(item, directions)
    directions.each do |direction|
        blocked = false
        direction.each do |tree|
            blocked = true if item <= tree
        end
        return true if not blocked
    end
    return false
end

def view_distance(item, direction)
    v_distance = 0
    direction.each do |dir|
        v_distance += 1
        break if item <= dir
    end
    return v_distance
end