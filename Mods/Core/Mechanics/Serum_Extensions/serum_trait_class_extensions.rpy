init -1 python:

    def serum_trait_compare(self,other): 
        if isinstance(other, other.__class__):
            if self.name == other.name:
                return 0

        if self.__hash__() < other.__hash__():
            return -1
        else:
            return 1

    SerumTrait.__cmp__ = serum_trait_compare

    def serum_trait_hash(self):
        return hash(self.name)

    SerumTrait.__hash__ = serum_trait_hash
    SerumTrait.hash = serum_trait_hash

    def serum_trait_eq(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name
        return False

    SerumTrait.__eq__ = serum_trait_eq

    def serum_trait_ne(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name
        return True

    SerumTrait.__ne__ = serum_trait_ne
