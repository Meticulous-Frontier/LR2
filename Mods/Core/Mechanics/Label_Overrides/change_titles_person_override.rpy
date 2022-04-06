init -1 python:
    config.label_overrides["change_titles_person"] = "change_titles_person_override"

    def build_title_selection_menu(person):
        person_titles = []
        mc_titles = []
        person_possessive_titles = []

        for title in get_titles(person):
            person_titles.append([title, [0, title]])
        for title in get_player_titles(person):
            mc_titles.append([title, [1, title]])
        for title in get_possessive_titles(person):
            person_possessive_titles.append([title, [2, title]])

        person_titles.insert(0, "Their Title")
        mc_titles.insert(0, "Your Title")
        person_possessive_titles.insert(0, "Possessive Title")

        return [person_titles, mc_titles, person_possessive_titles]

label change_titles_person_override(the_person):
    call screen enhanced_main_choice_display(build_menu_items(build_title_selection_menu(the_person)))
    if _return[0] == 0:
        $ the_person.set_title(_return[1])
    elif _return[0] == 1:
        $ the_person.set_mc_title(_return[1])
    elif _return[0] == 2:
        $ the_person.set_possessive_title(_return[1])
    return
