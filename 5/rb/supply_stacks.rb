require './stacks.rb'

def run
    file_data = File.read('supply_stacks.txt').split("\n")

    sort_stacks(file_data)
end

def sort_stacks(sorting_data)
    # doesn't work
    stack = stacks()

    sorting_data.each do |line|
        instructions = line.split("\s")
        quantity, from, to = instructions[1].to_i, instructions[3].to_i - 1, instructions[5].to_i - 1
        
        for _ in 0..quantity do
            if stack[from] != ''
                stack[from], popped = stack[from][1..-1], stack[from][0]
                stack[to] = popped + stack[to]
            end
        end
    end

    stack.each do |row|
        puts row[0]
    end
end