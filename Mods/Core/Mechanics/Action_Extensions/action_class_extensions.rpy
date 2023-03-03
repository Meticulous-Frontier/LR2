init 1 python:
    def action__cmp__(self, other):
        if isinstance(self, other.__class__):
            if self.effect == other.effect and self.args == other.args:
                return 0

        if self.__hash__() < other.__hash__():
            return -1
        else:
            return 1

    Action.__cmp__ = action__cmp__

    def action__hash__(self):
        return hash(tuple([self.effect] + self.args))

    Action.__hash__ = action__hash__
    Action.hash = action__hash__

    def action_eq(self, other):
        if isinstance(self, other.__class__):
            return self.effect == other.effect and self.args == other.args
        return False

    Action.__eq__ = action_eq

    def action_ne(self, other):
        if isinstance(self, other.__class__):
            return self.effect != other.effect and self.args == other.args
        return True

    Action.__ne__ = action_ne


    def get_action_enabled(self):
        if not hasattr(self, "_enabled"):
            self._enabled = True
        return self._enabled

    def set_action_enabled(self, value):
        self._enabled = value

    Action.enabled = property(get_action_enabled, set_action_enabled, None, "Is the action enabled.")

    def is_action_enabled(self, extra_args = None):
        if not self.enabled:
            return False

        requirement_return = self.check_requirement(extra_args)
        if isinstance(requirement_return, basestring):
            # Any string returned means the action is not enabled
            return False
        # If it's not a string it must be a bool
        return requirement_return

    def is_disabled_slug_shown(self, extra_args = None): # Returns true if this action is not enabled but should show something when it is disabled.
        if not self.enabled:
            return False

        requirement_return = self.check_requirement(extra_args)
        if isinstance(requirement_return, basestring):
            return True
        return False

    # Monkeywrench the action method overrides in the Action class
    Action.is_action_enabled = is_action_enabled
    Action.is_disabled_slug_shown = is_disabled_slug_shown

    def update_action(self, action):
        self.name = action.name
        self.effect = action.effect
        self.requirement = action.requirement
        self.args = action.args
        self.menu_tooltip = action.menu_tooltip
        self.priority = action.priority
        self.event_duration = action.event_duration
        self.is_fast = action.is_fast
        return

    Action.update_action = update_action

    # hook for logging executed actions
    def call_action_extended(org_func):
        def call_action_wrapper(action, extra_args = None):
            # run extension code
            if debug_log_enabled:
                add_to_debug_log("Action: " + remove_display_tags(action.name) + " ({total_time:.3f})", time.time())

            # run original function
            org_func(action, extra_args)

        return call_action_wrapper

    # wrap up the call_action function
    Action.call_action = call_action_extended(Action.call_action)
