# Add object comparison and hash function to the Role class

init -1 python:
    # Compare on role_name when comparing to another role otherwise use hash function
    def role_compare(self,other):
        if isinstance(self, other.__class__):
            if self.role_name == other.role_name:
                return 0

        if self.__hash__() < other.__hash__(): #Use hash values to break ties.
            return -1
        else:
            return 1

    Role.__cmp__ = role_compare

    def role_hash(self):
        return hash(self.role_name)

    Role.__hash__ = role_hash
    Role.hash = role_hash

    def role_eq(self, other):
        if isinstance(self, other.__class__):
            return self.role_name == other.role_name
        return False

    Role.__eq__ = role_eq

    def role_ne(self, other):
        if isinstance(self, other.__class__):
            return self.role_name != other.role_name
        return True

    Role.__ne__ = role_ne   

    def add_action(self, act):
        if not act in self.actions:
            self.actions.append(act)

    Role.add_action = add_action

    def remove_action(self, act):
        if act in self.actions:
            self.actions.remove(act)

    Role.remove_action = remove_action
