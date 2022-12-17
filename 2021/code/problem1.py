def main():
    with open('../inputs/input_1') as f:
        numbers = [int(n) for n in f.readlines()]
        answer = 0
        for i in range(1, len(numbers)):
            if numbers[i] > numbers[i-1]:
                answer += 1

        print(answer)

if __name__ == '__main__':
    main()