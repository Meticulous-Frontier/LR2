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


    def get_enabled_on_buy(self):
        if not hasattr(self, "_enabled_on_buy"):
            self._enabled_on_buy = True
        return self._enabled_on_buy

    def set_enabled_on_buy(self, value):
        self._enabled_on_buy = value
    
    Policy.enabled_on_buy = property(get_enabled_on_buy, set_enabled_on_buy, None, "Enable policy when bought, ignored when not toggleable.")


    # Override default purchase policy function to evaluate 'enabled_on_buy'
    def purchase_policy(the_policy, ignore_cost = False):
        the_policy.buy_policy(ignore_cost = ignore_cost)
        if not the_policy.toggleable or (the_policy.is_toggleable() and the_policy.enabled_on_buy):
            the_policy.apply_policy()
