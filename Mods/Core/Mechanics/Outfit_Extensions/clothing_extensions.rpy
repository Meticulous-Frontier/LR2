init -1 python:
    ###############################################
    # Custom Compare Functions For Clothing Class #
    ###############################################
    def clothing_compare(self, other):
        if isinstance(self, other.__class__):
            if self.name == other.name:
                return 0

        if self.__hash__() < other.__hash__():
            return -1
        else:
            return 1

    Clothing.__cmp__ = clothing_compare

    # add clothing hash function
    def clothing_hash(self):
        return hash(self.name)

    Clothing.__hash__ = clothing_hash
    Clothing.hash = clothing_hash

    def clothing_eq(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name
        return False

    Clothing.__eq__ = clothing_eq

    def clothing_ne(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name
        return True

    Clothing.__ne__ = clothing_ne
