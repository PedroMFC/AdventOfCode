import re
import operator
import copy

def read_input(file_name: str) -> list[list[str]]:
    mokeys = []

    file = open(file_name)
    lines = [ line[:-1] for line in file] # To remove '\n'
    file.close()

    for i in range(0, len(lines), 7):
        mokey = read_monkey(lines, i)
        mokeys.append(mokey)

    return mokeys

def read_monkey(lines: list[str], index: int) -> dict:
    monkey = { 'inspected_items': 0 }

    for i in range(1,6):
        if i == 1: # Starting items
            items = re.search('Starting items: (.+)', lines[index+i]).group(1)
            monkey['items'] = items.split(', ')
        elif i == 2: #Operation
            match = re.search('Operation: new = old (\*|\+) (\d+|old)', lines[index+i])
            opt = operator.mul if match.group(1) == '*' else operator.add
            monkey['operation'] = {
                'operator': opt,
                'number': match.group(2)
            }
        elif i == 3: # Test
            test = re.search('Test: divisible by (\d+)', lines[index+i]).group(1)
            monkey['test'] = int(test)
        elif i == 4: # If True
            next_mokey = re.search('If true: throw to monkey (\d+)', lines[index+i]).group(1)
            monkey['true'] = int(next_mokey)
        else: # If False
            next_mokey = re.search('If false: throw to monkey (\d+)', lines[index+i]).group(1)
            monkey['false'] = int(next_mokey)


    return monkey

def play_round(monkeys: list[dict], divide_by_three: bool = True, prod_mods: int = 1) -> list[dict]:

    for monkey in monkeys:
        
        for item in monkey['items']:
            second_value_opt = int(item) if monkey['operation']['number'] == 'old' else int(monkey['operation']['number'])
            worry_level = monkey['operation']['operator'](int(item), second_value_opt)

            if divide_by_three:
                worry_level //= 3
            else:
                worry_level %= prod_mods

            if worry_level % monkey['test'] == 0:
                monkeys[monkey['true']]['items'].append(worry_level)
            else:
                monkeys[monkey['false']]['items'].append(worry_level)

            monkey['inspected_items'] += 1
            
        monkey['items'] = []

    return monkeys

def get_monkey_business(items_inspected_by_monkey: list[int]) -> int:
    monkey_business = 1

    for i in range(2):
        max_monkey = max(items_inspected_by_monkey)
        items_inspected_by_monkey.remove(max_monkey)

        monkey_business *= max_monkey

    return monkey_business

def calculate_prod_mods(monkeys: list[dict]) -> int:
    prod_mods = 1

    for monkey in monkeys:
        prod_mods *= monkey['test']

    return prod_mods

def main() -> None:
    monkeys = read_input('2022/day11/input.txt')
    monkeys_copy = copy.deepcopy(monkeys)

    for i in range(20):
        monkeys = play_round(monkeys)

    items_inspected_by_monkey = [ monkey['inspected_items'] for monkey in monkeys ]
    monkey_business = get_monkey_business(items_inspected_by_monkey)

    print(f'The level of monkey business after 20 rounds is {monkey_business}')

    prod_mods = calculate_prod_mods(monkeys_copy)

    for i in range(10000):
        monkeys_copy = play_round(monkeys_copy, False, prod_mods)

    items_inspected_by_monkey_10000 = [ monkey['inspected_items'] for monkey in monkeys_copy ]
    monkey_business_10000 = get_monkey_business(items_inspected_by_monkey_10000)

    print(f'The level of monkey business after 20 rounds is {monkey_business_10000}')
    


if __name__ == "__main__":
    main()