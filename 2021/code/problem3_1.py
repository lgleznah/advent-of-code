def main():
    with open('../inputs/input_3') as f:
        numbers = f.readlines()
        numbers = [[int(n) for n in x[:-1]] for x in numbers]
        numbers = list(zip(*numbers))
        ratios = [round(sum(col) / len(col)) for col in numbers]
        gamma = int(''.join([str(r) for r in ratios]), 2)
        epsilon = int(''.join([str(1 - r) for r in ratios]), 2)

        print(gamma * epsilon)

if __name__ == '__main__':
    main()