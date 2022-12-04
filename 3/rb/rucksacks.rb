require './priorities.rb'

def run()
    data = read_file('rucksacks.txt')

    puts rucksack_sum(data)
    puts badge_sum(data)
end

def read_file(path)
    file_data = File.read(path).split()
end

def rucksack_sum(rucksack)
    total = 0

    rucksack.each do |compartment|
        half = compartment.length() / 2
        left_compartment, right_compartment = compartment[0..half].split(''), compartment[half..-1].split('')
        common_type = nil

        left_compartment.each do |l_char|
            break if common_type != nil
            right_compartment.each do |r_char|
                common_type = l_char if l_char == r_char
            end
        end

        total += priorities[common_type]
    end

    total
end

def badge_sum(rucksack)
    total = 0

    (0..rucksack.length - 1).step(3).each do |index|
        comp_one = rucksack[index + 0].split('')
        comp_two = rucksack[index + 1].split('')
        comp_three = rucksack[index + 2].split('')
        common_type = nil

        comp_one.each do |char_one|
            break if common_type != nil
            comp_two.each do |char_two|
                break if common_type != nil
                comp_three.each do |char_three|
                    common_type = char_one if char_one == char_two and char_two == char_three
                end
            end
        end

        total += priorities[common_type]
    end

    total
end