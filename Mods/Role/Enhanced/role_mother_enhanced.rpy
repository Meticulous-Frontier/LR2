init 5 python:
    def wear_promotion_outfit(person, is_planned = False):
        interview_outfit = person.event_triggers_dict.get("mom_work_promotion_outfit", None)
        if interview_outfit:
            if is_planned:
                person.next_day_outfit = interview_outfit.get_copy()
            person.apply_outfit(interview_outfit)
        return
