## Stripclub storyline Mod by Corrado
#  Waitresses role definition.
#  The role is appended to waitresses after they start to work for you.

init 3304 python:
    # Defined in base
    # def stripper_hire(the_person):
    #     if the_person not in stripclub_strippers:
    #         stripclub_strippers.append(the_person)

    def stripper_quit(person): # on_quit function called for strippers to make sure there's always someone working at the club. Also removes them from the list of dancers
        if person in stripclub_strippers:
            stripclub_strippers.remove(person)

    stripclub_stripper_role = Role("Stripper", get_stripper_role_actions() + [promote_to_manager_action, strip_club_move_action, strip_club_fire_action, strip_club_performance_review_action],
        on_turn = stripclub_employee_on_turn, on_move = stripclub_employee_on_move, on_day = stripclub_employee_on_day, hidden = True)
