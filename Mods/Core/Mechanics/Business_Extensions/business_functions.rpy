init -1 python:
    def change_funds(self, amount, add_to_log = True):
        self.funds += __builtin__.int(amount)

        if add_to_log:
            if amount >= 0:
                mc.log_event(self.name + " received: " + "$" + str(__builtin__.abs(amount)), "float_text_green")
            else:
                mc.log_event(self.name + " paid: " + "$" + str(__builtin__.abs(amount)), "float_text_green")
        return

    # Add Pay function to business object
    Business.change_funds = change_funds

    def supply_purchase_enhanced(self,focus,cha,skill):
        max_supply = __builtin__.int(((5*focus) + (3*cha) + (3*skill) + 20) * (self.team_effectiveness / 100.0))
        if (self.supply_count / self.supply_goal) < 20 and self.supply_count < 250 and mc.business.IT_project_is_active(supply_inventory_project):
            max_supply *= 1.25
        if max_supply + self.supply_count > self.supply_goal:
            max_supply = self.supply_goal - self.supply_count
            if max_supply <= 0:
                return 0

        max_supply = __builtin__.int(max_supply)

        self.funds -= __builtin__.round(max_supply * candace_calculate_discount(), 1)
        self.supply_count += max_supply
        self.supplies_purchased += max_supply #Used for end of day reporting
        return max_supply

    Business.supply_purchase = supply_purchase_enhanced

    def is_trait_researched(self, trait):
        if isinstance(trait, basestring):
            research_trait = find_in_list(lambda x: x.name.startswith(trait), list_of_traits) # As long as the naming convention of the serums are consistent then this should be a lazy workaround for not having them accessible in the global scope anymore
        else:
            research_trait = find_in_list(lambda x: x.name == trait.name, list_of_traits)
        if research_trait:
            return research_trait.researched
        return False

    Business.is_trait_researched = is_trait_researched

    def setup_employee_stats(person): #Centralized function for setting up employee stuff when you hire them
        if person.event_triggers_dict.get("employed_since", -1) == -1: # prevent fire / hire loop event triggering
            person.event_triggers_dict["employed_since"] = day
            mc.business.listener_system.fire_event("new_hire", the_person = person)
            for other_employee in mc.business.get_employee_list():
                town_relationships.begin_relationship(person, other_employee) #They are introduced to everyone at work, with a starting value of "Acquaintance"

        # set names when hiring (if not set)
        if not person.title:
            person.set_title(get_random_title(person))
        if not person.possessive_title:
            person.set_possessive_title(get_random_possessive_title(person))
        if not person.mc_title or person.mc_title == "Stranger":
            person.set_mc_title(get_random_player_title(person))

        # make sure she is dressed appropriately
        person.apply_outfit()

    def all_IT_projects():
        return [x for x in business_IT_project_list + nanobot_IT_project_list]

    def IT_projects(self):
        if not hasattr(self, "_IT_project_map"):
            self._IT_project_map = MappedList(IT_Project, all_IT_projects)
        return self._IT_project_map

    Business.IT_projects = property(IT_projects, None, None, "Owned IT Project List")

    def active_IT_projects(self):
        if not hasattr(self, "_active_IT_project_map"):
            self._active_IT_project_map = MappedList(IT_Project, all_IT_projects)
        return self._active_IT_project_map

    Business.active_IT_projects = property(active_IT_projects, None, None, "Active IT Project List")

    Business.IT_project_in_progress = None

    Business.IT_partial_projects = {}

    def set_active_IT_project(project):
        if mc.business.IT_project_in_progress != None:
            if mc.business.IT_project_in_progress[0] == project.identifier:
                return
        if mc.business.IT_project_in_progress and mc.business.IT_project_in_progress[1] < mc.business.IT_project_in_progress[0].project_cost and mc.business.IT_project_in_progress[1] > 0:
            mc.business.IT_partial_projects[mc.business.IT_project_in_progress[0].identifier] = mc.business.IT_project_in_progress[1]    #Stores the current progress of this project.
        if mc.business.IT_partial_projects.has_key(project.identifier):
            mc.business.IT_project_in_progress = [project,  mc.business.IT_partial_projects.get(project.identifier, 0)]
            mc.business.IT_partial_projects.pop(project.identifier, None)
        else:
            mc.business.IT_project_in_progress = [project, 0]  #SEcond variable 0 is for project progress. Default to 0 when starting a new project.
        return

    def IT_toggle_project(project):
        if project in mc.business.active_IT_projects:
            project.remove_policy()
            # print("Toggle project: " + project.name + " -> Removed")
        else:
            project.apply_policy()
            # print("Toggle project: " + project.name + " -> Added")

    def IT_increase_project_progress(self, amount = 0, add_to_log = False):
        if not self.IT_project_in_progress:
            return
        self.IT_project_in_progress[1] += amount
        if add_to_log:
            mc.log_event( "+" + str(amount) + " IT Project Progress", "float_text_green")
        if self.IT_project_in_progress[1] >= self.IT_project_in_progress[0].project_cost:
            self.IT_unlock_project(self.IT_project_in_progress[0])
            self.IT_project_in_progress = None
            self.add_mandatory_crisis(IT_project_complete_action)
        return

    Business.IT_increase_project_progress = IT_increase_project_progress

    def IT_unlock_project(self, project = None, add_to_log = True):
        if project:
            if project not in self.IT_projects:
                self.IT_projects.append(project)
                project.apply_policy()  # enable project at completion

                if add_to_log:
                    mc.log_event( project.name + " IT Project Complete!", "float_text_green")
        return

    Business.IT_unlock_project = IT_unlock_project

    def IT_project_is_active(self, project):
        return project in mc.business.active_IT_projects

    Business.IT_project_is_active = IT_project_is_active

    ##### Public sex related functions. Right now just placeholders, but we need these functions for later use when developing exhibitionism ####

    def topless_is_legal(self):
        return False

    def nudity_is_legal(self):
        return False

    def public_sex_is_legal(self):
        return False

    Business.topless_is_legal = topless_is_legal
    Business.nudity_is_legal = nudity_is_legal
    Business.public_sex_is_legal = public_sex_is_legal
