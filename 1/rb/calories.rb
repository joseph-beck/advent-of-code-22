def run
    file_data = read_file("../calorie_counter.txt")

    puts get_max_cal(file_data)
    puts get_top_three(file_data)
end

def read_file(path)
    file = File.read(path).split("\n")
end

def get_max_cal(data)
    total, calories = 0, []
    
    data.each do |cal|
        if cal != ""
            total += cal.to_i
        else
            calories.append(total)
            total = 0
        end
    end

    return calories.max()
end

def get_top_three(data)
    total, calories, top_three = 0, [], []

    data.each do |cal|
        if cal != ""
            total += cal.to_i
        else
            calories.append(total)
            total = 0
        end
    end

    for i in 0..2 do
        top_three.append(calories.max())
        puts calories.max()
        calories.delete(calories.max())
    end

    top_three.sum()
end