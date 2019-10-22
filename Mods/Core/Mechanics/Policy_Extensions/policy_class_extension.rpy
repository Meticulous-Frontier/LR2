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




    class ModPolicy(Policy): # Allows you to attach parent / child relation to the policies which display when the parent is selected.

        def __init__(self, name, desc, requirement, cost, on_buy_function = None, on_buy_arguments = None, parent = None, image = None, enabled = False, upgrade = False, refresh = None):

            Policy.__init__(self, name, desc, requirement, cost, on_buy_function, on_buy_arguments)
            self.children = [] # A list that gets filled with child elements
            self.parent = parent # A list of optional policies that can be toggled on / off

            if self.parent:
                if not hasattr(self.parent, "children"): # Allow non- ModPolicy (normal Policy) class to be used as parents
                    self.parent.children = []
                if self not in parent.children:
                    self.parent.children.append(self)
                else: # Use something like this to refresh attributes. The self.refresh is the same label that initializes the ModPolicy
                    self.parent.children[self.parent.children.index(self)].cost = self.cost


            self.upgrade = upgrade # A multi- stage or endless policy upgrade must be set to True so that it doesn't become "purchased" | is_owned() == True
            self.refresh = refresh # Set this to the label that creates the policy in the first place. This will refresh descriptions, cost, parents etc.
            self.enabled = enabled # Whether the policy is active or not
            self.image = image # Image background or icons to use?

    # def buy_mod_policy(self): # Allows for lists to be used when running functions on purchase
    #     mc.business.funds -= self.cost
    #     if self.on_buy_function is not None and type(self.on_buy_function) is list: # TODO: Find a better way to call listed functions in order with arguments.
    #         count = 0
    #         while count < len(self.on_buy_function):
    #             self.on_buy_function[count](self.on_buy_arguments[str(count)])
    #             count += 1
    #     else:
    #         if self.on_buy_function is not None:
    #             self.on_buy_function(**self.on_buy_arguments)
    #
    #     Policy.buy_mod_policy = buy_mod_policy
