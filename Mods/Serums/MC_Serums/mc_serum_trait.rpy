#Use this class to define an MC serum trait type. MC Serum types will roughly mimic regular serum traits, but without as many variables, since we don't need to sell these.
#Each MC serum should be linked to an existing regular serum trait for research purposes.
#Each MC serum trait also has atleast three different levels of effectives, based on their mastery and the category master level.
#MC Serum Traits can be declared in init python statements because their data is all calculated on the fly, so the list can be changed and fucked with as needed without destroying save games.


init -2 python:
    class MC_Serum_Trait(renpy.store.object):
        def __init__(self, name, linked_trait, category, perk_list, perk_advance_reqs):
            self.name = name
            self.linked_trait = linked_trait
            self.category = category
            self.perk_list = perk_list
            self.perk_advance_reqs = perk_advance_reqs
            return

        def apply_trait(self):
            perk_system.add_ability_perk(self.perk_list[self.get_trait_tier() - 1](), self.name)
            if mc.business.prod_assistant == ashley and not ashley_mc_submission_story_complete():
                ashley.event_triggers_dict["mc_obedience"] += 1
            return

        def menu_name(self):
            return self.name.replace('Serum: ', '')

        def get_trait_tier(self):
            base_tier = 1
            return 3
            dict_key = "mc_serum_" + self.category + "_tier"    #Determine category tier
            base_tier += mc.business.event_triggers_dict.get(dict_key, 0)
            for req_func in self.perk_advance_reqs: #Now determine individual tier level
                if req_func():
                    base_tier += 1
            return base_tier

        def get_trait_desc(self):
            return self.perk_list[self.get_trait_tier()]().description

        def get_side_effect_chance(self):
            base_side_effect_chance = 0
            the_serum = find_in_list(lambda x: x.name == self.linked_trait, list_of_traits)
            base_side_effect_chance += max(the_serum.mastery_level - 20, 0)
            base_side_effect_chance += get_mc_serum_category_side_effect_chance(self.category)
            base_side_effect_chance += get_mc_serum_duration_side_effect_chance()
            return base_side_effect_chance

        def get_unlocked(self):
            dict_key = "mc_serum_" + self.category + "_unlocked"
            if mc.business.event_triggers_dict.get(dict_key, True):
                the_serum = find_in_list(lambda x: x.name == self.linked_trait, list_of_traits)
                return the_serum.researched
            return False

        def is_active(self, min_tier = 0, exact_tier = None):
            if min_tier > self.get_trait_tier():
                return False
            if exact_tier != None:
                if exact_tier != self.get_trait_tier():
                    return False
            return perk_system.has_ability_perk(self.name)

        def is_available(self):
            if self.get_unlocked(): #Determine if its unlocked first
                active_traits = 0
                for trait in list_of_mc_traits:
                    if trait.is_active():
                        active_traits += 1
                        if trait.category == self.category:   #Check and see if another trait in the same catagory is available.
                            return False
                if active_traits >= mc_serum_max_quantity():    #Check and see if we have hit the max possible active traits.
                    return False
                return True
            return False

    list_of_mc_traits = []

    def get_mc_serum_duration():
        return mc.business.event_triggers_dict.get("mc_serum_duration", 3)

    def get_mc_serum_category_side_effect_chance(category):
        pass
        return 0

    def get_mc_serum_duration_side_effect_chance():
        pass
        return 0

    def mc_energy_serum_unlocked():
        return mc.business.event_triggers_dict.get("mc_serum_energy_unlocked", False)

    def mc_aura_serum_unlocked():
        return mc.business.event_triggers_dict.get("mc_serum_aura_unlocked", False)

    def mc_cum_serum_unlocked():
        return mc.business.event_triggers_dict.get("mc_serum_cum_unlocked", False)

    def mc_physical_serum_unlocked():
        return mc.business.event_triggers_dict.get("mc_serum_physical_unlocked", False)

    def mc_serum_get_energy_list():
        return list(filter(lambda x: x.category == "energy", list_of_mc_traits))

    def mc_serum_get_aura_list():
        return list(filter(lambda x: x.category == "aura", list_of_mc_traits))

    def mc_serum_get_cum_list():
        return list(filter(lambda x: x.category == "cum", list_of_mc_traits))

    def mc_serum_get_physical_list():
        return list(filter(lambda x: x.category == "physical", list_of_mc_traits))

    def mc_serum_max_quantity():
        return mc.business.event_triggers_dict.get("mc_serum_max_quant", 1)
