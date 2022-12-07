class DataTree:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = {}

    def mkdir(self, name):
        self.children[name] = DataTree(name, parent=self)
        return self.children[name]

    def touch(self, size, name):
        self.files[name] = int(size)

    # stolen hehe c:>

    @property
    def root(self):
        return self if self.parent is None else self.parent.root

    @property
    def size(self):
        return sum(self.files.values()) + sum(child.size for child in self.children.values())

    def __iter__(self):
        for child in self.children.values():
            yield child
            yield from child