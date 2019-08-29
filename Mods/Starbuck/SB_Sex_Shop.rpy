init -1 python:
    class Sex_Shop_Owner(Person):
        shop_progress_stage = 0
        shop_investment_total = 0
        shop_investment_rate = 0
        shop_stage_one_investment_total = 0
        shop_stage_two_investment_total = 0
        shop_stage_three_investment_total = 0
        shop_invest_one_max = 5000
        shop_invest_two_max = 20000
        shop_invest_three_max = 30000
        shop_owner_relationship_stage = 0

        def run_day(self):
            if self.shop_progress_stage > 0:
                investment_return = self.calc_investment_return()
                if (investment_return > 0) :
                    mc.business.funds += investment_return
                    business_message = "Sex shop has returned $" + str(investment_return) + " on your investment!"
                    mc.business.add_normal_message(business_message)

            super(Sex_Shop_Owner, self).run_day()
        pass

        def calc_investment_return(self):
            investment_return = 0
            if self.shop_progress_stage > 0:
                investment_return += (30 * store.shop_difficulty_value)
                investment_return += int (self.shop_stage_one_investment_total * self.shop_investment_rate * 0.01 * store.shop_difficulty_value)
            if self.shop_progress_stage > 1:
                investment_return += int (self.shop_stage_two_investment_total * self.shop_investment_rate * 0.006 * store.shop_difficulty_value)
            if self.shop_progress_stage > 2:
                investment_return += int (self.shop_stage_three_investment_total * self.shop_investment_rate * 0.004 * store.shop_difficulty_value)
            return investment_return

        def run_turn(self):
            super(Sex_Shop_Owner, self).run_turn()  #Make us

            sb_random_action = renpy.random.randint(0,100)
            current_action = "None"
            if sb_random_action <= 25:
                current_action = "masturbate"

            #TODO Move to an action, using renpy.call will interrupt the advance_time_people_run_turn_label preventing 
            #    the run_turn on some person objects (all that are after SB in the people_to_process list)
            #    suggestion: move to the SB_fetish_anal_event source code file and add appropriate action to mandatory list
            #                to make sure it is repeated, add it to the mandatory list again at end of label (since the executed action will be removed)
            #                the same it is done for the mom_weekly_pay_action event
            #TODO make it so MC can set option at PC to be notified when starbuck masturbates

            if self.event_triggers_dict.get("sb_fetish", "None") == "Anal": #She has an anal fetish#

                sb_event_chance = renpy.random.randint(0,100)
                if sb_event_chance < 10:   #TODO make this chance moddable at PC
                #NOTE: if this condition is true no further code can be run in this block#
                    if current_action == "masturbate":
                        renpy.call("starbuck_anal_fetish_masturbate", False) #Ends this python block
                        return #Doesn't matter because it has already returned
                    elif self.arousal > 60:
                        renpy.call("starbuck_anal_fetish_request",False)
                        return
                    else:
                        renpy.call("starbuck_anal_fetish_checkup",False)
                        return




            #super(Sex_Shop_Owner, self).run_turn()
        pass
