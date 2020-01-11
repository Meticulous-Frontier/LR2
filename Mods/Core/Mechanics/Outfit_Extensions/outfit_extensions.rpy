

init -1 python:
    def remove_all_cum(self):
        remove_list = []
        for acc in self.accessories:
            if acc.name in [mouth_cum.name, tits_cum.name, stomach_cum.name, face_cum.name, ass_cum.name, creampie_cum.name]:
                remove_list.append(acc)
        for acc in remove_list:
            self.accessories.remove(acc)
        return

    Outfit.remove_all_cum = remove_all_cum

    def check_outfit_cum(self):                                             #Checks if the person has any cum on them
        for acc in self.accessories:
            if acc.name in [mouth_cum.name, tits_cum.name, stomach_cum.name, face_cum.name, ass_cum.name, creampie_cum.name]:
                return True
        return False

    Outfit.check_outfit_cum = check_outfit_cum

    def remove_all_collars(self):
        for proper_name in ["Collar_Breed", "Collar_Cum_Slut", "Collar_Fuck_Doll"]:
            found = find_in_list(lambda x: x.proper_name == proper_name, self.accessories)
            if found:
                self.accessories.remove(found)
        return

    Outfit.remove_all_collars = remove_all_collars

    def get_overwear_slut_score_enhanced(self): #Calculates the sluttiness of this outfit assuming it's an overwear set. That means we assume a modest underwear set is used (ie. one that denies access).
        new_score = 0
        if self.tits_visible():
            new_score += 20
        elif self.tits_available():
            new_score += 10

        if self.vagina_visible():
            new_score += 20
        elif self.vagina_available():
            new_score += 10

        new_score += self.get_total_slut_modifiers()

        return new_score

    Outfit.get_overwear_slut_score = get_overwear_slut_score_enhanced

    def build_outfit_name_custom(self):
        def get_name_classification(slut_requirement):
            if slut_requirement <= 20:
                return "Conservative"
            if slut_requirement <= 40:
                return "Casual"
            if slut_requirement <= 60:
                return "Relaxed"
            if slut_requirement <= 80:
                return "Sexy"
            return "Slutty"

        def get_clothing_items(outfit_part):
            items = filter(lambda x: x.layer == 2, outfit_part)
            if not items:
                items = filter(lambda x: x.layer == 1, outfit_part)
            return items

        outfitname = ""

        upper = get_clothing_items(self.upper_body)
        if upper:
            outfitname += upper[0].name

        if not upper or not upper[0].has_extension:
            lower = get_clothing_items(self.lower_body)
            if upper and lower:
                outfitname += " and "
            if lower:
                outfitname += lower[0].name

        if len(outfitname) == 0:
            feet = get_clothing_items(self.feet)
            if feet:
                outfitname = feet[0].name

        if len(outfitname) == 0:
            return "Naked"

        self.update_slut_requirement()
        self.name = get_name_classification(self.slut_requirement) + " " + outfitname

        return self.name

    Outfit.build_outfit_name = build_outfit_name_custom

# initialize this part after wardrobe builder is initialized
init 6 python:
    def tits_available_enhanced(self):
        for cloth in self.upper_body:
            if cloth.anchor_below and not cloth in [cincher, heart_pasties]:
                return False
        return True

    Outfit.tits_available = tits_available_enhanced

    def get_total_slut_modifiers_enhanced(self):
        def clothing_in_preferences(topic, clothing):
            for layer in WardrobeBuilder.preferences[topic].keys():
                if clothing in WardrobeBuilder.preferences[topic][layer]:
                    return True
            return False

        new_score = 0
        for cloth in self.accessories + self.upper_body + self.lower_body + self.feet:
            new_score += cloth.slut_value
            if clothing_in_preferences("skimpy outfits", cloth):
                new_score += 1
            if clothing_in_preferences("conservative outfits", cloth):
                new_score -= 3
            if clothing_in_preferences("showing her tits", cloth):
                new_score += 2
            if clothing_in_preferences("showing her ass", cloth):
                new_score += 2
            if clothing_in_preferences("lingerie", cloth):
                new_score += 1
            if clothing_in_preferences("high heels", cloth):
                new_score += 1
            if cloth in [pumps, high_heels, leggings]:
                new_score += 5 # small extra modifier
            if cloth in [summer_dress, virgin_killer, evening_dress]:
                new_score += 10 # sexy modifier
            if cloth in [two_part_dress, thin_dress, nightgown_dress, thigh_high_boots, micro_skirt]:
                new_score += 15 # extremely slutty clothing (applies extra modifier)
            if cloth in [lacy_one_piece_underwear, lingerie_one_piece, leotard]:
                if not any(x for x in self.upper_body if x.layer == 2):
                    new_score += 10 # upper part not covered
                if not any(x for x in self.lower_body if x.layer == 2):
                    new_score += 10 # lower part not covered

        return new_score if new_score > 0 else 0

    Outfit.get_total_slut_modifiers = get_total_slut_modifiers_enhanced
