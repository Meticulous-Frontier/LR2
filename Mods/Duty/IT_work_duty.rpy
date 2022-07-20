init 1 python:
    def IT_work_duty_requirement(the_person):
        if mc.business.it_director:
            if the_person != mc.business.it_director:   #Don't let the IT director double dip
                return True
        return False

    def IT_work_duty_on_turn(the_person):
        if mc.business.IT_project_in_progress:
            mc.business.IT_increase_project_progress(amount = int((the_person.int * 2) + (the_person.focus))/3) #Not as much research as the IT director
        return



    IT_work_duty = Duty("Assist IT",
        "While working in Research and Development, have the employee assist with developing new IT projects.",
        requirement_function = IT_work_duty_requirement,
        on_turn_function = IT_work_duty_on_turn,
        only_at_work = True)

    general_rd_duties.append(IT_work_duty)
