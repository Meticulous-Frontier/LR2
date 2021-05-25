init -1 python:
    config.label_overrides["pregnant_finish"] = "pregnant_finish_override"


label pregnant_finish_override(the_person):
    if the_person.is_mc_father():
        $ the_person.event_triggers_dict["kids_with_mc"] = the_person.event_triggers_dict.get("kids_with_mc", 0) + 1

    $ del config.label_overrides["pregnant_finish"]
    call pregnant_finish(the_person) from _call_pregnant_finish_enhanced
    $ config.label_overrides["pregnant_finish"] = "pregnant_finish_override"
    return
