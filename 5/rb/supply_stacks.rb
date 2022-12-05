require './stacks.rb'

def run
    file_data = File.read('supply_stacks.txt').split("\n")

    puts sort_stacks(file_data)
end

def sort_stacks(sorting_data)
    # doesn't work
    stack = stacks()

    sorting_data.each do |line|
        instructions = line.split("\s")
        quantity, from, to = instructions[1].to_i, instructions[3].to_i - 1, instructions[5].to_i - 1
        
        for i in 0..quantity do
            stack[to].insert(0, stack[from].shift)
        end
    end

    stack
end