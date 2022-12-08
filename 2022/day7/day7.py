import re
from tree import Tree

def read_input(file_name: str) -> Tree:
    with open(file_name) as file:
        lines = [ line[:-1] for line in file ]


    tree = Tree('/')
    tree = read_tree(tree, lines, 1)

    return tree

def read_tree(tree_padre: Tree, lines: list[str], contador: int) -> tuple[Tree,int]:

    if contador >= len(lines):
        return tree_padre, contador

    match = re.search('\$ cd ((?!\.\.).+)', lines[contador])
    if match is not None:
        tree_hijo = Tree(match.group(1)) 
        tree_hijo, contador = read_tree(tree_hijo, lines, contador + 1)
        tree_padre.add_children(tree_hijo)

        tree_padre, contador = read_tree(tree_padre, lines, contador + 1)

        return tree_padre, contador


    match = re.search('\$ ls', lines[contador])
    if match is not None:
        tree_padre, contador = read_tree(tree_padre, lines, contador + 1)

        return tree_padre, contador

    match = re.search('(\d+) ((.|\.)+)', lines[contador])
    if match is not None:
        tree_archivo = Tree(match.group(2), match.group(1))
        tree_padre.add_children(tree_archivo)

        tree_padre, contador = read_tree(tree_padre, lines, contador + 1)

        return tree_padre, contador

    match = re.search('dir (.+)', lines[contador])
    if match is not None:
        tree_padre, contador = read_tree(tree_padre, lines, contador + 1)

        return tree_padre, contador

    return tree_padre, contador
    

def main() -> None:
    file_system = read_input('2022/day7/input.txt')

    parada = 0


if __name__ == "__main__":
    main()