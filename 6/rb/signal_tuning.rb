def run(path = "signal_data.txt")
    file_data = File.read(path).split("")

    puts signal_pos(file_data, 4)
    puts signal_pos(file_data, 14)
end

def signal_pos(data, size)
    for i in 0..data.length do
        char_buffer = data[i..i+size-1]
        return i + size if char_buffer & char_buffer == char_buffer
    end
end