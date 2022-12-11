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


def calculate_tail_move_v1(t_row: int, t_column: int, new_h_row: int, new_h_column: int) -> tuple[int, int]:
    new_t_row = None
    new_t_column = None


    # Case H moves same row
    if t_row == new_h_row:
        new_t_row = t_row
        if abs(t_column - new_h_column) <= 1:
            new_t_column = t_column
        elif new_h_column < t_column:
            new_t_column = t_column - 1
        else:
            new_t_column = t_column + 1

    # Case H moves same column
    elif t_column == new_h_column:
        new_t_column = t_column
        if abs(t_row - new_h_row ) <= 1:
            new_t_row = t_row
        elif new_h_row < t_row:
            new_t_row = t_row - 1
        else:
            new_t_row = t_row + 1
    # Diagonal
    else:
        if abs(t_row - new_h_row) == 1 and abs(t_column - new_h_column) == 1:
            new_t_row = t_row
            new_t_column = t_column
        else:
            if new_h_row < t_row :
                new_t_row = t_row -1
            else:
                new_t_row = t_row + 1

            if new_h_column < t_column:
                new_t_column = t_column - 1
            else:
                new_t_column = t_column + 1

    return new_t_row, new_t_column

def calculate_tail_move(t_row: int, t_column: int, new_h_row: int, new_h_column: int) -> tuple[int, int]:
    new_t_row = t_row
    new_t_column = t_column


    # Case H moves same row
    if t_row == new_h_row:
        if new_h_column < t_column - 1:
            new_t_column = t_column - 1
        elif new_h_column > t_column +1:
            new_t_column = t_column + 1

    # Case H moves same column
    elif t_column == new_h_column:
        if new_h_row < t_row -1:
            new_t_row = t_row - 1
        elif new_h_row > t_row + 1:
            new_t_row = t_row + 1
    # Diagonal
    else:
        if abs(t_row - new_h_row) != 1 or abs(t_column - new_h_column) != 1:
            if new_h_row < t_row:
                new_t_row = t_row -1
            else:
                new_t_row = t_row + 1

            if new_h_column < t_column:
                new_t_column = t_column - 1
            else:
                new_t_column = t_column + 1

    return new_t_row, new_t_column
def follow_motions(motions: list[list[str]], rope_long: int) -> set:
    visited = set()

    rope = [ [0, 0]  for i in range(rope_long)]

    visited.add( tuple([rope[0][0], rope[0][0]]) )

    for move in motions:
        for steps in range(int(move[1])):
            new_h_row, new_h_colum = make_move(move[0], rope[0][0], rope[0][1])
            rope_after_move = [[new_h_row, new_h_colum]]

            for i in range(1, rope_long):
                t_row, t_column = calculate_tail_move(rope[i][0], rope[i][1],
                                                      rope_after_move[i-1][0], rope_after_move[i-1][1])
                rope_after_move.append([t_row, t_column])
            
            visited.add( tuple([rope_after_move[rope_long - 1][0], rope_after_move[rope_long - 1][1]]) )

            rope = rope_after_move

    return visited

def main() -> None:
    motions = read_input('2022/day9/input.txt')

    visited_by_tail_2 = follow_motions(motions, 2)
    positions_visited_2 = len(visited_by_tail_2)

    print(f'Tail has visited {positions_visited_2} positions')

    visited_by_tail_10 = follow_motions(motions, 10)
    positions_visited_10 = len(visited_by_tail_10)

    print(f'Tail has visited {positions_visited_10} positions')

if __name__ == "__main__":
    main()
