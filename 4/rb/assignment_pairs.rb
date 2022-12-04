def run()
    file_data = read_file('assignments.txt')

    puts calculate_overlap(file_data)
    puts calculate_overlap_pairs(file_data)
end

def read_file(path)
    file_data = File.read(path).split()
end

def calculate_overlap(data)
    overlaps = 0

    data.each do |item|
        item_one, item_two = item.split(',')
        start_one, end_one = item_one.split('-')
        start_two, end_two = item_two.split('-')

        start_one, end_one, start_two, end_two = start_one.to_i, end_one.to_i, start_two.to_i, end_two.to_i

        overlaps += 1 if (start_one <= start_two and end_two <= end_one) or (start_two <= start_one and end_one <= end_two)
    end

    overlaps
end

def calculate_overlap_pairs(data)
    overlaps = 0

    data.each do |item|
        item_one, item_two = item.split(',')
        start_one, end_one = (item_one.split('-'))
        start_two, end_two = (item_two.split('-'))

        start_one, end_one, start_two, end_two = start_one.to_i, end_one.to_i, start_two.to_i, end_two.to_i

        overlaps += 1 if (start_one <= end_two) and (start_two <= end_one)
    end

    overlaps
end