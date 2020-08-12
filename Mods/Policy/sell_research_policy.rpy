# Sell research policy (Original by BadRabbit)

init 1310 python:

    def sell_research_policy_requirement():
        return True

    sell_research_policy = Policy(
        name = "Sell Research Capacity",
        cost = 500,
        desc = "Your company has lab facilities that you use for research. Other organizations could utilize your facilities for their purposes. When this policy is active you will sell your research capacity to earn some money, but you will make no progress in your own research.",
        toggleable = True,
        requirement = sell_research_policy_requirement,
    )

    serum_policies_list.append(sell_research_policy)

    # extend the default business research_progress function
    def business_research_progress_extended(org_func):
        def research_progress_wrapper(business, int, focus, skill):
            if sell_research_policy.is_active():
                cash_earned = __builtin__.round(((3*int) + (focus) + (2*skill) + 10) * (business.team_effectiveness))/100
                if business.head_researcher:    # more cash based on head researcher skill
                    cash_earned *= 1.0 + ((business.head_researcher.int - 2) * 0.05)

                mc.business.funds += cash_earned
                return 0
            else:
                # run original function
                return org_func(business, int, focus, skill)

        return research_progress_wrapper

    # wrap up the research_progress function
    Business.research_progress = business_research_progress_extended(Business.research_progress)
