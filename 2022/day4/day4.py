import numpy as np


def read_input(file_name: str) -> np.matrix:
    matrix = np.empty((0,2,2))

    with open(file_name) as file:
        for line in file:
            sections = line.replace('\n','').split(',')
            section_first = sections[0].split('-')
            section_second = sections[1].split('-')
            matrix = np.append(matrix, np.array([[section_first, section_second]]), axis=0)

    return matrix


def first_contains_second(first: np.array, second: np.array) -> bool:
    return int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1])


def overlap(first: np.array, second: np.array) -> bool:
    return int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[0])


def get_intersections_sum(sections_assingment: np.matrix) -> int:
    sum_full = 0
    sum_overlap = 0

    for sections in sections_assingment:
        if first_contains_second(sections[0], sections[1]) or first_contains_second(sections[1], sections[0]):
            sum_full += 1
        if overlap(sections[0], sections[1]) or overlap(sections[1], sections[0]):
            sum_overlap += 1

    return sum_full, sum_overlap


def main() -> None:
    sections_assingment = read_input('2022/day4/input.txt')

    intersections, overlap = get_intersections_sum(sections_assingment)

    print(f'There are {intersections} that fully intersect')
    print(f'There are {overlap} that overlap')

if __name__ == "__main__":
    main()