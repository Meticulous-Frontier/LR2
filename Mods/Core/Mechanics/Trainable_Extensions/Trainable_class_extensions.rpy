init 2 python: #Trainable declared at -2
    def trainable_get_cost_enhanced(self, the_person):
        base_modified_cost = self.base_cost * (2**(the_person.training_log[self.training_tag]/self.doubling_amount))
        trance_modifier = 2.0
        if the_person.has_exact_role(heavy_trance_role):
            trance_modifier = 1.0
        elif the_person.has_exact_role(very_heavy_trance_role):
            trance_modifier = 0.5

        # mc.log_event("Custom cost function run", "float_text_green")

        if mc_serum_feat_hypnotist.is_active():
            if mc_serum_feat_hypnotist.get_trait_tier() == 2:
                trance_modifier = trance_modifier * 0.8
            elif mc_serum_feat_hypnotist.get_trait_tier() >= 3:
                trance_modifier = trance_modifier * 0.6

        return int(base_modified_cost*trance_modifier)

    Trainable.get_cost = trainable_get_cost_enhanced
