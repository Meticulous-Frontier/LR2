init 1 python:

    # check if any serum in inventory has passed SerumTrait
    # usage example python:
    #   if mc.inventory.has_serum_with_trait(blood_brain_pen):
    #       # DO SOMETHING
    def has_serum_with_trait(self, the_trait):
        return next((x for x in self.get_serum_type_list() if x.has_trait(the_trait)), None) is not None

    SerumInventory.has_serum_with_trait = has_serum_with_trait

    # list of all SerumDesigns that contain the passed SerumTrait
    # usage example python:
    #    the_serum = get_random_from_list(mc.inventory.get_serums_with_trait(breast_enhancement))
    #    if the_serum:
    #        mc.inventory.change_serum(the_serum,-1)
    #        the_person.give_serum(copy.copy(the_serum), add_to_log = True)

    def get_serums_with_trait(self, the_trait):
        return [x for x in self.get_serum_type_list() if x.has_trait(the_trait)]

    SerumInventory.get_serums_with_trait = get_serums_with_trait

    def get_serum_type_list_enhanced(self):
        return list(set([x[0] for x in self.serums_held]))

    SerumInventory.get_serum_type_list = get_serum_type_list_enhanced
