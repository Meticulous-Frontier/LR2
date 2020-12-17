
init -1 python:
    # Compare on object name when comparing to another object otherwise use hash function
    def object_compare(self,other):
        if isinstance(self, other.__class__):
            if self.name == other.name:
                return 0

        if self.__hash__() < other.__hash__(): #Use hash values to break ties.
            return -1
        else:
            return 1

    Object.__cmp__ = object_compare

    def object_hash(self):
        return hash(self.name)

    Object.__hash__ = object_hash

    def object_eq(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name
        return False

    Object.__eq__ = object_eq

    def object_ne(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name
        return True

    Object.__ne__ = object_ne
