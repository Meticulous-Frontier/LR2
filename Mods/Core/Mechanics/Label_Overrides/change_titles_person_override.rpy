init -1 python:
    config.label_overrides["change_titles_person"] = "change_titles_person_override"

label change_titles_person_override(the_person):

    call screen enhanced_main_choice_display(build_menu_items(build_title_selection_menu(the_person)))
    if _return in get_titles(the_person): # Is it nescessary to check if it's already their title?
        $ the_person.set_title(_return)
    elif _return in get_player_titles(the_person):
        $ the_person.set_mc_title(_return)
    elif _return in get_possessive_titles(the_person):
        $ the_person.set_possessive_title(_return)
    return


init 2 python:
    def build_title_selection_menu(the_person):
        person_titles = []
        mc_titles = []
        person_possessive_titles = []

        for title in get_titles(the_person):
            person_titles.append([title, title])
        for title in get_player_titles(the_person):
            mc_titles.append([title, title])
        for title in get_possessive_titles(the_person):
            person_possessive_titles.append([title, title])

        person_titles.insert(0, "Their Title")
        mc_titles.insert(0, "Your Title")
        person_possessive_titles.insert(0, "Possessive Title")

        return [person_titles, mc_titles, person_possessive_titles]
