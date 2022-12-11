import re
import numpy as np


def read_input(file_name: str) -> list[list[str]]:
    instructions = []

    with open(file_name) as file:
        for line in file:
            match = re.search('(addx) (-?\d+)', line)
            if match is not None:
                instructions.append([match.group(1), match.group(2)])
            else:
                instructions.append([line[:-1]])

    return instructions

def calculate_register_values(instructions: list[list[int]]) -> list[int]:
    x = 1
    values = [x]

    for instruction in instructions:
        values.append(x)
        if instruction[0] == 'addx':
            x += int(instruction[1])
            values.append(x)

    return values

def get_x_value(register_values: list[int], cycle: int) -> int:
    return register_values[cycle - 1]*cycle

def sum_signal_strenght(register_values: list[int]) -> int:
    sum_signal = 0
    cycles = [20, 60, 100, 140, 180, 220]

    for i in cycles:
        sum_signal += get_x_value(register_values, i)

    return sum_signal

def main() -> None:
    instructions = read_input('2022/day10/input.txt')

    register_x_values = calculate_register_values(instructions)
    sum_strenght = sum_signal_strenght(register_x_values)

    print(f'The sum of the signal strength is {sum_strenght}')

if __name__ == "__main__":
    main()