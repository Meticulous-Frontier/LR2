## Stripclub storyline Mod by Corrado
#  Waitresses role definition.
#  The role is appended to waitresses after they start to work for you.

default stripclub_waitresses = MappedList(Person, all_people_in_the_game)

init 3304 python:
    list_of_instantiation_labels.append("instantiate_waitress_job")

    waitress_wardrobe = wardrobe_from_xml("Waitresses_Wardrobe")

    def strip_club_waitress_count():
        return __builtin__.len(stripclub_waitresses)

    def strip_club_hire_waitress(person):
        stripclub_waitresses.append(person)

    def strip_club_fire_waitress(person):
        if person in stripclub_waitresses:
            stripclub_waitresses.remove(person)

    stripclub_waitress_role = Role("Waitress", [promote_to_manager_action, strip_club_move_action, strip_club_fire_action, strip_club_performance_review_action],
        on_turn = stripclub_employee_on_turn, on_move = stripclub_employee_on_move, on_day = stripclub_employee_on_day, hidden = True)

label instantiate_waitress_job(stack = []):
    python:
        stripclub_waitress_job = Job("Waitress", stripclub_waitress_role, strip_club, strip_club_hire_waitress, strip_club_fire_waitress, work_days=[0,1,2,3,4,5,6], work_times = [3,4],
            mandatory_duties = [daily_serum_dosage_duty])
    $ execute_hijack_call(stack)
    return
