init -1 python:
    class IT_Project(Policy):
        def __init__(self, name, desc, requirement, cost, toggleable = False,
            on_buy_function = None, extra_arguments = None, on_apply_function = None, on_remove_function = None, on_turn_function = None, on_move_function = None, on_day_function = None, dependant_policies = None,
            project_progress = 0, project_cost = 100, category = "", req_sluttiness = 0):

            super(IT_Project, self).__init__(name, desc, requirement, cost, toggleable, on_buy_function, extra_arguments, on_apply_function, on_remove_function, on_turn_function, on_move_function, on_day_function, dependant_policies)
            self.project_progress = project_progress
            self.project_cost = project_cost
            self.category = category
            self.req_sluttiness = req_sluttiness


        def buy_policy(self, ignore_cost = False):  #Only use this function if an IT Project can be outright bought.
            mc.business.policy_list.append(self)
            if not ignore_cost:
                mc.business.funds -= self.cost
            if self.on_buy_function is not None:
                self.on_buy_function(**self.extra_arguments)
