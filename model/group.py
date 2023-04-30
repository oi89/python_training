from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    # method for string representation for Group object
    def __repr__(self):
        return f"{self.id}:{self.name}:{self.header}:{self.footer}"

    # method for comparing Group objects. If id = None, then we don't compare id.
    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and self.name == other.name

    # method for sort lists, return either id, either very big identifier
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
