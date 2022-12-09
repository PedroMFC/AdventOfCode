def read_input(file_name: str) -> list[list[int]]:
    grid = []

    with open(file_name) as file:
        for line in file:
            row = [ int(tree) for tree in line[:-1]]
            grid.append(row)

    return grid

# PART 1: VISIBILITY FUNCTIONS

def is_edge_tree(grid: list[list[int]], row: int, column: int) -> bool:
    return row == 0 or column == 0 or row == len(grid) - 1 or column == len(grid[row]) - 1


def is_visible_left(grid: list[int], row: int, column: int) -> bool:
    for index in range(column):
        if grid[row][index] >= grid[row][column]:
            return False

    return True

def is_visible_right(grid: list[int], row: int, column: int) -> bool:
    for index in range(column+1, len(grid[row])):
        if grid[row][index] >= grid[row][column]:
            return False

    return True


def is_visible_top(grid: list[int], row: int, column: int) -> bool:
    for index in range(row):
        if grid[index][column] >= grid[row][column]:
            return False

    return True


def is_visible_bottom(grid: list[int], row: int, column: int) -> bool:
    for index in range(row+1, len(grid)):
        if grid[index][column] >= grid[row][column]:
            return False

    return True


def is_visible(grid: list[list[int]], row: int, column: int) -> bool:
    return (
        is_edge_tree(grid, row, column) or
        is_visible_left(grid, row, column) or
        is_visible_right(grid, row, column) or
        is_visible_top(grid, row, column) or
        is_visible_bottom(grid, row, column)
    )


def get_visible_trees(grid: list[list[int]]) -> int:
    visible_trees = 0

    for i, row in enumerate(grid):
        for j, value in enumerate(grid[i]):
            if is_visible(grid, i, j):
                visible_trees += 1


    return visible_trees


# PART 2: SCORE FCUNTIONS
def get_score_left(grid: list[int], row: int, column: int) -> int:
    score = 0

    for index in reversed(range(column)):
        score += 1
        if grid[row][index] >= grid[row][column]:
            break

    return score

def get_score_right(grid: list[int], row: int, column: int) -> int:
    score = 0

    for index in range(column+1, len(grid[row])):
        score += 1
        if grid[row][index] >= grid[row][column]:
            break

    return score

def get_score_top(grid: list[int], row: int, column: int) -> int:
    score = 0

    for index in reversed(range(row)):
        score += 1
        if grid[index][column] >= grid[row][column]:
            break

    return score

def get_score_bottom(grid: list[int], row: int, column: int) -> int:
    score = 0

    for index in range(row+1, len(grid)):
        score += 1
        if grid[index][column] >= grid[row][column]:
            break

    return score

def get_score(grid: list[list[int]], row: int, column: int) -> int:
    return (
        get_score_left(grid, row, column) *
        get_score_right(grid, row, column) *
        get_score_top(grid, row, column) *
        get_score_bottom(grid, row, column)
    )

def get_score_trees(grid: list[list[int]]) -> int:
    scores = []

    for i, row in enumerate(grid):
        for j, value in enumerate(grid[i]):
            scores.append(get_score(grid, i, j))


    return max(scores)

def main() -> None:
    tree_grid = read_input('2022/day8/input.txt')

    visible_trees  = get_visible_trees(tree_grid)

    print(f'There are {visible_trees} visible trees')

    max_score = get_score_trees(tree_grid)

    print(f'The maximum score is {max_score}')

if __name__ == "__main__":
    main()