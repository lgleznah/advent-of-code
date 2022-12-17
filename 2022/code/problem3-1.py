alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    with open("../inputs/input3", "r") as f:
        priority_sum = 0
        for line in f:
            comp_1, comp_2 = set(line[:len(line) // 2]), set(line[len(line) // 2:])
            (duplicated, ) = comp_1 & comp_2
            priority_dup = alphabet.index(duplicated) + 1
            priority_sum += priority_dup
        
        print(priority_sum)

if __name__ == "__main__":
    main()