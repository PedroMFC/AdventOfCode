import numpy as np

def read_input(file_name: str) -> np.matrix:
    matrix = np.empty((0,2), int)

    with open(file_name) as file:
        for line in file:
            first_compartment = line[:len(line)//2]
            second_compartment = line[len(line)//2:-1]
            matrix = np.append(matrix, np.array([[first_compartment, second_compartment]]), axis=0)

    return matrix


def calculate_priority(letter: str) -> int:
    return ord(letter) - ord('a') + 1 if letter.islower() else ord(letter) - ord('A') + 27


def get_priority_sum(rucksack: np.matrix) -> int:
    sum = 0

    for compartments in rucksack:
        item_in_both = get_items_both_compartemnts(compartments[0],compartments[1])
        sum += calculate_priority(item_in_both)

    return sum


def get_items_both_compartemnts(first: str, second: str) -> str:
    return ''.join(set(first).intersection(second))


def get_group(first: str, second: str, third: str) -> str:
    common_1 = get_items_both_compartemnts(first, second)
    common_all = get_items_both_compartemnts(common_1, third)

    return common_all

def join_compartements(compartments: np.array) -> str:
    return compartments[0].join(compartments[1]) 

def get_group_priority_sum(rucksack: np.matrix) -> int:
    sum = 0

    for group in range(0, len(rucksack), 3):
        common_item = get_group( 
            join_compartements( rucksack[group] ), 
            join_compartements( rucksack[group + 1] ),
            join_compartements( rucksack[group + 2]) )
        sum += calculate_priority(common_item)

    return sum


def main() -> None:
    rucksack = read_input('2022/day3/input.txt')

    priority_sum = get_priority_sum(rucksack)

    print(f'The priorury sum is {priority_sum}')

    group_sum = get_group_priority_sum(rucksack)

    print(f'The priorury sum of groups is {group_sum}')


if __name__ == "__main__":
    main()