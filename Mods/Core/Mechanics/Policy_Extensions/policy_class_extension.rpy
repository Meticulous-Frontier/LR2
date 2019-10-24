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

    def buy_policy_enhanced(self, alternate_click = False):

        if hasattr(self, "upgrade"):
            upgrade = self.upgrade
        else:
            upgrade = False

        if not hasattr(self, "enabled"):
            self.enabled = False


        if alternate_click is True: # This is true if you right click the policy in the policy_selection_screen
            if self.alternate_on_buy_arguments is not None:
                self.on_buy_function(**self.alternate_on_buy_arguments)
                if hasattr(self, "refund"):
                    mc.business.pay(+self.refund)
            if upgrade is False: # If it is not an upgrade or normal policy it is disabled / sold when right clicking. purchase_policy() is where it is appended.
                if self in mc.business.policy_list:
                    mc.business.policy_list.remove(self)
        else:
            if self.on_buy_function is not None:
                self.on_buy_function(**self.on_buy_arguments)
            if upgrade is False:
                mc.business.policy_list.append(self)
                if type(self) is ModPolicy and not self.enabled:
                    self.enabled = True # Marks it as enabled and no longer need to re- purchase it
                    mc.business.pay(-self.cost) # Currently do not deduct cost for the alternate_on_buy_arguments

            if not self.enabled:
                mc.business.pay(-self.cost) # Currently do not deduct cost for the alternate_on_buy_arguments
                self.refund = self.cost

    Policy.buy_policy = buy_policy_enhanced # Allows alternate usage for right clicking etc.


    class ModPolicy(Policy): # Allows you to attach parent / child relation to the policies which display when the parent is selected.

        def __init__(self, name, desc, requirement, cost, on_buy_function = None, on_buy_arguments = None, alternate_on_buy_arguments = None, parent = None, image = None, upgrade = False, refresh = None):

            Policy.__init__(self, name, desc, requirement, cost, on_buy_function, on_buy_arguments)
            self.children = [] # A list that gets filled with child elements
            self.parent = parent # The parent of a policy is where you want it to be subcatagorized

            if self.parent:
                if not hasattr(self.parent, "children"): # Allow non- ModPolicy (normal Policy) class to be used as parents
                    self.parent.children = []

                if self not in parent.children:
                    self.parent.children.append(self)
                else: # Use something like this to refresh attributes. The self.refresh is the same label that initializes the ModPolicy
                    self.parent.children[self.parent.children.index(self)].cost = self.cost
                    self.parent.children[self.parent.children.index(self)].desc = self.desc # Some text can't be interpolated e.g the return of a function

            self.alternate_on_buy_arguments = alternate_on_buy_arguments # Arguments sent to on_buy_function when right clicking in policy_selection_screen
            self.upgrade = upgrade # A multi- stage or endless policy upgrade must be set to True so that it doesn't become "purchased" | is_owned() == True
            self.refresh = refresh # Set this to the label that creates the policy in the first place. This will refresh descriptions, cost, parents etc.
            self.image = image # Image background or icons to use?
            self.enabled = False
            #if self.parent:
            #    self.enabled = self.parent.children[self.parent.children.index(self)].enabled

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
