init -1 python:

    def serum_trait_compare(self,other): 
        if isinstance(other, SerumTrait):
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