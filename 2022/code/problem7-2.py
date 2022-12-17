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
                # CD command. Change the current directory to the given one
                case "$ cd":
                    new_directory = line.split()[2]
                    current_directory = current_directory[new_directory]

                # LS command. Add new files to the current directory, as given by the output of LS
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

def get_sizes(filesystem, sizes_dict, dirname):
    # Depth-first traversal of the filesystem, that keeps track in a dict of the directories sizes
    current_dir_size = 0
    for file, contents in filesystem.items():
        match contents:
            case int(size):
                current_dir_size += size
            case dict(directory) if file != "..":
                current_dir_size += get_sizes(directory, sizes_dict, f'{dirname}{file}/')
    
    sizes_dict.update({dirname: current_dir_size})
    
    return current_dir_size


def get_disk_usage_and_sizes(filesystem):
    sizes = {}
    disk_usage = get_sizes(filesystem["/"], sizes, "/")
    return disk_usage, sizes

def main():
    filesystem = load_filesystem()
    disk_usage, sizes = get_disk_usage_and_sizes(filesystem)
    
    required_space = disk_usage + 30000000 - 70000000
    for dir, size in sorted(list(sizes.items()), key = lambda x: x[1]):
        if size > required_space:
            print(f"Found! Directory {dir}, with size {size}, must be deleted!")
            break

if __name__ == "__main__":
    main()