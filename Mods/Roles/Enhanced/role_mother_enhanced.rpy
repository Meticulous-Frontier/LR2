init 5 python:
    def mom_weekly_pay_requirement(the_person):
        if the_person.is_available and day%7 == 5: #It is the end of the day on friday
            return True
        return False

    def wear_promotion_outfit(person, is_planned = False):
        interview_outfit = person.event_triggers_dict.get("mom_work_promotion_outfit", None)
        if interview_outfit:
            if is_planned:
                person.next_day_outfit = interview_outfit.get_copy()
            person.planned_outfit = interview_outfit.get_copy() # also set it as planned so she doesn't change clothes on interactions
            person.apply_outfit(interview_outfit)
        return
