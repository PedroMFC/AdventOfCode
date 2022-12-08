class Tree:

    def __init__(self, name, size = 0 ):
        self.name = name
        self.children = []
        self.size = size

    def add_children(self, child):
        self.children.append(child)

    def get_name(self):
        return self.name
    
    def get_children(self):
        return self.children

    def is_node(self):
        return self.size != 0

    def get_size(self):
        size = 0
        if self.is_node():
            size =  self.size
        else:
            for child in self.children:
                size += child.get_size()

        return size

    
    



