import os

def read_input(file_name: str) -> list[str]:
    array = []
    with open(file_name) as file:
        for line in file:
            array.append(line.rstrip('\n'))

    return array


def get_elves_calories(calories_array: list[str]) -> list[int]:
    calories_sum = []

    sum = 0
    for element in calories_array:
        if element == '':
            calories_sum.append(sum)
            sum = 0
        else:
            sum += int(element)

    return calories_sum

def get_max_index(array: list[int]) -> (int,int):
    max_value = max(array)
    return array.index(max_value) + 1, max_value

        
def main() -> None:
    input = read_input('day1/input.txt')
    calories_sum = get_elves_calories(input)
    max_index, max_value = get_max_index(calories_sum)
    print(f'The elf with most calories is {max_index} with {max_value}')


if __name__ == "__main__":
    main()