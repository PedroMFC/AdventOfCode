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
        item_in_both = get_item_both_compartemnts(compartments[0],compartments[1])
        sum += calculate_priority(item_in_both)

    return sum

def get_item_both_compartemnts(first: str, second: str) -> str:
    return ''.join(set(first).intersection(second))

def main() -> None:
    rucksack = read_input('day3/input.txt')

    priority_sum = get_priority_sum(rucksack)

    print(f'The priorury sum is {priority_sum}')

if __name__ == "__main__":
    main()