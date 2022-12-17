results_dict = {
    ("A", "X"): 3,
    ("A", "Y"): 4,
    ("A", "Z"): 8,
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    ("C", "X"): 2,
    ("C", "Y"): 6,
    ("C", "Z"): 7
}

def main():
    with open("../inputs/input2", "r") as f:
        total_score = sum([results_dict[(line[0], line[2])] for line in f.readlines()])
        print(total_score)

if __name__ == "__main__":
    main()