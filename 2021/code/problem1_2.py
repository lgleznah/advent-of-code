def main():
    with open('../inputs/input_1') as f:
        numbers = [int(n) for n in f.readlines()]
        answer = 0
        for i in range(0, len(numbers) - 3):
            if (numbers[i+1] + numbers[i+2] + numbers[i+3] > numbers[i] + numbers[i+1] + numbers[i+2]):
                answer += 1
        
        print(answer)

if __name__ == '__main__':
    main()