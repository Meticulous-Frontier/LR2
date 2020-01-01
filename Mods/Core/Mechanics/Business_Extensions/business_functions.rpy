init -1 python:
    def change_funds(self, amount, add_to_log = True):
        self.funds += amount

        if add_to_log:
            if amount >= 0:
                mc.log_event(self.name + " received: " + "$" + str(abs(amount)), "float_text_green")
            else:
                mc.log_event(self.name + " payed: " + "$" + str(abs(amount)), "float_text_green")

        return

    # Add Pay function to business object
    Business.change_funds = change_funds

    def change_line_weight_enhanced(self,line,weight_change): # Allow values above 100 ( it is capped by production_remaining anyway)

        cs = renpy.current_screen()
        production_remaining = cs.scope["production_remaining"]
        production_max = cs.scope["production_max"]

        if line in self.serum_production_array:
            used_production = self.get_used_line_weight()
            if weight_change > 0 and weight_change + used_production > production_max:
                weight_change = production_remaining - used_production # Side effect of this is that if you try to over cap it resets to 0%, but I think we want that.

            self.serum_production_array[line][1] += weight_change
            if self.serum_production_array[line][1] < 0:
                self.serum_production_array[line][1] = 0 #We cannot have a value less than 0%

    Business.change_line_weight = change_line_weight_enhanced
