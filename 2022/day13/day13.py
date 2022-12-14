def read_input(file_name: str) -> list[str]:
    with open(file_name) as file:
        lines = [ line.rstrip('\n') for line in file]

    return lines

def line_to_list(line: str) -> list:
    my_list = []

    line = line[1:]
    
    contador = 0
    skip = False
    while contador < len(line):
        value = line[contador]
        
        if value == ']':
            if contador < len(line) - 1 and not skip:
                return my_list, contador + 1
            skip = False
        elif value == '[':
            skip = True
            sub_list, sub_contador =  line_to_list(line[contador:])
            contador += sub_contador
            my_list.append(sub_list)
            continue
        elif value != ',' and not skip:
            my_list.append(value)
        
        contador += 1


    return my_list

def compare(line1: str, line2: str) -> int:
    list1 = line1 if isinstance(line1, list) else [line1]
    list2 = line2 if isinstance(line2, list) else [line2]

    for i, value in enumerate(list1):
        if i >= len(list2):
            return 0
        if len(list2[i]) == 0:
            return 0
        if isinstance(value, list) or isinstance(list2[i], list):
            result = compare(value, list2[i])
            if result >= 0:
                return result
            continue
        if value < list2[i]:
            return 1
        if value > list2[i]:
            return 0
    
    return -1

def main() -> None:
    lines = read_input('2022/day13/input.txt')
    
    right_order = 0
    for i in range(0, len(lines), 3):
        result = compare(line_to_list(lines[i]), line_to_list(lines[i+1]))
        if abs(result) > 0:
            right_order += i // 3 + 1

    print(f'The sum of right ordered is {right_order}')



if __name__ == "__main__":
    main()