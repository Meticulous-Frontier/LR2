## Automatic Only Fanatics Account Creation Crisis Mod by Tristimdorion
init 2 python:
    def auto_onlyfans_account_requirement():
        if mc.business.is_weekend():
            return not get_person_without_onlyfans_account() is None
        return False

    def auto_onlyfans_account_person_requirement(person):
        if person.has_role(onlyfans_role):
            return False
        elif person.effective_sluttiness() < 50 - (5 * (person.get_opinion_score("showing her tits") + person.get_opinion_score("showing her ass") + person.get_opinion_score("public sex"))):
            return False
        return True

    def get_person_without_onlyfans_account():
        return get_random_from_list([x for x in all_people_in_the_game(unique_character_list) if auto_onlyfans_account_person_requirement(x)])

    def auto_create_onlyfans_account():
        person = get_person_without_onlyfans_account()
        if person:
            person.add_role(onlyfans_role)
        return

    auto_onlyfans_account_action = ActionMod("Automatic Only Fanatics", auto_onlyfans_account_requirement, "auto_onlyfans_account_action_label",
        menu_tooltip = "When a girl becomes slutty enough she will open a Only Fanatics account on her own (no user dialogs).", category = "Misc", is_crisis = True, crisis_weight = 5)

label auto_onlyfans_account_action_label():
    $ auto_create_onlyfans_account()
    return
