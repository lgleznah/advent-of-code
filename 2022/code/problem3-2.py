from itertools import islice

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    with open("../inputs/input3", "r") as f:
        priority_sum = 0
        while True:
            next_lines = list(islice(f, 3))
            if not next_lines:
                break

            (elf1, elf2, elf3) = set(next_lines[0].strip()), set(next_lines[1].strip()), set(next_lines[2].strip())
            (duplicated, ) = elf1 & elf2 & elf3
            priority_sum += alphabet.index(duplicated) + 1

        print(priority_sum)

if __name__ == "__main__":
    main()