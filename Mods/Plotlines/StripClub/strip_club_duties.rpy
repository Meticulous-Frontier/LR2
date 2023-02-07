init 1 python:
    def strip_club_init_serums():
        # init stripclub daily serum attributes
        mc.business.strippers_serum = None
        mc.business.waitresses_serum = None
        mc.business.bdsm_performers_serum = None
        mc.business.manager_serum = None
        return

    def stripclub_employee_on_turn(the_person):
        #Each turn check to see if the person wants to quit.
        for duty in the_person.duties:
            if the_person.is_at_work() or not duty.only_at_work:
                duty.on_turn(the_person)
        return

    def stripclub_employee_on_move(the_person):
        for duty in the_person.duties:
            if the_person.is_at_work() or not duty.only_at_work:
                duty.on_move(the_person)
        return

    def stripclub_employee_on_day(the_person):
        for duty in the_person.duties:
            if the_person.event_triggers_dict.get("worked_today", False) or not duty.only_at_work: #Only perform on_day functions if they had work that day.
                duty.on_day(the_person)

        the_person.event_triggers_dict["worked_today"] = False #Reset this for the next day.
        return
