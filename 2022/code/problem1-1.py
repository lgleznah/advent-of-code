import itertools

def main():
    with open("../inputs/input1", "r") as f:
        calories = [line.strip() for line in f.readlines()]
        elf_calories = [list(y) for x, y in itertools.groupby(calories, lambda z: z == "") if not x]
        max_calories = max([sum([int(food) for food in elf]) for elf in elf_calories])
        print(max_calories)

if __name__ == "__main__":
    main()