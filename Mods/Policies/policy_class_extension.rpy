init 2:
    python:
        def policy_compare(self,other): #
            if type(other) is Policy:
                if self.name == other.name:
                    return 0
                else:
                    if self.__hash__() < other.__hash__(): #Use hash values to break ties.
                        return -1
                    else:
                        return 1

            else:
                if self.__hash__() < other.__hash__(): #Use hash values to break ties.
                    return -1
                else:
                    return 1

        Policy.__cmp__ = policy_compare

        def policy_hash(self):
            return hash(self.name)

        Policy.__hash__ = policy_hash
