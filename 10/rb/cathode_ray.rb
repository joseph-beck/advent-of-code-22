# mostly by ChatGPT 🙃

def run(path="../input.txt")
    file_data = File.read(path).strip.split("\n")
  
    values = get_values(file_data)
    sum_signal_strength = [20, 60, 100, 140, 180, 220].sum { |cycle| cycle * values[cycle-1] }
    puts sum_signal_strength
  
    make_crt(file_data)
  end
  
  def get_values(data)
    values, x = [0], 1
    data.each do |line|
      if line.start_with?("noop")
        values << x
      else
        line = line.split(" ")
        values << x
        x += line[1].to_i
        values << x
      end
    end
    values
  end
  
  def make_crt(data, line=40)
    values = get_values(data)
    crt = values.map.with_index { |index, i| (index - (i % line)).abs <= 1 ? '#' : '.' }
    (0...values.length.div(line)).each do |i|
      puts crt[i*line, (i+1)*line].join('')
    end
  end