def load_filesystem():
    with open("../inputs/input7", "r") as file:
        filesystem = {"/": {}}
        current_directory = filesystem
        # Process all lines of the file, running commands as needed
        lines = file.readlines()
        line_idx = 0
        while line_idx < len(lines):
            line = lines[line_idx]
            match line[:4]:
                case "$ cd":
                    new_directory = line.split()[2]
                    current_directory = current_directory[new_directory]
                case "$ ls":
                    line_idx += 1
                    while (line_idx < len(lines) and lines[line_idx][0] != '$'):
                        line = lines[line_idx]
                        match line[:3]:
                            case "dir":
                                dirname = line.split()[1]
                                current_directory.update({dirname: {"..": current_directory}})
                            case _:
                                size, filename = line.split()
                                current_directory.update({filename: int(size)})
                        
                        line_idx += 1

                    line_idx -= 1
            
            line_idx += 1

    return filesystem

def get_sizes_lessthan(filesystem, sizes_list):
    current_dir_size = 0
    for file, contents in filesystem.items():
        match contents:
            case int(size):
                current_dir_size += size
            case dict(directory) if file != "..":
                current_dir_size += get_sizes_lessthan(directory, sizes_list)
    
    if current_dir_size < 100000:
        sizes_list.append(current_dir_size)
    
    return current_dir_size


def get_sum_sizes_lessthan(filesystem):
    # Depth-first traversal of the filesystem, that keeps track in a list of the directories
    # whose size is at most 100000
    sizes_lessthan = []
    _ = get_sizes_lessthan(filesystem, sizes_lessthan)
    return sum(sizes_lessthan)

def main():
    filesystem = load_filesystem()
    print(get_sum_sizes_lessthan(filesystem))

if __name__ == "__main__":
    main()