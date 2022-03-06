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

    def get_it_director(self):
        if not hasattr(self, "_it_director"):
            self._it_director = None
        return next((x for x in all_people_in_the_game() if x.identifier == self._it_director), None)

    def set_it_director(self, item):
        if isinstance(item, Person):
            self._it_director = item.identifier
        else:
            self._it_director = None

    def del_it_director(self):
        del self._it_director

    # add follow_mc attribute to person class (without sub-classing)
    Business.it_director = property(get_it_director, set_it_director, del_it_director, "The company IT director position.")

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

    def get_uniform_limits_enhanced(self): #Returns three values: the max sluttiness of a full outfit, max sluttiness of an underwear set, and if only overwear sets are allowed or notself.
        slut_limit = 0
        underwear_limit = 0
        limited_to_top = True
        if maximal_arousal_uniform_policy.is_active():
            slut_limit = 999 #ie. no limit at all.
            underwear_limit = 999
            limited_to_top = False
        elif corporate_enforced_nudity_policy.is_active():
            slut_limit = 80
            underwear_limit = 999
            limited_to_top = False
        elif minimal_coverage_uniform_policy.is_active():
            slut_limit = 60
            underwear_limit = 30
            limited_to_top = False
        elif reduced_coverage_uniform_policy.is_active():
            slut_limit = 40
            underwear_limit = 15
            limited_to_top = False
        elif casual_uniform_policy.is_active():
            slut_limit = 30
            underwear_limit = 0
            limited_to_top = True
        elif relaxed_uniform_policy.is_active():
            slut_limit = 20
            underwear_limit = 0
            limited_to_top = True
        elif strict_uniform_policy.is_active():
            slut_limit = 10
            underwear_limit = 0
            limited_to_top = True
        else:
            slut_limit = 0
            underwear_limit = 0
            limited_to_top = True
        return slut_limit, underwear_limit, limited_to_top

    Business.get_uniform_limits = get_uniform_limits_enhanced

    def add_uniform_to_company(self, outfit, full_outfit_flag = False, overwear_flag = False, underwear_flag = False, research = True, production = True, supply = True, marketing = True, hr = True):
        uniform = UniformOutfit(outfit)
        if uniform.can_toggle_full_outfit_state():
            uniform.set_full_outfit_flag(full_outfit_flag)
        if uniform.can_toggle_overwear_state():
            uniform.set_overwear_flag(overwear_flag)
        if uniform.can_toggle_underwear_state():
            uniform.set_underwear_flag(underwear_flag)

        uniform.set_research_flag(research)
        uniform.set_production_flag(production)
        uniform.set_supply_flag(supply)
        uniform.set_marketing_flag(marketing)
        uniform.set_hr_flag(hr)

        mc.business.business_uniforms.append(uniform)
        mc.business.update_uniform_wardrobes()
        return

    Business.add_uniform_to_company = add_uniform_to_company

    def production_progress_enhanced(self,focus,int,skill,multiplier = 1.0):
        #First, figure out how many production points we can produce total. Subtract that much supply and mark that much production down for the end of day report.
        production_amount = __builtin__.int(((3*focus) + int + (2*skill) + 10) * (self.team_effectiveness / 100.0) * multiplier)
        self.production_potential += production_amount

        if production_amount > self.supply_count:
            production_amount = self.supply_count #Figure out our total available production, before we split it up between tasks (which might not have 100% usage!)

        for line in self.production_lines:
            supply_used = line.add_production(production_amount) #NOTE: this is modified by the weighted use of the Line in particular. This allows for greater than 100% efficency.
            self.supply_count += - supply_used
            self.production_used += supply_used

        return production_amount

    Business.production_progress = production_progress_enhanced

    def get_business_stripper_wardrobe(self):
        if not hasattr(self, "_stripper_wardrobe"):
            self._stripper_wardrobe = stripclub_wardrobe
        return self._stripper_wardrobe

    Business.stripper_wardrobe = property(get_business_stripper_wardrobe, None, None, "Instance of stripper wardrobe")

    def get_business_waitress_wardrobe(self):
        if not hasattr(self, "_waitress_wardrobe"):
            self._waitress_wardrobe = waitress_wardrobe
        return self._waitress_wardrobe

    Business.waitress_wardrobe = property(get_business_waitress_wardrobe, None, None, "Instance of waitress wardrobe")

    def get_business_bdsm_wardrobe(self):
        if not hasattr(self, "_bdsm_wardrobe"):
            self._bdsm_wardrobe = BDSM_performer_wardrobe
        return self._bdsm_wardrobe

    Business.bdsm_wardrobe = property(get_business_bdsm_wardrobe, None, None, "Instance of bdsm wardrobe")

    def get_business_manager_wardrobe(self):
        if not hasattr(self, "_manager_wardrobe"):
            self._manager_wardrobe = manager_wardrobe
        return self._manager_wardrobe

    Business.manager_wardrobe = property(get_business_manager_wardrobe, None, None, "Instance of manager wardrobe")

    def get_business_mistress_wardrobe(self):
        if not hasattr(self, "_mistress_wardrobe"):
            self._mistress_wardrobe = mistress_wardrobe
        return self._mistress_wardrobe

    Business.mistress_wardrobe = property(get_business_mistress_wardrobe, None, None, "Instance of mistress wardrobe")

    def get_business_stripclub_uniforms(self):
        def parse_wardrobe_to_uniform(wardrobe, flag_func):
            for outfit in wardrobe.outfits:
                uniform = StripClubOutfit(outfit)
                uniform.set_full_outfit_flag(True)
                getattr(uniform, flag_func)(True)
                mc.business._stripclub_uniforms.append(uniform)

            for outfit in wardrobe.overwear_sets:
                uniform = StripClubOutfit(outfit)
                uniform.set_overwear_flag(True)
                getattr(uniform, flag_func)(True)
                mc.business._stripclub_uniforms.append(uniform)

            for outfit in wardrobe.underwear_sets:
                uniform.set_underwear_flag(True)
                getattr(uniform, flag_func)(True)
                mc.business._stripclub_uniforms.append(uniform)
            return

        if not hasattr(self, "_stripclub_uniforms"):
            self._stripclub_uniforms = []

            parse_wardrobe_to_uniform(stripclub_wardrobe, "set_stripper_flag")
            parse_wardrobe_to_uniform(waitress_wardrobe, "set_waitress_flag")
            parse_wardrobe_to_uniform(BDSM_performer_wardrobe, "set_bdsm_flag")
            parse_wardrobe_to_uniform(manager_wardrobe, "set_manager_flag")
            parse_wardrobe_to_uniform(mistress_wardrobe, "set_mistress_flag")

        return self._stripclub_uniforms

    Business.stripclub_uniforms = property(get_business_stripclub_uniforms, None, None, "Instance of total stripclub uniforms.")

    def update_stripclub_wardrobes(self):
        def update_stripclub_uniform(wardrobe, uniform):
            if uniform.full_outfit_flag:
                wardrobe.add_outfit(uniform.outfit)
            if uniform.overwear_flag:
                wardrobe.add_overwear_set(uniform.outfit)
            if uniform.underwear_flag:
                wardrobe.add_underwear_set(uniform.outfit)
            return

        self.stripper_wardrobe.clear_wardrobe()
        self.waitress_wardrobe.clear_wardrobe()
        self.bdsm_wardrobe.clear_wardrobe()
        self.manager_wardrobe.clear_wardrobe()
        self.mistress_wardrobe.clear_wardrobe()

        for uniform in self.stripclub_uniforms:
            if uniform.stripper_flag:
                update_stripclub_uniform(self.stripper_wardrobe, uniform)
            if uniform.waitress_flag:
                update_stripclub_uniform(self.waitress_wardrobe, uniform)
            if uniform.bdsm_flag:
                update_stripclub_uniform(self.bdsm_wardrobe, uniform)
            if uniform.manager_flag:
                update_stripclub_uniform(self.manager_wardrobe, uniform)
            if uniform.mistress_flag:
                update_stripclub_uniform(self.mistress_wardrobe, uniform)
        return

    Business.update_stripclub_wardrobes = update_stripclub_wardrobes

    def calculate_strip_club_income(self):
        income = 0
        if "get_strip_club_foreclosed_stage" in globals():
            if get_strip_club_foreclosed_stage() >= 5: # The player owns the club
                multiplier = 1
                if __builtin__.len(people_in_role(stripclub_manager_role)) > 0 or __builtin__.len(people_in_role(stripclub_mistress_role)) > 0:
                    multiplier = 1.1 # +10% income

                for person in known_people_in_the_game():
                    if person.has_role([stripper_role, stripclub_waitress_role, stripclub_bdsm_performer_role]):
                        income += (calculate_stripper_profit(person) * multiplier)  # profit

                    if person.has_role([stripper_role, stripclub_waitress_role, stripclub_bdsm_performer_role, stripclub_manager_role, stripclub_mistress_role]):
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
                mc.business.change_funds(strip_club_income, add_to_log = False)
                mc.business.add_normal_message("The [strip_club.formal_name] has made a net profit of $" + str(__builtin__.round(strip_club_income, 1)) + " today!")

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

    def fire_IT_director(self):
        if self.it_director:
            self.it_director.remove_role(IT_director_role)
            self.it_director = None
            #cleanup_HR_director_meetings()

    Business.fire_IT_director = fire_IT_director


    # wrap default remove_employee function to also trigger the fire_HR_director code when needed
    def business_remove_employee_extended(org_func):
        def remove_employee_wrapper(business, person):
            org_func(business, person)

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

    def business_remove_mandatory_crisis(self, crisis_event):
        if isinstance(crisis_event, basestring):
            found = find_in_list(lambda x: x.effect == crisis_event, self.mandatory_crises_list)
            if found:
                self.mandatory_crises_list.remove(found)
                return True
            found = find_in_list(lambda x: x.effect == crisis_event, self.mandatory_morning_crises_list)
            if found:
                self.mandatory_morning_crises_list.remove(found)
                return True
        elif isinstance(crisis_event, Action):
            found = find_in_list(lambda x: x == crisis_event, self.mandatory_crises_list)
            if found:
                self.mandatory_crises_list.remove(found)
                return True
            found = find_in_list(lambda x: x == crisis_event, self.mandatory_morning_crises_list)
            if found:
                self.mandatory_morning_crises_list.remove(found)
                return True
        return False

    Business.remove_mandatory_crisis = business_remove_mandatory_crisis

    def business_get_employee_list(self):
        return [x for x in self.research_team + self.production_team + self.supply_team + self.market_team + self.hr_team if x.is_available]

    Business.get_employee_list = business_get_employee_list

    def business_mc_offspring_count(self):
        return sum(x.number_of_children_with_mc() for x in self.get_employee_list())

    Business.mc_offspring_count = business_mc_offspring_count

    def business_employees_with_children_with_mc(self):
        return [x for x in self.get_employee_list() if x.has_child_with_mc()]

    Business.employees_with_children_with_mc = business_employees_with_children_with_mc

    # Date schedule related functions

    def date_scheduled_today(self):
        return (self.event_triggers_dict.get("movie_date_scheduled", False) and day%7 == 1) \
            or (self.event_triggers_dict.get("fuck_date_scheduled", False) and day%7 == 3) \
            or (self.event_triggers_dict.get("dinner_date_scheduled", False) and day%7 == 4)

    Business.date_scheduled_today = date_scheduled_today

    # College intern related functions
    def business_college_interns_research(self):
        if not hasattr(self, "_college_interns_research"):
            self._college_interns_research = MappedList(Person, all_people_in_the_game)
        return self._college_interns_research

    Business.college_interns_research = property(business_college_interns_research, None, None)

    def business_college_interns_production(self):
        if not hasattr(self, "_college_interns_production"):
            self._college_interns_production = MappedList(Person, all_people_in_the_game)
        return self._college_interns_production

    Business.college_interns_production = property(business_college_interns_production, None, None)

    def business_college_interns_market(self):
        if not hasattr(self, "_college_interns_market"):
            self._college_interns_market = MappedList(Person, all_people_in_the_game)
        return self._college_interns_market

    Business.college_interns_market = property(business_college_interns_market, None, None)

    def business_college_interns_supply(self):
        if not hasattr(self, "_college_interns_supply"):
            self._college_interns_supply = MappedList(Person, all_people_in_the_game)
        return self._college_interns_supply

    Business.college_interns_supply = property(business_college_interns_supply, None, None)

    def business_college_interns_HR(self):
        if not hasattr(self, "_college_interns_HR"):
            self._college_interns_HR = MappedList(Person, all_people_in_the_game)
        return self._college_interns_HR

    Business.college_interns_HR = property(business_college_interns_HR, None, None)

    Business.college_interns_unlocked = False
    Business.college_supply_interns_unlocked = False
    Business.college_market_interns_unlocked = False
    Business.college_hr_interns_unlocked = False
    Business.max_interns_by_division = 3    #Can be changed in later game code.
    Business.cost_to_hire_intern = 5000

    def hire_college_intern(self, person, target_division, add_to_location = False):
        div_func = {
            "Research" : [ self.college_interns_research, self.r_div],
            "Production" : [ self.college_interns_production, self.p_div],
            "Supply" : [ self.college_interns_supply, self.s_div ],
            "Marketing" : [ self.college_interns_market, self.m_div ],
            "HR" : [ self.college_interns_HR, self.h_div ]
        }
        if not person in div_func[target_division][0]:
            div_func[target_division][0].append(person)
        person.add_role(college_intern_role)
        person.add_job(student_job)
        person.set_override_schedule(div_func[target_division][1], the_days = [5,6], the_times = [1,2])
        if add_to_location:
            university.add_person(person)
        if person.event_triggers_dict.get("intern_since", -1) == -1:
            person.event_triggers_dict["intern_since"] = day
            self.listener_system.fire_event("new_intern", the_person = person)

        # they never meet other employees...so why add relationships?
        # for other_employee in (self.college_interns_research + self.college_interns_production + self.college_interns_HR + self.college_interns_supply + self.college_interns_market):
        #     town_relationships.begin_relationship(person, other_employee) #They are introduced to everyone at work, with a starting value of "Acquaintance"
        return

    Business.hire_college_intern = hire_college_intern

    def remove_college_intern(self, person):
        if person in self.college_interns_research:
            self.college_interns_research.remove(person)
        elif person in self.college_interns_production:
            self.college_interns_production.remove(person)
        elif person in self.college_interns_supply:
            self.college_interns_supply.remove(person)
        elif person in self.college_interns_market:
            self.college_interns_market.remove(person)
        elif person in self.college_interns_HR:
            self.college_interns_HR.remove(person)
        else:
            pass    #Some kind of error here?

        person.set_override_schedule(None, the_days = [5,6], the_times = [1,2])
        person.remove_role(college_intern_role)
        return

    Business.remove_college_intern = remove_college_intern

    def get_intern_depts_with_openings(self):
        dept_list = []
        if len(self.college_interns_research) < self.max_interns_by_division:
            dept_list.append("Research")
        if len(self.college_interns_production) < self.max_interns_by_division:
            dept_list.append("Production")
        if len(self.college_interns_market) < self.max_interns_by_division and self.college_market_interns_unlocked:
            dept_list.append("Marketing")
        if len(self.college_interns_supply) < self.max_interns_by_division and self.college_supply_interns_unlocked:
            dept_list.append("Supply")
        if len(self.college_interns_HR) < self.max_interns_by_division and self.college_hr_interns_unlocked:
            dept_list.append("HR")
        return dept_list

    Business.get_intern_depts_with_openings = get_intern_depts_with_openings

    def business_get_intern_list(self):
        return [x for x in self.college_interns_research + self.college_interns_production + self.college_interns_supply + self.college_interns_market + self.college_interns_HR if x.is_available]

    Business.get_intern_list = business_get_intern_list

    def any_intern_in_office(self):
        for x in self.get_intern_list():
            if college_intern_is_at_work(x):
                return True
        return False

    Business.any_intern_in_office = any_intern_in_office
