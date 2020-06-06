init -1 python:
    def get_hr_director(self):
        if not hasattr(self, "_hr_director"):
            self._hr_director = False
        return self._hr_director

    def set_hr_director(self, value):
        self._hr_director = value

    def del_hr_director(self):
        del self._hr_director

    # add follow_mc attribute to person class (without sub-classing)
    Business.hr_director = property(get_hr_director, set_hr_director, del_hr_director, "The company HR director position.")

    def get_unisex_restroom_unlocks(self):
        if not hasattr(self, "_unisex_restroom_unlocks"):
            self._unisex_restroom_unlocks = {}
        return self._unisex_restroom_unlocks

    def set_unisex_restroom_unlocks(self, value):
        self._unisex_restroom_unlocks = value

    def del_unisex_restroom_unlocks(self):
        del self._unisex_restroom_unlocks

    Business.unisex_restroom_unlocks = property(get_unisex_restroom_unlocks, set_unisex_restroom_unlocks, del_unisex_restroom_unlocks, "Tracking dictionary for the unisex restroom event.")

    def update_employee_status(self, new_person):
        if new_person.event_triggers_dict.get("employed_since", -1) == -1:
            new_person.event_triggers_dict["employed_since"] = day
            self.listener_system.fire_event("new_hire", the_person = new_person)

        for other_employee in self.get_employee_list():
            town_relationships.begin_relationship(new_person, other_employee) #They are introduced to everyone at work, with a starting value of "Acquaintance"

    Business.update_employee_status = update_employee_status

    def hire_person(self, new_person, target_division, add_to_location = False):
        div_func = {
            "Research" : [ self.research_team, self.r_div],
            "Production" : [ self.production_team, self.p_div],
            "Supply" : [ self.supply_team, self.s_div ],
            "Marketing" : [ self.market_team, self.m_div ],
            "HR" : [ self.hr_team, self.h_div ]
        }
        div_func[target_division][0].append(new_person)
        new_person.special_role.append(employee_role)
        new_person.job = self.get_employee_title(new_person)
        new_person.set_work([1,2,3], div_func[target_division][1])
        self.update_employee_status(new_person)
        if add_to_location:
            div_func[target_division][1].add_person(new_person)

    Business.hire_person = hire_person

    def add_unique_mandatory_crisis(self, the_crisis):
        if the_crisis not in self.mandatory_crises_list:
            self.mandatory_crises_list.append(the_crisis)

    Business.add_unique_mandatory_crisis = add_unique_mandatory_crisis
