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


        
        