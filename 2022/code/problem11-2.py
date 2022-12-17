from operator import add, mul
from functools import reduce

operations_dict = {
    '+': add,
    '*': mul
}

def make_function(operation, operand):
    return lambda x: operation(x, x if operand == "old" else int(operand))

def load_monkeys(file_contents):
    monkeys = []
    for i in range(8):
        items = [int(item.replace(',','')) for item in file_contents[i*7 + 1].split()[2:]]

        operator, operand = file_contents[i*7 + 2].split()[4:]
        operation = operations_dict[operator]
        update_func = make_function(operation, operand)
        divisibility_test_value = int(file_contents[i*7 + 3].split()[3])
        test_true_target = int(file_contents[i*7 + 4].split()[5])
        test_false_target = int(file_contents[i*7 + 5].split()[5])
        
        monkey = {
            'items': items,
            'update_func': update_func,
            'div_test_value': divisibility_test_value,
            'target_if_true': test_true_target,
            'target_if_false': test_false_target
        }

        monkeys.append(monkey)
    
    return monkeys

def simulate_monkeys(monkeys):
    inspection_counts = [0 for _ in range(len(monkeys))]
    product = reduce(lambda x, y: x * y, [monkey['div_test_value'] for monkey in monkeys])

    for rnd in range(10000):
        for monkey_number, monkey in enumerate(monkeys):
            while monkey['items']:
                item = monkey['items'].pop(0)
                item = monkey['update_func'](item)
                item %= product
                if (item % monkey['div_test_value'] == 0):
                    monkeys[monkey['target_if_true']]['items'].append(item)
                else:
                    monkeys[monkey['target_if_false']]['items'].append(item)

                inspection_counts[monkey_number] += 1

    first_monkey_inspections, second_monkey_inspections = sorted(inspection_counts, reverse=True)[:2]
    print(first_monkey_inspections * second_monkey_inspections)


def main():
    with open("../inputs/input11", "r") as file:
        monkeys = load_monkeys(file.readlines())
        simulate_monkeys(monkeys)

if __name__ == "__main__":
    main()