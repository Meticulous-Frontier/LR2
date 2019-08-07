init -1 python:
    def clothing_compare(self, other):
        if isinstance(other, Clothing):
            if self.proper_name == other.proper_name:
                return 0

        if self.__hash__() < other.__hash__(): #Use hash values to break ties.
            return -1
        else:
            return 1

    Clothing.__cmp__ = clothing_compare

    def clothing_hash(self):
        return hash(self.proper_name)

    Clothing.__hash__ = clothing_hash