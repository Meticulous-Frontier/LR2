init -1 python:
    def strip_club_give_daily_serum():
        for person in people_in_role([stripper_role, stripclub_waitress_role, stripclub_manager_role, stripclub_mistress_role, bdsm_performer_role]):
            if person.is_employee():
                continue

            if person.has_role(stripper_role) and getattr(mc.business, "strippers_serum", None):
                strip_club_give_daily_serum_to_person(person, mc.business.strippers_serum)
            if person.has_role(stripclub_waitress_role) and getattr(mc.business, "waitresses_serum", None):
                strip_club_give_daily_serum_to_person(person, mc.business.waitresses_serum)
            if person.has_role([stripclub_manager_role, stripclub_mistress_role]) and getattr(mc.business, "manager_serum", None):
                strip_club_give_daily_serum_to_person(person, mc.business.manager_serum)
            if person.has_role(stripclub_bdsm_performer_role) and getattr(mc.business, "bdsm_performers_serum", None):
                strip_club_give_daily_serum_to_person(person, mc.business.bdsm_performers_serum)
        return

    def strip_club_give_daily_serum_to_person(person, group_serum):
        if not mc.business.inventory.get_serum_count(group_serum) > 0:
            return

        mc.business.inventory.change_serum(group_serum, -1)
        person.give_serum(copy.copy(group_serum), add_to_log = False)
        return

    # extend the default run day function
    def business_give_daily_serum_extended(org_func):
        def give_daily_serum_wrapper(business):
            # run original function
            org_func(business)
            # run extension code
            if get_strip_club_foreclosed_stage() >= 5:  # only when player owns strip club
                strip_club_give_daily_serum()

        return give_daily_serum_wrapper

    # wrap up the give_daily_serum function
    Business.give_daily_serum = business_give_daily_serum_extended(Business.give_daily_serum)
