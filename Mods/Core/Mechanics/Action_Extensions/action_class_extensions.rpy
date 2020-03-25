init 1 python:
    def action__cmp__(self, other):
        if isinstance(self, other.__class__):
            if self.effect == other.effect:
                return 0

        if self.__hash__() < other.__hash__():
            return -1
        else:
            return 1

    Action.__cmp__ = action__cmp__

    def action__hash__(self):
        return hash(self.effect)

    Action.__hash__ = action__hash__
    Action.hash = action__hash__

    def action_eq(self, other):
        if isinstance(self, other.__class__):
            return self.effect == other.effect
        return False

    Action.__eq__ = action_eq

    def action_ne(self, other):
        if isinstance(self, other.__class__):
            return self.effect != other.effect
        return True

    Action.__ne__ = action_ne    