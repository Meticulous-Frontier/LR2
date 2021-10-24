init 2 python:
    # maid knows her work locations by using add_work_location / remove_work_location
    # then set her schedule (preferably alt_schedule) to be in one of these locations
    # she will automatically wear a maid outfit when she moves to the location and unlock actions.

    maid_wardrobe = wardrobe_from_xml("Maid_Wardrobe")

    def add_maid_work_location(person, location):
        if not location.identifier in person.event_triggers_dict.get("maid_work_location_identifiers", []):
            if not "maid_work_location_identifiers" in person.event_triggers_dict.keys():
                person.event_triggers_dict["maid_work_location_identifiers"] = []
            person.event_triggers_dict["maid_work_location_identifiers"].append(location.identifier)

    def remove_maid_work_location(person, location):
        if location.identifier in person.event_triggers_dict.get("maid_work_location_identifiers", []):
            person.event_triggers_dict["maid_work_location_identifiers"].remove(location.identifier)

    def clear_maid_work_locations(person):
        if "maid_work_location_identifiers" in person.event_triggers_dict.keys():
            person.event_triggers_dict.pop("maid_work_location_identifiers")

    def maid_at_work(person):
        return person.location.identifier in person.event_triggers_dict.get("maid_work_location_identifiers", [])

    def maid_on_move(person):
        return

    def maid_on_turn(person):
        if maid_at_work(person):    # at end of maid work time slot she gets paid.
            mc.business.change_funds(-50)
        return

    def maid_slap_ass_requirement(person):
        if person.obedience > 120:
            return maid_at_work(person)
        return False

    def maid_grope_requirement(person):
        if person.love > 20:
            return maid_at_work(person)
        return False

    def maid_service_requirement(person):
        if person.sluttiness > 40:
            return maid_at_work(person)
        return False

    maid_slap_ass_action = Action("Slap Maid", maid_slap_ass_requirement, "maid_slap_ass_label")
    maid_grope_action = Action("Grope Maid", maid_grope_requirement, "maid_grope_label")
    maid_service_action = Action("Maid Service", maid_service_requirement, "maid_service_label")

    maid_role = Role("Maid", actions = [
            maid_slap_ass_action,
            maid_grope_action,
            maid_service_action
        ],
        hidden = True, on_turn = maid_on_turn, on_move = maid_on_move)


label maid_slap_ass_label(the_person):
    return

label maid_grope_label(the_person):
    return

label maid_service_label(the_person):
    return