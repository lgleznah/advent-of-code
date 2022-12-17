def main():
    with open('../inputs/input_2') as f:
        commands = f.readlines()
        hpos, depth = (0, 0)
        aim = 0
        for c in commands:
            command, amount = (c.split()[0], int(c.split()[1]))
            match command:
                case 'forward':
                    hpos += amount
                    depth += aim * amount
                
                case 'down':
                    aim += amount

                case 'up':
                    aim -= amount

        print(hpos * depth)

if __name__ == '__main__':
    main()