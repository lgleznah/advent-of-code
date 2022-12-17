def print_character(output_screen, register_value, cycle_count):
    row, column = cycle_count // 40, cycle_count % 40
    if (register_value - 1 <= column and column <= register_value + 1):
        output_screen[row][column] = '#'
    else:
        output_screen[row][column] = '.'

def main():
    with open("../inputs/input10", "r") as file:
        cycle_count = 0
        register_value = 1
        output_screen = [['?' for _ in range(40)] for _ in range(6)]

        for line in file.readlines():
            instruction = line.split()
            match instruction[0]:
                case "addx":
                    for _ in range(2):
                        print_character(output_screen, register_value, cycle_count)
                        cycle_count += 1
                    
                    register_value += int(instruction[1])

                case "noop":
                    print_character(output_screen, register_value, cycle_count)
                    cycle_count += 1

        print('\n'.join([''.join(line) for line in output_screen]))

if __name__ == "__main__":
    main()