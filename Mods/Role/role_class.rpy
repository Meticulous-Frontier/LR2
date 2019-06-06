# Replacement for the Role class the solves some shortcomings of the original implementation
# roles don't need to be stored in the renpy storage (an instance gets saved when stored with a parent object that is a store object)
# add comparison so python comparison works based on name

init -1 python:
    class Role(): #Roles are assigned to special people. They have a list of actions that can be taken when you talk to the person and acts as a flag for special dialogue options.
        def __init__(self, role_name, actions):
            self.role_name = role_name
            self.actions = actions # A list of actions that can be taken. These actions are shown when you talk to a person with this role if their requirement is met.
        
        def __cmp__(self,other): # Compare on role_name when comparing to another role otherwise use hash function
            if isinstance(other, Role):
                if self.role_name == other.role_name:
                    return 0

            if self.__hash__() < other.__hash__(): #Use hash values to break ties.
                return -1
            else:
                return 1

        def __hash__(self):
            return hash(self.role_name)
