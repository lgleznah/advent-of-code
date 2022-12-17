def main():
    with open("../inputs/input5", "r") as f:
        stacks = [
            ['B', 'Z', 'T'],
            ['V', 'H', 'T', 'D', 'N'],
            ['B', 'F', 'M', 'D'],
            ['T', 'J', 'G', 'W', 'V', 'Q', 'L'],
            ['W', 'D', 'G', 'P', 'V', 'F', 'Q', 'M'],
            ['V', 'Z', 'Q', 'G', 'H', 'F', 'S'],
            ['Z', 'S', 'N', 'R', 'L', 'T', 'C', 'W'],
            ['Z', 'H', 'W', 'D', 'J', 'N', 'R', 'M'],
            ['M', 'Q', 'L', 'F', 'D', 'S']
        ]

        moves = f.readlines()[10:]
        for move in moves:
            _, amount, _, source, _, destination = move.split(' ')
            amount, source, destination = int(amount), int(source), int(destination)
            elements_to_move = stacks[source-1][-amount:]
            for element in elements_to_move:
                stacks[destination-1].append(element)
            stacks[source-1][-amount:] = []

        for stack in stacks:
            print(stack[-1], end="")

if __name__ == "__main__":
    main()