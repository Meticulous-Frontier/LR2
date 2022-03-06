
init -1 python:
    def goal__init__(self, goal_name, goal_description, event_name, listener_type, valid_goal_function, on_trigger_function, arg_dict = None, difficulty_scale_function = None, report_function = None, progress_fraction_function = None, mandatory = False, enabled = True):
        self.name = goal_name #Short form name to be displayed to the player, generally on a progress bar of some sort.
        self.description = goal_description #A long form fluff description of the goal purpose.
        self.event_name = event_name #The event (aka a string to give to a listener manager) that this goal listens to.
        self.listener_type = listener_type #Either "MC" or "Business", decides which object the goal will grab as their listener manager when you ask it to enroll.
        self.valid_goal_function = valid_goal_function #A function called to check to see if the goal is a valid/reasonable one to give to the player. Also is used to make sure goals aren't completed when they are assigned.
        self.on_trigger_function = on_trigger_function #A function called by an event listener that that this goal is hooked up to.
        if arg_dict: #A dict to hold arguments you want to be used by the on_trigger function without having to get specific about what they are here.
            self.arg_dict = arg_dict
        else:
            self.arg_dict = {}

        self.completed = False #A flag set to true when the goal is finished, so the player can complete the objective and claim their bonus point.

        self.difficulty_scale_function = difficulty_scale_function #A function called when the goal is activated (aka when it is copied from the default goal) to scale the parameters to the current difficulty.
        self.report_function = report_function
        self.progress_fraction_function = progress_fraction_function
        self.mandatory = mandatory
        self.enabled = enabled

    Goal.__init__ = goal__init__

    def goal_toggle_enabled(self):
        def enable_in_list(the_goal, the_list):
            found = next((x for x in the_list if x.name == the_goal.name), None)
            if not found:
                the_list.append(the_goal)
                the_goal.enabled = True

        def disable_in_list(the_goal, the_list):
            if __builtin__.len(the_list) < 3: # minimum of two active items
                return
            found = next((x for x in the_list if x.name == the_goal.name), None)
            if found:
                the_list.remove(found)
                the_goal.enabled = False

        #renpy.notify(self.name + " is now [" + str(hex(id(self))) + "] :" + str(self.enabled))
        if not self.enabled:
            if self in stat_goals_options_list:
                enable_in_list(self, stat_goals)
            if self in work_goals_options_list:
                enable_in_list(self, work_goals)
            if self in sex_goals_options_list:
                enable_in_list(self, sex_goals)
        else:
            if self in stat_goals_options_list:
                disable_in_list(self, stat_goals)
            if self in work_goals_options_list:
                disable_in_list(self, work_goals)
            if self in sex_goals_options_list:
                disable_in_list(self, sex_goals)
        return

    Goal.toggle_enabled = goal_toggle_enabled

    def goal__cmp__(self, other):
        if isinstance(self, other.__class__):
            if self.name == other.name:
                return 0

        if self.__hash__() > other.__hash__():
            return 1
        else:
            return -1

    Goal.__cmp__ == goal__cmp__

    def goal__hash__(self):
        return hash(self.name)

    Goal.__hash__ = goal__hash__
    Goal.hash = goal__hash__

    def goal_eq(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name
        return False

    Goal.__eq__ = goal_eq

    def goal_ne(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name
        return True

    Goal.__ne__ = goal_ne

init 2 python:
    # replace existing create functions to prevent goal repetition (caused by random selection).
    def create_new_stat_goal(goal_difficulty, recursion = 0):
        if recursion < 5:
            potential_goal = get_random_from_list(list(set(stat_goals) - set([mc.stat_goal])))
        else:
            potential_goal = get_random_from_list(stat_goals)

        if potential_goal.check_valid(goal_difficulty) or recursion > 10: # forced exit add random goal even if not valid.
            goal_template = copy.deepcopy(potential_goal)
            goal_template.activate_goal(goal_difficulty)
            return goal_template
        else:
            return create_new_stat_goal(goal_difficulty, recursion + 1) #Quick and dirty recursion to cycle through and get a goal. Note: Explodes if we don't have a goal.

    def create_new_work_goal(goal_difficulty, recursion = 0):
        if recursion < 5:
            potential_goal = get_random_from_list(list(set(work_goals) - set([mc.work_goal])))
        else:
            potential_goal = get_random_from_list(work_goals)

        if potential_goal.check_valid(goal_difficulty) or recursion > 10: # forced exit add random goal even if not valid.
            goal_template = copy.deepcopy(potential_goal)
            goal_template.activate_goal(goal_difficulty)
            return goal_template
        else:
            return create_new_work_goal(goal_difficulty, recursion + 1) #Quick and dirty recursion to cycle through and get a goal. Note: Explodes if we don't have a goal.

    def create_new_sex_goal(goal_difficulty, recursion = 0):
        if recursion < 5:
            potential_goal = get_random_from_list(list(set(sex_goals) - set([mc.sex_goal])))
        else:
            potential_goal = get_random_from_list(sex_goals)

        if potential_goal.check_valid(goal_difficulty) or recursion > 10: # forced exit add random goal even if not valid.
            goal_template = copy.deepcopy(potential_goal)
            goal_template.activate_goal(goal_difficulty)
            return goal_template
        else:
            return create_new_sex_goal(goal_difficulty, recursion + 1) #Quick and dirty recursion to cycle through and get a goal. Note: Explodes if we don't have a goal.
