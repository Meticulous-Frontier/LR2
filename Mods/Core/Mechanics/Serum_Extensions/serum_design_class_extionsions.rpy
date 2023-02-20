init 1 python:
    # Checks if the SerumDesign contains a specific trait based on its name.
    def has_trait(self, the_trait):
        return next((x for x in self.traits + self.side_effects if x == the_trait), None) is not None

    SerumDesign.has_trait = has_trait

    def get_slots_used(self):
        return len([x for x in self.traits if not "Production" in x.exclude_tags])

    SerumDesign.slots_used = property(get_slots_used, None, None, "Slots used in serum design")

    # override so we can pass the add_to_log parameter
    def generate_side_effects_enhanced(self, add_to_log = True): #Called when a serum is finished development. Tests all traits against their side effect chance and adds an effect for any that fail.
        for trait in self.traits:
            if trait.test_effective_side_effect_chance():
                valid_side_effects = []
                for side_effect_trait in list_of_side_effects:
                    valid_side_effect = True #Check to make sure we don't have conflicting trait tags.
                    for tag in side_effect_trait.exclude_tags:
                        for checking_trait in self.traits + self.side_effects:
                            if tag in checking_trait.exclude_tags:
                                valid_side_effect = False
                    if valid_side_effect:
                        valid_side_effects.append(side_effect_trait)

                the_side_effect = renpy.random.choice(valid_side_effects)
                self.add_trait(the_side_effect, is_side_effect = True)
                if add_to_log:
                    mc.log_event(self.name + " developed side effect " + the_side_effect.name + " due to " + trait.name, "float_text_blue")

    SerumDesign.generate_side_effects = generate_side_effects_enhanced

    def serum_design_update_attention_extended(org_func):
        def update_attention_wrapper(serum_design):
            # original function
            org_func(serum_design)
            # extension code
            max_value = serum_design.attention
            if max_value > 0 and clinical_testing in serum_design.traits:
                max_value -= 1
            serum_design.attention = max_value

        return update_attention_wrapper

    SerumDesign.update_attention = serum_design_update_attention_extended(SerumDesign.update_attention)
