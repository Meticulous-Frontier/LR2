init 5 python:
    def has_nora_trait_info(person):
        if person.has_role(mother_role) and person.sluttiness > 75 and person.love > 75 and nora_reward_mother_trait not in list_of_traits:
            return True
        elif person.has_role(sister_role) and person.sluttiness > 75 and person.obedience > 150 and nora_reward_sister_trait not in list_of_traits:
            return True
        elif person.has_role(cousin_role) and person.sluttiness > 75 and person.love < -25 and nora_reward_cousin_trait not in list_of_traits:
            return True
        elif person.has_role(aunt_role) and person.sluttiness > 75 and nora_reward_aunt_trait not in list_of_traits:
            return True
        elif person.has_role(nora_role) and person.sluttiness > 75 and nora_reward_nora_trait not in list_of_traits:
            return True
        elif person.has_role(pregnant_role) and person.event_triggers_dict.get("preg_transform_day",day) < day and person.sluttiness > 75 and nora_reward_hucow_trait not in list_of_traits:
            return True
        elif person.love > 85 and nora_reward_high_love_trait not in list_of_traits:
            return True
        elif person.love < -50 and nora_reward_low_love_trait not in list_of_traits:
            return True
        elif person.obedience > 180 and nora_reward_high_obedience_trait not in list_of_traits:
            return True
        elif person.sluttiness > 100 and nora_reward_high_slut_trait not in list_of_traits:
            return True
        elif person.int >= 7 and person.charisma >= 7 and person.focus >= 7 and nora_reward_genius_trait not in list_of_traits:
            return True
        elif person.has_exact_role(very_heavy_trance_role) and nora_reward_instant_trance not in list_of_traits:
            return True
        return False


    def study_person_requirement(the_person):
        if len(list_of_nora_traits) == 0:
            return False
        if not has_nora_trait_info(the_person):
            return "No interesting properties"
        if time_of_day == 4:
            return "Not enough time"
        return True
