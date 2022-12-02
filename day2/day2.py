import numpy as np

encrypted_first = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

encrypted_second = {
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

points = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3,
    'Win': 6,
    'Drawn': 3,
    'Loose': 0 
}

results = {
    'Rock': {
        'Rock': 'Drawn',
        'Paper': 'Win',
        'Scissors': 'Loose'
    },
    'Paper': {
        'Rock': 'Loose',
        'Paper': 'Drawn',
        'Scissors': 'Win'
    },
    'Scissors': {
        'Rock': 'Win',
        'Paper': 'Loose',
        'Scissors': 'Drawn'
    },

}

end_strategy = {
    'X': 'Loose',
    'Y': 'Drawn',
    'Z': 'Win'
}

second_choose = {
    'Rock': {
        'Loose': 'Scissors',
        'Drawn': 'Rock',
        'Win': 'Paper'
    },
    'Paper': {
        'Loose': 'Rock',
        'Drawn': 'Paper',
        'Win': 'Scissors'
    },
    'Scissors': {
        'Loose': 'Paper',
        'Drawn': 'Scissors',
        'Win': 'Rock'
    },

}

def read_input(file_name: str) -> list[str]:
    matrix = np.loadtxt(file_name, dtype='str', delimiter=' ')

    return matrix


def get_points_part1(first: str, second: str) ->int:

    result = results[encrypted_first[first]][encrypted_second[second]]

    return points[result] + points[encrypted_second[second]]

def get_points_part2(first: str, second: str) -> int:
    choose = second_choose[encrypted_first[first]][end_strategy[second]]

    return points[end_strategy[second]] + points[choose]


def get_total_points_part1(strategy) -> int:
    points = 0
    for match in strategy:
        points += get_points_part1(match[0],match[1])

    return points

def get_total_points_part2(strategy) -> int:
    points = 0
    for match in strategy:
        points += get_points_part2(match[0],match[1])
        parada = 0

    return points


def main() -> None:
    strategy = read_input('day2/input.txt')

    points = get_total_points_part1(strategy)

    print(f'The score in part 1 is {points}')

    points2 = get_total_points_part2(strategy)

    print(f'The score in part2 1 is {points2}')

if __name__ == "__main__":
    main()