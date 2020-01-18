


init 1 python:
    def Perk_mod_initialization():

        global perk_system
        perk_system = Perks()
        return


init -1 python:
    class Perks(renpy.store.object):
        def __init__(self):
            self.stat_perks = {}
            self.item_perks = {}
            self.ability_perks = {}

        def update(self):  #By adding an update, we can add temporary perks that may expire.
            for x in self.stat_perks.copy():
                if self.stat_perks[x].update():
                    self.stat_perks.pop(x)
            for x in self.item_perks.copy():  #Note, we probably don't need this, since items are generally unlocks
                if self.item_perks[x].update():
                    self.item_perks.pop(x)
            for x in self.ability_perks:
                x.update()
            return

        def add_stat_perk(self, this_perk, perk_name):
            if perk_name in self.stat_perks:  #We already have this perk, don't add it again.
                return
            else:
                self.stat_perks[perk_name] = this_perk
                self.stat_perks[perk_name].apply()
            return

        def has_stat_perk(self, perk_name):
            if perk_name in self.stat_perks:
                return True
            return False

        def get_stat_perk(self, perk_name):
            if perk_name in self.stat_perks:
                return self.stat_perks[perk_name]
            return None

        def add_item_perk(self, this_perk, perk_name):
            if perk_name in self.item_perks:
                return
            else:
                self.item_perks[perk_name] = this_perk

        def has_item_perk(self, perk_name):
            if perk_name in self.item_perks:
                return True
            return False

        def get_item_perk(self, perk_name):
            if perk_name in self.item_perks:
                return self.item_perks[perk_name]
            return None

    class Stat_Perk(renpy.store.object):
        def __init__(self, description, cha_bonus = 0, int_bonus = 0, foc_bonus = 0,
            hr_bonus = 0, market_bonus = 0, research_bonus = 0, production_bonus = 0, supply_bonus = 0,
            foreplay_bonus = 0, oral_bonus = 0, vaginal_bonus = 0, anal_bonus = 0, energy_bonus = 0,
            stat_cap = 0, skill_cap = 0, sex_cap = 0, energy_cap = 0,
            bonus_is_temp = False, duration = 0):

            if description == None:
                self.description = " "
            else:
                self.description = description

            self.cha_bonus = cha_bonus
            self.int_bonus = int_bonus
            self.foc_bonus = foc_bonus
            self.hr_bonus = hr_bonus
            self.market_bonus = market_bonus
            self.research_bonus = research_bonus
            self.production_bonus = production_bonus
            self.supply_bonus = supply_bonus
            self.foreplay_bonus = foreplay_bonus
            self.oral_bonus = oral_bonus
            self.vaginal_bonus = vaginal_bonus
            self.anal_bonus = anal_bonus
            self.energy_bonus = energy_bonus
            self.stat_cap = stat_cap
            self.skill_cap = skill_cap
            self.sex_cap = sex_cap
            self.energy_cap = energy_cap
            self.bonus_is_temp = bonus_is_temp
            self.duration = duration
            self.start_day = day

        def apply(self):
            mc.charisma += self.cha_bonus
            mc.int += self.int_bonus
            mc.focus += self.foc_bonus
            mc.hr_skill += self.hr_bonus
            mc.market_skill += self.market_bonus
            mc.research_skill += self.research_bonus
            mc.production_skill += self.production_bonus
            mc.supply_skill += self.supply_bonus
            mc.sex_skills["Foreplay"] += self.foreplay_bonus
            mc.sex_skills["Oral"] += self.oral_bonus
            mc.sex_skills["Vaginal"] += self.vaginal_bonus
            mc.sex_skills["Anal"] += self.anal_bonus
            mc.max_energy += self.energy_bonus
            mc.max_stats += self.stat_cap
            mc.max_work_skills += self.skill_cap
            mc.max_sex_skills += self.sex_cap
            mc.max_energy_cap += self.energy_cap
            return

        def remove(self):
            mc.charisma -= self.cha_bonus
            mc.int -= self.int_bonus
            mc.focus -= self.foc_bonus
            mc.hr_skill -= self.hr_bonus
            mc.market_skill -= self.market_bonus
            mc.research_skill -= self.research_bonus
            mc.production_skill -= self.production_bonus
            mc.supply_skill -= self.supply_bonus
            mc.sex_skills["Foreplay"] -= self.foreplay_bonus
            mc.sex_skills["Oral"] -= self.oral_bonus
            mc.sex_skills["Vaginal"] -= self.vaginal_bonus
            mc.sex_skills["Anal"] -= self.anal_bonus
            mc.max_energy -= self.energy_bonus
            mc.max_stats -= self.stat_cap
            mc.max_work_skills -= self.skill_cap
            mc.max_sex_skills -= self.sex_cap
            mc.max_energy_cap -= self.energy_cap
            return

        def update(self):
            if self.bonus_is_temp:
                if day > self.duration + self.start_day:
                    self.remove()
                    return True
            return False

    class Item_Perk(renpy.store.object):
        def __init__(self,  description, usable = False, bonus_is_temp = False, duration = 0):
            self.description = description
            self.usable = usable
            self.bonus_is_temp = bonus_is_temp
            self.duration = duration
            self.start_day = day


        def update(self):
            if self.bonus_is_temp:
                if day > self.duration + self.start_day:
                    self.remove()
                    return True
            return False
