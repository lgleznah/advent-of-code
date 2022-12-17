directions = {'forward': (1,0), 'down': (0,1), 'up': (0, -1)}

def main():
    with open('../inputs/input_2') as f:
        commands = f.readlines()
        hpos, depth = (0, 0)
        for c in commands:
            command, amount = (c.split()[0], int(c.split()[1]))
            hpos, depth = (hpos + directions[command][0] * amount, depth + directions[command][1] * amount)

        print(hpos * depth)

if __name__ == '__main__':
    main()