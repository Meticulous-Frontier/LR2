init 2 python:
    def policy_compare(self,other): #
        if isinstance(self, other.__class__):
            if self.name == other.name:
                return 0

        if self.__hash__() < other.__hash__():
            return -1
        else:
            return 1

    Policy.__cmp__ = policy_compare

    def policy_hash(self):
        return hash(self.name)

    Policy.__hash__ = policy_hash
    Policy.hash = policy_hash

    def policy_eq(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name
        return False

    Policy.__eq__ = policy_eq

    def policy_ne(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name
        return True

    Policy.__ne__ = policy_ne
