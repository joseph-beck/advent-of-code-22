import sys

from tree import DataTree

def run(path = '../instructions.txt'):
    file_data = open(path).read().split('\n')

    print(sum_dirs_one(make_directories(file_data)))
    print(sum_dirs_two(make_directories(file_data)))

def make_directories(data):
    system = DataTree('/')
    for line in data[1:]:
        match line.split():
            case '$', 'cd', loc: system = system.parent if loc == '..' else system.mkdir(loc)
            case '$', 'ls': pass
            case 'dir', _: pass
            case size, name: system.touch(size, name)
    return system
    
def sum_dirs_one(system, total=0):
    for child in system.root: total += child.size if child.size < 100000 else 0
    return total

def sum_dirs_two(system,child_totals=[]):
    # update space = 70000000 - 30000000
    # = 40000000
    for child in system.root: child_totals.append(child.size if 40000000 + child.size > system.root.size else sys.maxsize)
    return min(child_totals)
