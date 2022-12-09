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


def calculate_tail_move(t_row: int, t_column: int, h_row: int, h_column: int, new_h_row: int, new_h_column: int) -> tuple[int, int]:
    new_t_row = None
    new_t_colum = None


    # Case H moves same row
    if h_row == new_h_row:
        if t_column == new_h_column:
            new_t_row = t_row
             
        tail_row = row
        if new_column < column:
            tail_colum = new_column + 1
        else:
            tail_colum = new_column - 1 

    # Case same column
    elif column == new_column:
        tail_colum = column
        if new_row < row:
            tail_row = new_row + 1
        else:
            tail_row = new_row - 1
    # Diagonal -> keeps H position
    else:
        tail_row = row
        tail_colum = column


    return new_t_row, new_t_colum

def follow_motions(motions: list[list[str]]) -> np.matrix:
    space = np.zeros((500, 500))

    h_row = 0
    h_column = 0
    t_row = 0
    t_column = 0
    space = mark_as_visited(space, t_row, t_column)

    for move in motions:
        for steps in range(int(move[1])):
            new_h_row, new_h_colum = make_move(move[0], row, column)

            t_row, t_column = calculate_tail_move(t_row,t_column, h_row, h_column, new_h_row, new_h_colum)
            space = mark_as_visited(space, t_row, t_column)

            h_row = new_h_row
            h_column = new_h_colum

    return space


def main() -> None:
    motions = read_input('2022/day9/input.txt')

    visited_by_tail = follow_motions(motions)
    positions_visited = visited_by_tail.sum()

    print(f'Tail has visited {positions_visited} positions')

if __name__ == "__main__":
    main()
