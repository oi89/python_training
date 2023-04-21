class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    # функция для строкового представления объекта Group
    def __repr__(self):
        return f"{self.id}: {self.name}"

    # функция для сравнения объектов Group
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
