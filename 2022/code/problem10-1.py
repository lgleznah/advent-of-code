def main():
    with open("../inputs/input10", "r") as file:
        cycle_count = 0
        register_value = 1
        reading_points = [20, 60, 100, 140, 180, 220]
        signal_pow_sum = 0

        for line in file.readlines():
            instruction = line.split()
            match instruction[0]:
                case "addx":
                    for _ in range(2):
                        cycle_count += 1
                        if (cycle_count in reading_points):
                            signal_pow_sum += register_value * cycle_count
                    
                    register_value += int(instruction[1])

                case "noop":
                    cycle_count += 1
                    if (cycle_count in reading_points):
                            signal_pow_sum += register_value * cycle_count

        print(signal_pow_sum)

if __name__ == "__main__":
    main()