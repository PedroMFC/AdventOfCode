import re
from tree import Tree

def read_input(file_name: str) -> Tree:
    with open(file_name) as file:
        lines = [ line[:-1] for line in file ]

    tree = read_tree(lines, 0)

    return tree

def read_tree(lines: list[str], contador: int) -> tuple[Tree,int]:
    tree = None
    mi_contador = contador

    if re.search('\$ cd ((?!..).+)', lines[mi_contador]):
        contador +=1
        tree, mi_contador = read_tree(lines, mi_contador)
    elif re.search('', lines[mi_contador])
    else: # re.search('\$ cd ..', lines[mi_contador]):
        return tree, mi_contador
    

def main() -> None:
    file_system = read_input('2022/day7/input.txt')


if __name__ == "__main__":
    main()