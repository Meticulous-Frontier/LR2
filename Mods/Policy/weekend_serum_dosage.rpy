# Weekend Serum Dosage policy - Original by Kaden

init -1 python:
    # extend the default run turn function
    def business_give_weekend_serum(org_func):
        def give_weekend_serum_wrapper(self):
            # run extension code prior to original function
            if time_of_day == 1 and weekend_serum_dosage_policy.is_active() and not self.is_work_day():
                self.give_daily_serum()
            # run original function
            org_func(self)

        return give_weekend_serum_wrapper

    # wrap up the give_weekend_serum function
    Business.run_turn = business_give_weekend_serum(Business.run_turn)

init 1 python:
    def weekend_serum_dosage_policy_requirement():
        if daily_serum_dosage_policy.is_owned():
            return True
        else:
            return False

    weekend_serum_dosage_policy = Policy(name = "Weekend Serum Dosage",
        desc = "Mandatory serum testing is expanded into the weekend. Each employee will receive two doses of the selected serum for their department to take over the weekend, if enough are currently in the stockpile.",
        cost = 10000,
        toggleable = True,
        requirement = weekend_serum_dosage_policy_requirement,
        dependant_policies = daily_serum_dosage_policy)

    serum_policies_list.append(weekend_serum_dosage_policy)
