import re
from tree import Tree

def read_input(file_name: str) -> Tree:
    with open(file_name) as file:
        lines = [ line[:-1] for line in file ]


    tree = Tree('/')
    tree, contador = read_tree(tree, lines, 1)

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
        tree_archivo = Tree(match.group(2), int(match.group(1)))
        tree_padre.add_children(tree_archivo)

        tree_padre, contador = read_tree(tree_padre, lines, contador + 1)

        return tree_padre, contador

    match = re.search('dir (.+)', lines[contador])
    if match is not None:
        tree_padre, contador = read_tree(tree_padre, lines, contador + 1)

        return tree_padre, contador

    return tree_padre, contador # cd ..

def get_sizes(tree: Tree) -> list[int]:
    sizes = []

    if not tree.is_node():
        sizes.append(tree.get_size())
        for child in tree.get_children():
            sizes_child = get_sizes(child)
            for size_child in sizes_child:
                sizes.append(size_child)

    return sizes

def get_directory_to_delete(sizes: list[int]) -> int:
    max_space = 70000000
    spaced_needed = 30000000
    unused_space = max_space - max(sizes)
    space_to_free = spaced_needed - unused_space

    result_space_free = [ size - space_to_free for size in sizes ]

    result_space_free.sort(key= lambda size: max_space if size < 0 else size) # max_space is random. We want e a huge number that discard (send to last positions) sizes that will not give us enough space

    return result_space_free[0] + space_to_free # Recover size of the direcotry


    
def get_sizes_most(sizes: list[int], max: int) -> int:
    sum = 0

    for size in sizes:
        if size < max:
            sum += size

    return sum


def main() -> None:
    file_system = read_input('2022/day7/input.txt')

    sizes = get_sizes(file_system)
    sizes_most_100000 = get_sizes_most(sizes, 100000)

    print(f'The sum  of directories with size at most 100000 is {sizes_most_100000}')

    directory_to_delete = get_directory_to_delete(sizes)

    print(f'The directory to delete has size {directory_to_delete}')

if __name__ == "__main__":
    main()