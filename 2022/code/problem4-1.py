def main():
    with open("../inputs/input4", "r") as f:
        total_overlaps = 0
        for line in f:
            elf1, elf2 = line.split(",")
            ((start1, end1), (start2, end2)) = [[int(x) for x in elf1.split("-")], [int(x) for x in elf2.split("-")]]

            # Second interval is inside the first one
            if (start2 >= start1 and start2 <= end1 and end2 >= start1 and end2 <= end1):
                total_overlaps += 1

            # First interval is inside the second one
            elif (start1 >= start2 and start1 <= end2 and end1 >= start2 and end1 <= end2):
                total_overlaps += 1

        print(total_overlaps)

if __name__ == "__main__":
    main()