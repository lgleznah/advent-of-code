results_dict = {
    ("A", "X"): 4,
    ("A", "Y"): 8,
    ("A", "Z"): 3,
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    ("C", "X"): 7,
    ("C", "Y"): 2,
    ("C", "Z"): 6
}

def main():
    with open("../inputs/input2", "r") as f:
        total_score = sum([results_dict[(line[0], line[2])] for line in f.readlines()])
        print(total_score)

if __name__ == "__main__":
    main()