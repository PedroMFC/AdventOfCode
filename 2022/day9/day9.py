import re
import numpy as np

def read_input(file_name: str) -> list[list[str]]:
    motions = []

    with open(file_name) as file:
        for line in file:
            match = re.search('(R|U|L|D) (\d+)', line)
            motion = [match.group(1), match.group(2)]
            motions.append(motion)

    return motions

def mark_as_visited(space: np.matrix, row: int, column: int) -> np.matrix:
    space[row][column] = 1
    return space

def make_move(direction: str, row: int, column: int) -> np.matrix:
    if direction == 'R':
        column += 1
    elif direction == 'L':
        column -= 1
    elif direction == 'U':
        row -= 1
    else: # direction == 'D'
        row += 1

    return row, column


def calculate_tail_move(row: int, column: int, new_row: int, new_column: int) -> tuple[int, int]:
    if abs(row - new_row) + abs(column -new_column) <= 1: # T does not move because it touches H in the same
        return row, column

    if abs(row - new_row) + abs(column -new_column) >= 2:

    return new_row, new_column

def follow_motions(motions: list[list[str]]) -> np.matrix:
    space = np.zeros((500, 500))

    row = 0
    column = 0
    space = mark_as_visited(space, row, column)

    for move in motions:
        for steps in range(int(move[1])):
            new_row, new_colum = make_move(move[0], row, column)

            tail_row, tail_column = calculate_tail_move(row, column, new_row, new_colum)
            space = mark_as_visited(space, tail_row, tail_column)

            row = new_row
            column = new_colum

    return space


def main() -> None:
    motions = read_input('2022/day9/input.txt')

    visited_by_tail = follow_motions(motions)
    positions_visited = visited_by_tail.sum()

    print(f'Tail has visited {positions_visited} positions')

if __name__ == "__main__":
    main()
