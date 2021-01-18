init 1 python:
    #Requirement functions
    def exhibition_fetish_employee_intro_requirement():
        if time_of_day == 3:
            if mc.business.is_open_for_business():
                if mc.is_at_work():
                    return True
        return False


    def exhibition_fetish_family_intro_requirement():
        if the_person.location == the_person.home:
            if the_person.location.get_person_count() == 1: #She is alone in her bedroom
                return True
        return False

    def exhibition_fetish_generic_intro_requirement(the_person):
        if the_person.location != the_person.home:
            return True
        return False

    def exhibition_fetish_mom_intro_requirement():
        return False

    def exhibition_fetish_lily_intro_requirement():
        return False

    def exhibition_fetish_rebecca_intro_requirement():
        return False

    def exhibition_fetish_gabrielle_intro_requirement():
        return False

    def exhibition_fetish_stephanie_intro_requirement():
        return False

    def exhibition_fetish_alex_intro_requirement():
        return False

    def exhibition_fetish_nora_intro_requirement():
        return False

    def exhibition_fetish_emily_intro_requirement():
        return False

    def exhibition_fetish_christina_intro_requirement():
        return False

    def exhibition_fetish_starbuck_intro_requirement():
        return False

    def exhibition_fetish_sarah_intro_requirement():
        return False

    def exhibition_fetish_ophelia_intro_requirement():
        return False

    def exhibition_fetish_candace_intro_requirement():
        return False

    def exhibition_fetish_dawn_intro_requirement():
        return False

    def exhibition_fetish_erica_intro_requirement():
        return False

    def exhibition_fetish_ashley_intro_requirement():
        return False

init 2 python: #Other exhibition fetish related python code

    pass

init 50 python:
    def get_exhbition_fetish_unique_dialogue_list():
        anal_list = [lily, starbuck]

        return anal_list

    def debug_set_stats_for_exhbition_fetish_mins(the_person):
        the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.max_opinion_score("anal sex")
        the_person.core_sluttiness = 70
        the_person.sluttiness = 70
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0
        return

    def abort_exhbition_fetish_intro(the_person): #Use this function to exit a anal fetish scene for whatever reason (something fails, MC choice, etc.)
        the_person.event_triggers_dict["exhbition_fetish_start"] = False
        the_person.remove_role(exhbition_fetish_role)
### Function labels

# Fetish Labels
label exhibition_fetish_employee_intro_label(the_person):
    return False

label exhibition_fetish_family_intro_label(the_person):
    return False

label exhibition_fetish_generic_intro_label(the_person):
    return False

label exhibition_fetish_mom_intro_label():
    return False

label exhibition_fetish_lily_intro_label():
    return False

label exhibition_fetish_rebecca_intro_label():
    return False

label exhibition_fetish_gabrielle_intro_label():
    return False

label exhibition_fetish_stephanie_intro_label():
    return False

label exhibition_fetish_alex_intro_label():
    return False

label exhibition_fetish_nora_intro_label():
    return False

label exhibition_fetish_emily_intro_label():
    return False

label exhibition_fetish_christina_intro_label():
    return False

label exhibition_fetish_starbuck_intro_label():
    return False

label exhibition_fetish_sarah_intro_label():
    return False

label exhibition_fetish_ophelia_intro_label():
    return False

label exhibition_fetish_candace_intro_label():
    return False

label exhibition_fetish_dawn_intro_label():
    return False

label exhibition_fetish_erica_intro_label():
    return False

label exhibition_fetish_ashley_intro_label():
    return False

label unit_test_exhbition_fetish_intro():

    "Generic intros"
    $ debug_set_stats_for_exhbition_fetish_mins(mom)
    "Method: exhbition_fetish_family_intro_label"
    call exhbition_fetish_family_intro_label(mom) from _unit_test_exhbition_fetish_intro_01
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(starbuck)
    "Method: exhbition_fetish_generic_intro_label"
    call exhbition_fetish_generic_intro_label(starbuck) from _unit_test_exhbition_fetish_intro_02
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(stephanie)
    "Method: exhbition_fetish_employee_intro_label"
    call  exhbition_fetish_employee_intro_label(stephanie) from _unit_test_exhbition_fetish_intro_03
    $ mc.energy = mc.max_energy

    $ stephanie.remove_role(exhbition_fetish_role)
    $ mom.remove_role(exhbition_fetish_role)
    $ starbuck.remove_role(exhbition_fetish_role)

    "Unique intros"
    $ debug_set_stats_for_exhbition_fetish_mins(mom)
    "Method: exhbition_fetish_mom_intro_label"
    call exhbition_fetish_mom_intro_label() from _unit_test_exhbition_fetish_intro_04
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(lily)
    "Method: exhbition_fetish_lily_intro_label"
    call exhbition_fetish_lily_intro_label() from _unit_test_exhbition_fetish_intro_05
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(aunt)
    "Method: exhbition_fetish_rebecca_intro_label"
    call exhbition_fetish_rebecca_intro_label() from _unit_test_exhbition_fetish_intro_06
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(cousin)
    "Method: exhbition_fetish_gabrielle_intro_label"
    call exhbition_fetish_gabrielle_intro_label() from _unit_test_exhbition_fetish_intro_07
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(stephanie)
    "Method: exhbition_fetish_stephanie_intro_label"
    call exhbition_fetish_stephanie_intro_label() from _unit_test_exhbition_fetish_intro_08
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(alexia)
    "Method: exhbition_fetish_alex_intro_label"
    call exhbition_fetish_alex_intro_label() from _unit_test_exhbition_fetish_intro_09
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(nora)
    "Method: exhbition_fetish_nora_intro_label"
    call exhbition_fetish_nora_intro_label() from _unit_test_exhbition_fetish_intro_10
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(emily)
    "Method: exhbition_fetish_emily_intro_label"
    call exhbition_fetish_emily_intro_label() from _unit_test_exhbition_fetish_intro_11
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(christina)
    "Method: exhbition_fetish_christina_intro_label"
    call exhbition_fetish_christina_intro_label() from _unit_test_exhbition_fetish_intro_12
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(starbuck)
    "Method: exhbition_fetish_starbuck_intro_label"
    call exhbition_fetish_starbuck_intro_label() from _unit_test_exhbition_fetish_intro_13
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(sarah)
    "Method: exhbition_fetish_sarah_intro_label"
    call exhbition_fetish_sarah_intro_label() from _unit_test_exhbition_fetish_intro_14
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(salon_manager)
    "Method: exhbition_fetish_ophelia_intro_label"
    call exhbition_fetish_ophelia_intro_label() from _unit_test_exhbition_fetish_intro_15
    $ mc.energy = mc.max_energy

    $ create_debug_candace()
    $ debug_set_stats_for_exhbition_fetish_mins(candace)
    "Method: exhbition_fetish_candace_intro_label"
    call exhbition_fetish_candace_intro_label() from _unit_test_exhbition_fetish_intro_16
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(dawn)
    "Method: exhbition_fetish_dawn_intro_label"
    call exhbition_fetish_dawn_intro_label() from _unit_test_exhbition_fetish_intro_17
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(erica)
    "Method: exhbition_fetish_erica_intro_label"
    call exhbition_fetish_erica_intro_label() from _unit_test_exhbition_fetish_intro_18
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhbition_fetish_mins(ashley)
    "Method: exhbition_fetish_ashley_intro_label"
    call exhbition_fetish_ashley_intro_label() from _unit_test_exhbition_fetish_intro_19
    $ mc.energy = mc.max_energy

    return
