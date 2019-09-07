init 2 python:
    def policy_compare(self,other): #
        if isinstance(other, Policy):
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

    def update_policy(policy, policy_list): # Arguments such as rooms are not up to date on save reloads
        policy_to_update = find_in_list(lambda x: x.name == policy.name, policy_list)
        if not policy_to_update:
            return

        policy_to_update.name = policy.name
        policy_to_update.cost = policy.cost
        policy_to_update.desc = policy.desc
        policy_to_update.requirement = policy.requirement
        policy_to_update.on_buy_arguments = policy.on_buy_arguments

        return policy_to_update
