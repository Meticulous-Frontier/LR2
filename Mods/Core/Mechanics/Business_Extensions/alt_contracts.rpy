# alternative way of creating contracts
# generates
init 2 python:
    def generate_contract(contract_tier = 0):

        serum = SerumDesign()

        weighted_production_traits = [[t, (t.tier + 1) * 2] for t in [x for x in list_of_traits if x.researched and "Production" in x.exclude_tags]]
        serum.add_trait(get_random_from_weighted_list(weighted_production_traits) or primitive_serum_prod)

        if serum.slots >= 2:  # key part of serums is suggestion
            weighted_suggestion_traits = [[t, (t.tier + 1) * 2] for t in [x for x in list_of_traits if x.researched and "Suggest" in x.exclude_tags]]
            serum.add_trait(get_random_from_weighted_list(weighted_suggestion_traits) or suggestion_drugs_trait)

        count = 0
        while serum.slots_used() < serum.slots and count < 10: # try to add traits in a loop for a max of 10 tries
            weighted_traits = [[t, (t.tier + 1) * 2] for t in [x for x in list_of_traits if x.researched and not "Production" in x.exclude_tags and not x in serum.traits]]
            trait = get_random_from_weighted_list(weighted_traits)
            if trait and serum.trait_add_allowed(trait):
                serum.add_trait(trait)
            count += 1

        serum.generate_side_effects(add_to_log = False)

        aspect_list = ["mental","physical","sexual","medical"]
        aspect_value_list = [serum.mental_aspect, serum.physical_aspect, serum.sexual_aspect, serum.medical_aspect]

        sorted_aspect_list = sorted(((value, index) for index, value in enumerate(aspect_value_list)), reverse=True)

        # pick primary and secondary aspect
        primary_aspect = aspect_list[sorted_aspect_list[0][1]]
        secondary_aspect = aspect_list[sorted_aspect_list[1][1]]

        # print("Main aspects: " + primary_aspect + " - " + secondary_aspect)
        # print("Traits:" + ", ".join([x.name for x in serum.traits]))

        contract_name, contract_description = get_contract_description(primary_aspect, secondary_aspect, contract_tier)

        contract_length = 3 + (renpy.random.randint(0,3+contract_tier) * renpy.random.randint(0,3+contract_tier))

        amount_desired = 5*(contract_tier+renpy.random.randint(1,3))*(contract_tier+renpy.random.randint(1,3))


        new_contract = Contract(contract_name, contract_description, contract_length,
            mental_requirement = serum.mental_aspect, physical_requirement = serum.physical_aspect,
            sexual_requirement = serum.sexual_aspect, medical_requirement = serum.medical_aspect,
            flaw_tolerance = serum.flaws_aspect, attention_tolerance = serum.attention, amount_desired = amount_desired)

        return new_contract
