def main():
    with open("../inputs/input6", "r") as f:
        signal = f.read()
        index = 0
        while True:
            signal_part = signal[index:index+14]
            if (len(set(signal_part)) == 14):
                print(index+14)
                return
            index += 1

if __name__ == "__main__":
    main()