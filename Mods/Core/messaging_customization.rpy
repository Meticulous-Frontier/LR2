####################################################
# Allows for suppressing of log message categories #
####################################################

init -2:
    # categories
    default persistent.serum_messages = True
    default persistent.stat_change_messages = True
    default persistent.skill_change_messages = True
    default persistent.clarity_messages = True

init 2 python:
    import inspect

    # generic extension function for suppressing messages
    def generic_messages_extended(org_func, message_flag, default_value):
        func_args = inspect.getargspec(org_func)
        idx = func_args[0].index("add_to_log")

        def generic_messages_wrapper(*args, **kwargs):
            if not message_flag:
                if len(args) > idx:  # replace add_to_log argument if passed
                    list_args = list(args)
                    list_args[idx] = False
                    args = tuple(list_args)
                elif kwargs.get("add_to_log", default_value) == True: # append or replace the keyword argument for suppressing the message
                    kwargs["add_to_log"] = False

            # run original function
            return org_func(*args, **kwargs)

        return generic_messages_wrapper

    # serum messages
    Person.apply_serum_study = generic_messages_extended(Person.apply_serum_study, persistent.serum_messages, True)
    Person.add_suggest_effect = generic_messages_extended(Person.add_suggest_effect, persistent.serum_messages, True)

    SerumDesign.run_on_turn = generic_messages_extended(SerumDesign.run_on_turn, persistent.serum_messages, False)
    SerumDesign.run_on_apply = generic_messages_extended(SerumDesign.run_on_apply, persistent.serum_messages, True)
    SerumDesign.run_on_remove = generic_messages_extended(SerumDesign.run_on_remove, persistent.serum_messages, False)
    SerumDesign.run_on_day = generic_messages_extended(SerumDesign.run_on_day, persistent.serum_messages, False)

    SerumTrait.run_on_turn = generic_messages_extended(SerumTrait.run_on_turn, persistent.serum_messages, False)
    SerumTrait.run_on_apply = generic_messages_extended(SerumTrait.run_on_apply, persistent.serum_messages, True)
    SerumTrait.run_on_remove = generic_messages_extended(SerumTrait.run_on_remove, persistent.serum_messages, False)
    SerumTrait.run_on_day = generic_messages_extended(SerumTrait.run_on_day, persistent.serum_messages, True)

    # clarity messages
    MainCharacter.change_masturbation_novelty = generic_messages_extended(MainCharacter.change_masturbation_novelty, persistent.clarity_messages, True)
    MainCharacter.change_locked_clarity = generic_messages_extended(MainCharacter.change_locked_clarity, persistent.clarity_messages, True)
    MainCharacter.convert_locked_clarity = generic_messages_extended(MainCharacter.convert_locked_clarity, persistent.clarity_messages, True)
    MainCharacter.spend_clarity = generic_messages_extended(MainCharacter.spend_clarity, persistent.clarity_messages, False)
    MainCharacter.add_clarity = generic_messages_extended(MainCharacter.add_clarity, persistent.clarity_messages, True)

    # stat changes
    Person.change_happiness = generic_messages_extended(Person.change_happiness, persistent.stat_change_messages, True)
    Person.change_love = generic_messages_extended(Person.change_love, persistent.stat_change_messages, True)
    Person.change_slut_temp = generic_messages_extended(Person.change_slut_temp, persistent.stat_change_messages, True)
    Person.change_slut_core = generic_messages_extended(Person.change_slut_core, persistent.stat_change_messages, True)
    Person.change_obedience = generic_messages_extended(Person.change_obedience, persistent.stat_change_messages, True)
    Person.change_arousal = generic_messages_extended(Person.change_arousal, persistent.stat_change_messages, True)
    Person.change_max_arousal = generic_messages_extended(Person.change_max_arousal, persistent.stat_change_messages, True)
    Person.change_novelty = generic_messages_extended(Person.change_novelty, persistent.stat_change_messages, True)
    Person.change_energy = generic_messages_extended(Person.change_energy, persistent.stat_change_messages, True)
    Person.change_max_energy = generic_messages_extended(Person.change_max_energy, persistent.stat_change_messages, True)

    MainCharacter.change_energy = generic_messages_extended(MainCharacter.change_max_energy, persistent.stat_change_messages, True)
    MainCharacter.change_max_energy = generic_messages_extended(MainCharacter.change_max_energy, persistent.stat_change_messages, True)

    # skill changes
    Person.change_cha = generic_messages_extended(Person.change_cha, persistent.skill_change_messages, True)
    Person.change_int = generic_messages_extended(Person.change_int, persistent.skill_change_messages, True)
    Person.change_focus = generic_messages_extended(Person.change_focus, persistent.skill_change_messages, True)
    Person.change_sex_skill = generic_messages_extended(Person.change_sex_skill, persistent.skill_change_messages, True)
