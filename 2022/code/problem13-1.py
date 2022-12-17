import re

def compare(a, b):
    match a,b:
        case int(), int():
            return (-1 if a < b else (0 if a == b else 1))
        
        case list(), list():
            for a_elem, b_elem in zip(a,b):
                compare_result = compare(a_elem, b_elem)
                if (compare_result != 0):
                    return compare_result
            
            return (-1 if len(a) < len(b) else (0 if len(a) == len(b) else 1))

        case int(), list():
            return compare([a], b)
        
        case list(), int():
            return compare(a, [b])

def main():
    with open("../inputs/input13", "r") as file:
        inputs = file.readlines()
        i = 0
        pair_index = 1
        index_sum = 0
        while i < len(inputs):
            safe_list1 = re.sub('[^0-9\[\],]', '', inputs[i])
            safe_list2 = re.sub('[^0-9\[\],]', '', inputs[i+1])
            list1 = eval(safe_list1)
            list2 = eval(safe_list2)

            if (compare(list1, list2) == -1):
                index_sum += pair_index

            i += 3
            pair_index += 1

        print(index_sum)

if __name__ == "__main__":
    main()