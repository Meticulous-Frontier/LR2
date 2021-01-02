init -1 python:
    def get_hr_director(self):
        if not hasattr(self, "_hr_director"):
            self._hr_director = None
        return next((x for x in all_people_in_the_game() if x.identifier == self._hr_director), None)

    def set_hr_director(self, item):
        if isinstance(item, Person):
            self._hr_director = item.identifier
        else:
            self._hr_director = None

    def del_hr_director(self):
        del self._hr_director

    # add follow_mc attribute to person class (without sub-classing)
    Business.hr_director = property(get_hr_director, set_hr_director, del_hr_director, "The company HR director position.")

    def get_funds_yesterday(self):
        if not hasattr(self, "_funds_yesterday"):
            self._funds_yesterday = 1000 # default start money
        return self._funds_yesterday

    def set_funds_yesterday(self, value):
        self._funds_yesterday = value

    def del_funds_yesterday(self):
        del self._funds_yesterday

    Business.funds_yesterday = property(get_funds_yesterday, set_funds_yesterday, del_funds_yesterday, "Holds business funds from day before")

    def get_unisex_restroom_unlocks(self):
        if not hasattr(self, "_unisex_restroom_unlocks"):
            self._unisex_restroom_unlocks = {}
        return self._unisex_restroom_unlocks

    def set_unisex_restroom_unlocks(self, value):
        self._unisex_restroom_unlocks = value

    def del_unisex_restroom_unlocks(self):
        del self._unisex_restroom_unlocks

    Business.unisex_restroom_unlocks = property(get_unisex_restroom_unlocks, set_unisex_restroom_unlocks, del_unisex_restroom_unlocks, "Tracking dictionary for the unisex restroom event.")

    def update_employee_status(self, person):
        if person.event_triggers_dict.get("employed_since", -1) == -1:
            person.event_triggers_dict["employed_since"] = day
            self.listener_system.fire_event("new_hire", the_person = person)

        for other_employee in self.get_employee_list():
            town_relationships.begin_relationship(person, other_employee) #They are introduced to everyone at work, with a starting value of "Acquaintance"

    Business.update_employee_status = update_employee_status

    def hire_person(self, person, target_division, add_to_location = False):
        div_func = {
            "Research" : [ self.research_team, self.r_div],
            "Production" : [ self.production_team, self.p_div],
            "Supply" : [ self.supply_team, self.s_div ],
            "Marketing" : [ self.market_team, self.m_div ],
            "HR" : [ self.hr_team, self.h_div ]
        }
        if not person in div_func[target_division][0]:
            div_func[target_division][0].append(person)
        person.add_role(employee_role)
        person.job = self.get_employee_title(person)
        person.set_work(div_func[target_division][1])
        if add_to_location:
            div_func[target_division][1].add_person(person)
        self.update_employee_status(person)

    Business.hire_person = hire_person

    def calculate_strip_club_income(self):
        income = 0
        if "get_strip_club_foreclosed_stage" in globals():
            if get_strip_club_foreclosed_stage() >= 5: # The player owns the club
                multiplier = 1
                if __builtin__.len(people_in_role(manager_role)) > 0 or __builtin__.len(people_in_role(mistress_role)) > 0:
                    multiplier = 1.1 # +10% income

                for person in known_people_in_the_game():
                    if person.has_role([stripper_role, waitress_role, bdsm_performer_role]):
                        income += (calculate_stripper_profit(person) * multiplier)  # profit

                    if person.has_role([stripper_role, waitress_role, bdsm_performer_role, manager_role, mistress_role]):
                        income -= person.stripper_salary    # costs

        return income

    Business.calculate_strip_club_income = calculate_strip_club_income

    # extend the default run day function
    def business_run_day_extended(org_func):
        def run_day_wrapper(business):
            # run original function
            org_func(business)
            # run extension code
            strip_club_income = business.calculate_strip_club_income()
            if strip_club_income != 0:
                mc.business.funds += strip_club_income
                mc.business.add_normal_message("The [strip_club.formalName] has made a net profit of $" + str(__builtin__.round(strip_club_income, 1)) + " today!")

        return run_day_wrapper

    # wrap up the run_day function
    Business.run_day = business_run_day_extended(Business.run_day)

    # add fire HR director function to Business
    def fire_HR_director(self):
        if self.hr_director:
            self.hr_director.remove_role(HR_director_role)
            self.hr_director = None
            cleanup_HR_director_meetings()

    Business.fire_HR_director = fire_HR_director


    # wrap default remove_employee function to also trigger the fire_HR_director code when needed
    def business_remove_employee_extended(org_func):
        def remove_employee_wrapper(business, person, remove_linked = True):
            org_func(business, person, remove_linked)

            if person is business.hr_director:
                business.fire_HR_director()

        return remove_employee_wrapper

    Business.remove_employee = business_remove_employee_extended(Business.remove_employee)

    def business_add_mandatory_crisis(self, crisis_event):
        if not crisis_event in self.mandatory_crises_list:
            self.mandatory_crises_list.append(crisis_event)

    Business.add_mandatory_crisis = business_add_mandatory_crisis

    def business_add_mandatory_morning_crisis(self, crisis_event):
        if not crisis_event in self.mandatory_morning_crises_list:
            self.mandatory_morning_crises_list.append(crisis_event)

    Business.add_mandatory_morning_crisis = business_add_mandatory_morning_crisis
