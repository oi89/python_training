from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    # функция для строкового представления объекта Group
    def __repr__(self):
        return f"{self.id}: {self.name}"

    # функция для сравнения объектов Group. Если id = None, то не сравниваем id.
    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and self.name == other.name

    # функция для сортировки списков, возвращает либо id, либо очень большой идентификатор
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
