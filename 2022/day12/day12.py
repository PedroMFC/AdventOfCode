class Node:
    def __init__(self, position: tuple[int, int]):
        self.postion = position
        self.real_cost = 0
        self.heuristic_cost = 0
        self.parent = None

    def set_parent(self, parent) -> None:
        self.parent = parent

    def get_parent(self):
        return self.parent

    def get_position(self) -> tuple[int, int]:
        return self.postion

    def set_real_cost(self, real_cost: int) -> None:
        self.real_cost = real_cost

    def get_real_cost(self) -> int:
        return self.real_cost

    def get_heuristic_cost(self) -> int:
        return self.heuristic_cost

    def get_total_cost(self) -> int:
        return self.get_real_cost() + self.get_heuristic_cost()

    def calculate_heuristic_cost(self, dest: tuple[int, int]) -> None:
        self.heuristic_cost = abs(self.postion[0] - dest[0]) + abs(self.postion[1] - dest[1])

    def __cmp__(self, obj) -> int:
        if self.get_total_cost() < obj.get_total_cost():
            return -1
        
        if self.get_total_cost() > obj.get_total_cost():
            return 1

        return 0

    def __eq__(self, obj) -> bool:
        return self.postion == obj.get_position()

    def __lt__(self, other):
        return self.get_total_cost() < other.get_total_cost()



def read_input(file_name: str) -> list[list[str]]:
    area = []

    with open(file_name) as file:
        for line in file:
            characters = [ char for char in line[:-1] ]
            area.append(characters)


    return area

def calculate_position(area: list[list[str]], character: str) -> tuple[int,int]:

    for i, row in enumerate(area):
        for j, value in enumerate(row):
            if value == character:
                return (i,j)

    return (None, None)


def can_be_reached(origen: str, destino: str) -> bool:
    if origen == 'S':
        origen = 'a'
    if destino == 'E':
        destino = 'z'
    
    return ord(destino) <= ord(origen) + 1

def valid_position(postion: tuple[int, int], num_rows: int, num_columns: int) -> bool:
    return postion[0] >= 0 and postion[0] < num_rows and postion[1] >= 0 and postion[1] < num_columns

'''
https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
'''

def calculate_path(area: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> list[Node]:
    num_rows = len(area)
    num_columns = len(area[0])

    open_list = [Node((start[0], start[1]))]
    close_list = []
    end_node = Node((end[0], end[1]))


    while len(open_list) > 0:
        actual_node = open_list[0]
        actual_position = actual_node.get_position()

        open_list.pop(0)
        close_list.append(actual_node)

        if actual_node == end_node:
            path = []
            actual = actual_node

            while actual is not None:
                path.append(actual)
                actual = actual.get_parent()
            return path

        children = []
        for new_position in [ (0,1), (1, 0), (0, -1), (-1,0) ]:
            node_position = (actual_position[0] - new_position[0], actual_position[1] - new_position[1])

            if ( not valid_position(node_position, num_rows, num_columns) or
                 not can_be_reached(area[actual_position[0]][actual_position[1]], area[node_position[0]][node_position[1]])):
                 continue

            child = Node(node_position)
            child.set_parent(actual_node)
            children.append(child)


        for child in children:

            child_is_closed = list(filter(lambda node_child: child == node_child, close_list))
            if len(child_is_closed) > 0:
                continue

            child.set_real_cost(actual_node.get_real_cost() + 1)
            child.calculate_heuristic_cost(end_node.get_position())

            insert_child = True
            for index, open_child in enumerate(open_list):
                if child == open_child:
                    if child.get_total_cost() < open_child.get_total_cost():
                        open_list.pop(index)
                    else:
                        insert_child = False
                    break

            if insert_child:
                open_list.append(child)
            

        open_list.sort()

def calculate_reverse_path(area: list[list[str]], start: tuple[int, int], search_str: str) -> list[Node]:
    num_rows = len(area)
    num_columns = len(area[0])

    open_list = [Node((start[0], start[1]))]
    close_list = []

    while len(open_list) > 0:
        actual_node = open_list[0]
        actual_position = actual_node.get_position()

        open_list.pop(0)
        close_list.append(actual_node)

        if area[actual_position[0]][actual_position[1]] == search_str:
            path = []
            actual = actual_node

            while actual is not None:
                path.append(actual)
                actual = actual.get_parent()
            return path

        children = []
        for new_position in [ (0,1), (1, 0), (0, -1), (-1,0) ]:
            node_position = (actual_position[0] - new_position[0], actual_position[1] - new_position[1])

            if ( not valid_position(node_position, num_rows, num_columns) or
                not can_be_reached(area[node_position[0]][node_position[1]], area[actual_position[0]][actual_position[1]])):
                continue

            child = Node(node_position)
            child.set_parent(actual_node)
            children.append(child)


        for child in children:

            child_is_closed = list(filter(lambda node_child: child == node_child, close_list))
            if len(child_is_closed) > 0:
                continue

            child.set_real_cost(child.get_parent().get_real_cost() + 1)

            insert_child = True
            for index, open_child in enumerate(open_list):
                if child == open_child:
                    if child.get_real_cost() < open_child.get_real_cost():
                        open_list.pop(index)
                    else:
                        insert_child = False
                    break

            if insert_child:
                open_list.append(child)
            

        open_list.sort()

def main() -> None:
    area = read_input('2022/day12/input.txt')

    path = calculate_path(area, calculate_position(area, 'S'), calculate_position(area, 'E'))
    
    print(f'The fewest step from S required are {len(path)-1}')

    a_path = calculate_reverse_path(area, calculate_position(area, 'E'), 'a')

    print(f'The fewest step from any a required are {len(a_path)-1}')

if __name__ == "__main__":
    main()