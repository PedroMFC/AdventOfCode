
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
    return array.index(max_value), max_value

def get_three_max_values(array: list[int]) -> int:
    max_values = 3

    sum = 0
    for i in range(3):
        index, value = get_max_index(array)
        sum += value
        array.pop(index)

    return sum
        
def main() -> None:
    input = read_input('day1/input.txt')
    calories_sum = get_elves_calories(input)

    max_index, max_value = get_max_index(calories_sum)
    print(f'The elf with most calories is {max_index + 1} with {max_value}')

    sum_three_elves = get_three_max_values(calories_sum)
    print(f'The elves with more calories sum {sum_three_elves}')


if __name__ == "__main__":
    main()