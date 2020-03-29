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

    # Based on suggestion from DaMatt on F95Zone
    def change_production_enhanced(self,new_serum,production_line):
        if "machinery_room_overload" in globals(): # Should not cause issues if not present.
            production_max = machinery_room_overload
        else:
            production_max = 100

        if production_line in self.serum_production_array: #If it already exists, change the serum type and production points stored, but keep the weight for that line (it can be changed later)
            self.serum_production_array[production_line][0] = new_serum
            self.serum_production_array[production_line][1] = int(production_max - self.get_used_line_weight() + self.serum_production_array[production_line][1]) #Set the production weight to everything we have remaining
            self.serum_production_array[production_line][2] = 0 #Set production points stored to 0 for the new serum
            self.serum_production_array[production_line][3] = -1 #Set autosell to -1, ie. don't auto sell.
        else: #If the production line didn't exist before, add a key for that line.
            self.serum_production_array[production_line] = [new_serum, int(production_max - self.get_used_line_weight()), 0, -1]

    Business.change_production = change_production_enhanced

    def is_trait_researched(self, trait):
        research_trait = find_in_list(lambda x: x.name == trait.name, list_of_traits)
        if research_trait:
            return research_trait.researched
        return False

    Business.is_trait_researched = is_trait_researched