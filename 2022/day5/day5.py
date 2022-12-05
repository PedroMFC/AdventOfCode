import re
import copy

def get_stacks(stack_input: list[str]) -> list[list[str]]:
    stack_input.reverse()

    stacks_ids = stack_input.pop(0)
    number_stacks = int(stacks_ids[-3])
    stacks = []
    for i in range(number_stacks):
        stacks.append([])

    for line in stack_input:
        for i in range(number_stacks):
            crate = line[i*4 + 1]
            if crate != ' ':
                stacks[i].append(crate)

    return stacks

def get_procedure(procedure_input: list[str]) -> list[list[str]]:
    procedure = []
    
    for movement in procedure_input:
        match = re.search("move (\d+) from (\d+) to (\d+)",movement)
        procedure.append( [match.group(1), match.group(2), match.group(3) ])

    return procedure


def read_input(file_name: str) -> tuple[list[list[str]], list[list[int]]]:
    stack_reading = True
    stacks_input = []
    procedure_input = []

    with open(file_name) as file:
        for line in file:
            if line == '\n':
                stack_reading = False
                continue
            stacks_input.append(line) if stack_reading else procedure_input.append(line)

    stacks = get_stacks(stacks_input)
    procedure = get_procedure(procedure_input)

    return stacks, procedure


def move_crates_CrateMover_9000(stacks: list[list[str]], procedure: list[list[int]]) -> list[list[str]]:

    for movement in procedure:
        cranes_to_move = int(movement[0])
        origin = int(movement[1]) - 1
        destiny = int(movement[2]) - 1
        for i in range(cranes_to_move):
            crane = stacks[origin].pop()
            stacks[destiny].append(crane)

    return stacks

def move_crates_CrateMover_9001(stacks: list[list[str]], procedure: list[list[int]]) -> list[list[str]]:

    for movement in procedure:
        cranes_to_move = int(movement[0])
        origin = int(movement[1]) - 1
        destiny = int(movement[2]) - 1

        aux = []
        for i in range(cranes_to_move):
            crane = stacks[origin].pop()
            aux.append(crane)
        for crane in reversed(aux):
            stacks[destiny].append(crane)

    return stacks


def get_top_items(stacks: list[list[str]]) -> str:
    top_items = ''

    for stack in stacks:
        top_items += stack[- 1]

    return top_items


def main() -> None:
    stacks, procedure = read_input('2022/day5/input.txt')

    stacks_CrateMover_9000 = move_crates_CrateMover_9000(copy.deepcopy(stacks), procedure)
    stacks_CrateMover_9001 = move_crates_CrateMover_9001(copy.deepcopy(stacks), procedure)

    top_items_CrateMover_9000 = get_top_items(stacks_CrateMover_9000)
    top_items_CrateMover_9001 = get_top_items(stacks_CrateMover_9001)

    print(f'The top items withc CrateMover 9000 are {top_items_CrateMover_9000}')
    print(f'The top items withc CrateMover 9001 are {top_items_CrateMover_9001}')


if __name__ == "__main__":
    main()