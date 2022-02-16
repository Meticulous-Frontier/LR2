## Stripclub storyline Mod by Corrado
#  Waitresses role definition.
#  The role is appended to waitresses after they start to work for you.

init 3304 python:
    def strip_club_hire_waitress():
        stripclub_waitresses.append(person)

    def strip_club_fire_waitress(person):
        if person in stripclub_waitresses:
            stripclub_waitresses.remove(person)

    waitress_wardrobe = wardrobe_from_xml("Waitresses_Wardrobe")

    stripclub_waitress_role = Role("Waitress", [promote_to_manager_action, strip_club_stripper_fire_action, strip_club_stripper_performance_review_action], hidden = True)
