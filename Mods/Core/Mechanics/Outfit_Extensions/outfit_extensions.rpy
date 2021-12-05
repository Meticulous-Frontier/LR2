init -1 python:
    #############################################
    # Custom Compare Functions For Outfit Class #
    #############################################
    def outfit_compare(self, other):
        if isinstance(self, other.__class__):
            if self.name == other.name:
                return 0

        if self.__hash__() < other.__hash__():
            return -1
        else:
            return 1

    Outfit.__cmp__ = outfit_compare

    # add outfit hash function
    def outfit_hash(self):
        return hash(self.name)

    Outfit.__hash__ = outfit_hash
    Outfit.hash = outfit_hash

    def outfit_eq(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name
        return False

    Outfit.__eq__ = outfit_eq

    def outfit_ne(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name
        return True

    Outfit.__ne__ = outfit_ne

    ######################################
    # Extension Methods For Outfit Class #
    ######################################

    def feet_available(self):
        reachable = True
        for cloth in self.feet:
            if cloth.anchor_below:
                reachable = False
        return reachable

    Outfit.feet_available = feet_available

    def feet_visible(self):
        visible = True
        for cloth in self.feet:
            if cloth.hide_below:
                visible = False
        return visible

    Outfit.feet_visible = feet_visible

    def can_remove_bra(self):
        if not self.wearing_bra():
            return False
        bra = self.get_bra()
        unanchored = self.get_upper_unanchored()
        return bra in unanchored

    Outfit.can_remove_bra = can_remove_bra

    def can_remove_panties(self):
        if not self.wearing_panties():
            return False
        panties = self.get_panties()
        unanchored = self.get_lower_unanchored()
        return panties in unanchored

    Outfit.can_remove_panties = can_remove_panties

    def has_overwear(self): #Returns true if the outfit has layer 2 clothing items for upper and lower body.
        if any(x in [nightgown_dress] for x in self.upper_body):
            return False
        if not any(x.layer >= 2 for x in self.upper_body):
            return False
        if not any(x.layer >= 2 for x in self.lower_body):
            return False
        return True

    Outfit.has_overwear = has_overwear

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

    def has_mouth_cum(self):
        return any(x.name == mouth_cum.name for x in self.accessories)

    Outfit.has_mouth_cum = has_mouth_cum

    def has_tits_cum(self):
        return any(x.name == tits_cum.name for x in self.accessories)

    Outfit.has_tits_cum = has_tits_cum

    def has_stomach_cum(self):
        return any(x.name == stomach_cum.name for x in self.accessories)

    Outfit.has_stomach_cum = has_stomach_cum

    def has_face_cum(self):
        return any(x.name == face_cum.name for x in self.accessories)

    Outfit.has_face_cum = has_face_cum

    def has_ass_cum(self):
        return any(x.name == ass_cum.name for x in self.accessories)

    Outfit.has_ass_cum = has_ass_cum

    def has_creampie_cum(self):
        return any(x.name == creampie_cum.name for x in self.accessories)

    Outfit.has_creampie_cum = has_creampie_cum

    def full_access(self):
        return (self.tits_visible() and self.tits_available() and not self.wearing_bra()
            and self.vagina_visible() and self.vagina_available() and not self.wearing_panties()
            and not any(x.layer >= 2 for x in self.upper_body if not x.half_off)
            and not any(x.layer >= 2 for x in self.lower_body if not x.half_off))

    Outfit.full_access = full_access

    def remove_all_collars(self):
        for proper_name in ["Collar_Breed", "Collar_Cum_Slut", "Collar_Fuck_Doll", "Spiked_Choker", "Wide_Choker"]:
            found = find_in_list(lambda x: x.proper_name == proper_name, self.accessories)
            if found:
                self.accessories.remove(found)
        return

    Outfit.remove_all_collars = remove_all_collars

    def get_body_parts_slut_score(self, extra_modifier = False):
        new_score = 0
        if self.tits_available():
            new_score += 15
        elif self.tits_visible():
            new_score += 30
        if extra_modifier and (not self.wearing_bra() or not self.bra_covered()):
            new_score += 15

        if self.vagina_available():
            new_score += 15
        elif self.vagina_visible():
            new_score += 30
        if extra_modifier and (not self.wearing_panties() or not self.panties_covered()):
            new_score += 15
        return new_score

    Outfit.get_body_parts_slut_score = get_body_parts_slut_score

    def get_underwear_slut_score_enhanced(self): #Calculates the sluttiness of this outfit assuming it's an underwear set. We assume a modest overwear set is used (ie. one that covers visibility).
        new_score = 0
        new_score += self.get_body_parts_slut_score()
        new_score += self.get_total_slut_modifiers()
        return new_score

    Outfit.get_underwear_slut_score = get_underwear_slut_score_enhanced

    def get_overwear_slut_score_enhanced(self): #Calculates the sluttiness of this outfit assuming it's an overwear set. That means we assume a modest underwear set is used (ie. one that denies access).
        new_score = 0
        new_score += self.get_body_parts_slut_score()
        new_score += self.get_total_slut_modifiers()
        return new_score

    Outfit.get_overwear_slut_score = get_overwear_slut_score_enhanced

    def get_full_outfit_slut_score_enhanced(self): #Calculates the sluttiness of this outfit assuming it's a full outfit. Full penalties and such apply.
        new_score = 0
        new_score += self.get_body_parts_slut_score(extra_modifier = True)
        new_score += self.get_total_slut_modifiers()
        return new_score

    Outfit.get_full_outfit_slut_score = get_full_outfit_slut_score_enhanced

    def get_slut_value_classification(slut_requirement):
        classifications = ["Conservative", "Timid", "Modest", "Casual", "Trendy", "Stylish", "Enticing", "Provocative", "Sensual", "Sexy", "Seductive", "Sultry", "Slutty"]
        ci = (slut_requirement + 5) // 7
        if ci >= __builtin__.len(classifications):
            return classifications[-1]
        return classifications[ci]

    def build_outfit_name_custom(self):
        def get_clothing_items(outfit_part):
            for layer in range(2, 0, -1):
                items = filter(lambda x: x.layer == layer, outfit_part)
                if items:
                    return items
            return None

        outfitname = ""

        upper = get_clothing_items(self.upper_body)
        if upper:
            outfitname += upper[0].name

        if not upper or (not upper[0].has_extension or upper[0].has_extension.layer <= 1):
            lower = get_clothing_items(self.lower_body)
            if upper and lower:
                outfitname += " and "
            if lower:
                outfitname += lower[0].name

        feet = get_clothing_items(self.feet)
        if feet:
            if __builtin__.len(outfitname) != 0:
                outfitname += " with "
            outfitname += feet[0].name

        if __builtin__.len(outfitname) == 0:
            return "Naked"

        self.name = get_slut_value_classification(self.get_full_outfit_slut_score()) + " " + outfitname

        return self.name

    Outfit.build_outfit_name = build_outfit_name_custom

    def update_name(self):
        self.name = self.build_outfit_name()
        return

    Outfit.update_name = update_name

# initialize this part after wardrobe builder is initialized
init 6 python:
    def wearing_bra_enhanced(self): # specific cloth items don't count as bra
        if self.upper_body:
            if self.get_upper_ordered()[0].underwear and not self.get_upper_ordered()[0] in [cincher, heart_pasties]:
                return True
        return False

    Outfit.wearing_bra = wearing_bra_enhanced

    def get_total_slut_modifiers_enhanced(self):
        new_score = 0
        for cloth in self.accessories + self.upper_body + self.lower_body + self.feet:
            new_score += cloth.slut_value
            if WardrobeBuilder.clothing_in_preferences("skimpy outfits", cloth):
                new_score += 1
            # if WardrobeBuilder.clothing_in_preferences("conservative outfits", cloth):
            #     new_score -= 3
            if WardrobeBuilder.clothing_in_preferences("showing her tits", cloth):
                new_score += 2
            if WardrobeBuilder.clothing_in_preferences("showing her ass", cloth):
                new_score += 2
            if WardrobeBuilder.clothing_in_preferences("lingerie", cloth):
                new_score += 1
            if WardrobeBuilder.clothing_in_preferences("high heels", cloth):
                new_score += 1
            if cloth in [pumps, high_heels, leggings]:
                new_score += 3 # small extra modifier
            if cloth in [two_part_dress, thin_dress, nightgown_dress, thigh_high_boots, micro_skirt, daisy_dukes, jean_hotpants]:
                new_score += 5 # extremely slutty clothing (applies extra modifier)
            if cloth in [pinafore]:
                if not any(x for x in self.upper_body if x.layer == 1 or x.layer == 2):
                    new_score += 5 # tits not covered in pinafore
            if cloth in [lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear, leotard]:
                if not any(x for x in self.upper_body if x.layer == 2):
                    new_score += 5 # upper part not covered
                if not any(x for x in self.lower_body if x.layer == 2):
                    new_score += 10 # lower part not covered

        # take transparency of clothing into account for sluttiness score
        for cloth in self.upper_body + self.lower_body:
            if cloth.colour[3] < 1:
                if cloth.layer == 2:
                    new_score += int((1 - cloth.colour[3]) * 40)
                elif cloth.layer == 1:
                    new_score += int((1 - cloth.colour[3]) * 10)

        return new_score

    Outfit.get_total_slut_modifiers = get_total_slut_modifiers_enhanced

    #Categorizing outfits based on type

    def is_dress(self):
        if any(self.has_clothing(item) for item in real_dress_list):
            return True
        return False

    Outfit.is_dress = is_dress

    def has_skirt(self):
        if any(self.has_clothing(item) for item in skirts_list):
            return True
        return False

    Outfit.has_skirt = has_skirt

    def has_pants(self):
        if any(self.has_clothing(item) for item in pants_list):
            return True
        return False

    Outfit.has_pants = has_pants

    def has_shirt(self):
        if any(self.has_clothing(item) for item in shirts_list):
            return True
        return False

    Outfit.has_shirt = has_shirt

    def has_socks(self):
        if any(self.has_clothing(item) for item in only_socks_list):
            return True
        return False

    Outfit.has_socks = has_socks

    def has_hose(self):
        if any(self.has_clothing(item) for item in real_pantyhose_list):
            return True
        return False

    Outfit.has_hose = has_hose

    # enhances original function to only return items
    # on layer 1 and higher
    def get_tit_strip_list_extended(org_func):
        def get_tit_strip_list_wrapper(outfit, visible_enough = True):
            result = org_func(outfit, visible_enough)
            # only return items not on layer 0 (for now cincher, heart_pasties)
            return [x for x in result if x.layer != 0]

        return get_tit_strip_list_wrapper

    Outfit.get_tit_strip_list = get_tit_strip_list_extended(Outfit.get_tit_strip_list)
