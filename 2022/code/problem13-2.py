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

class Package:
    def __init__(self, package):
        self.package = package

    def __lt__(self, other):
        return (compare(self.package, other.package) == -1)

    def __str__(self):
        return str(self.package)

def main():
    with open("../inputs/input13", "r") as file:
        inputs = file.readlines()
        
        packages = [Package([[2]]),Package([[6]])]
        i = 0
        while i < len(inputs):
            safe_list1 = re.sub('[^0-9\[\],]', '', inputs[i])
            safe_list2 = re.sub('[^0-9\[\],]', '', inputs[i+1])
            packages.append(Package(eval(safe_list1)))
            packages.append(Package(eval(safe_list2)))
            i += 3

        sorted_packages = sorted(packages)

        indexof_two = -1
        indexof_six = -1
        for idx, package in enumerate(sorted_packages):
            if package.package == [[2]]:
                indexof_two = idx + 1

            if package.package == [[6]]:
                indexof_six = idx + 1

        print(indexof_two * indexof_six)

if __name__ == "__main__":
    main()