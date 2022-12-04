require './outcomes.rb'

def run()
    file_data = read_file("rps.txt")

    puts calculate_score(file_data)
    puts calculate_desired_score(file_data)
end

def read_file(path)
    file_data = File.read(path).split("\n")
end

def calculate_score(data)
    total = 0

    data.each do |round|
        total += outcomes[round]
    end

    total
end

def calculate_desired_score(data)
    total = 0

    data.each do |round|
        total += desired_outcomes[round]
    end

    total
end