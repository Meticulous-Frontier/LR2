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
        return hash((self.name, tuple(x for x in map(hash, self.upper_body)),
            tuple(x for x in map(hash, self.lower_body)),
            tuple(x for x in map(hash, self.feet)),
            tuple(x for x in map(hash, self.accessories))))

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

    # compare if clothing items match in each outfit (ignores accessories)
    def matches(self, other):
        current_clothing = self.upper_body + self.lower_body + self.feet
        other_clothing = other.upper_body + other.lower_body + other.feet

        if len(current_clothing) != len(other_clothing):
            return False

        return sorted(current_clothing) == sorted(other_clothing)

    Outfit.matches = matches

    #####################################
    # Enhanced Methods for Outfit Class #
    #####################################

    def remove_random_upper_enhanced(self, top_layer_first = False, do_not_remove = False):
        #if top_layer_first only the upper most layer is removed, otherwise anything unanchored is a valid target.
        #if do_not_remove is set to True we only use this to find something valid to remove and return that clothing item. this lets us use this function to find thigns to remove with an animation.
        #Returns None if there is nothing to be removed.
        to_remove = None
        if top_layer_first:
            #Just remove the very top layer
            if self.get_upper_unanchored():
                to_remove = self.get_upper_unanchored()[0]
                if to_remove.is_extension:
                    return None #Extensions can't be removed directly.
            else:
                return None
        else:
            to_remove = get_random_from_list(self.get_upper_unanchored())
            if to_remove and to_remove.is_extension:
                return None

        if to_remove and to_remove.layer == 0: # don not nipple covers or cinchers
            return None

        if to_remove and not do_not_remove:
            self.remove_clothing(to_remove)
        return to_remove

    Outfit.remove_random_upper = remove_random_upper_enhanced

    ######################################
    # Extension Methods For Outfit Class #
    ######################################

    def feet_available(self):
        return not any(x for x in self.feet if x.anchor_below)

    Outfit.feet_available = feet_available

    def feet_visible(self):
        return not any(x for x in self.feet if x.hide_below)

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

    def can_add_upper_enhanced(self, new_clothing):
        allowed = True
        for cloth in self.upper_body:
            if (cloth.layer == 0 and cloth.name == new_clothing.name) or (cloth.layer > 0 and cloth.layer == new_clothing.layer):
                allowed = False

        if new_clothing.has_extension: #It's a dress with a top and a bottom, make sure we can add them both!
            for cloth in self.lower_body:
                if cloth.layer == new_clothing.has_extension.layer:
                    allowed = False

        return allowed

    Outfit.can_add_upper = can_add_upper_enhanced

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
        for acc in [x for x in self.accessories if x.name in [mouth_cum.name, tits_cum.name, stomach_cum.name, face_cum.name, ass_cum.name, creampie_cum.name]]:
            self.accessories.remove(acc)
        return

    Outfit.remove_all_cum = remove_all_cum

    def has_glasses(self):
        return any([x for x in self.accessories if x.name in [big_glasses.name, modern_glasses.name]])

    Outfit.has_glasses = has_glasses

    def remove_glasses(self):
        for acc in [x for x in self.accessories if x.name in [big_glasses.name, modern_glasses.name]]:
            self.accessories.remove(acc)
        return

    Outfit.remove_glasses = remove_glasses

    def check_outfit_cum(self):                                             #Checks if the person has any cum on them
        return any([x for x in self.accessories if x.name in [mouth_cum.name, tits_cum.name, stomach_cum.name, face_cum.name, ass_cum.name, creampie_cum.name]])

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

    def get_underwear_body_parts_slut_score(self):
        new_score = 0
        if self.tits_visible() or self.tits_available():
            new_score += 16
        if self.vagina_visible() or self.vagina_available():
            new_score += 16
        return new_score

    Outfit.get_underwear_body_parts_slut_score = get_underwear_body_parts_slut_score

    def get_overwear_body_parts_slut_score(self):
        new_score = 0
        if self.tits_visible() or self.vagina_visible():
            new_score += 24
        if self.tits_visible():
            new_score += 12
        if self.vagina_visible():
            new_score += 12
        return new_score

    Outfit.get_overwear_body_parts_slut_score = get_overwear_body_parts_slut_score

    def get_full_outfit_body_parts_slut_score(self):
        # Full nudity should be no more than 80 sluttiness, per corporate_enforced_nudity_policy
        # Tries to be the sum of underwear/overwear scores
        # Exception: when not wearing panties, pants slightly less slutty than sum, skirts more slutty
        # Exception: when wearing only a shirt and panties or vice versa, sluttiness is much less than sum

        new_score = 0
        if self.tits_visible() or self.vagina_visible():
            new_score += 24

        if self.tits_visible():
            new_score += 12 + 16
        else:
            if self.wearing_bra():
                if not self.bra_covered():
                    new_score += 24
            else:
                new_score += 16

        if self.vagina_visible():
            new_score += 12 + 16
        else:
            if self.vagina_available():
                new_score += 8

            if self.wearing_panties():
                if not self.panties_covered():
                    new_score += 24
            else:
                new_score += 12

        return new_score

    Outfit.get_full_outfit_body_parts_slut_score = get_full_outfit_body_parts_slut_score

    def get_underwear_slut_score_enhanced(self): #Calculates the sluttiness of this outfit assuming it's an underwear set. We assume a modest overwear set is used (ie. one that covers visibility).
        new_score = 0
        new_score += self.get_underwear_body_parts_slut_score()
        new_score += self.get_total_slut_modifiers()
        return new_score if new_score < 100 else 100

    Outfit.get_underwear_slut_score = get_underwear_slut_score_enhanced

    def get_overwear_slut_score_enhanced(self): #Calculates the sluttiness of this outfit assuming it's an overwear set. That means we assume a modest underwear set is used (ie. one that denies access).
        new_score = 0
        new_score += self.get_overwear_body_parts_slut_score()
        new_score += self.get_total_slut_modifiers()
        return new_score if new_score < 100 else 100

    Outfit.get_overwear_slut_score = get_overwear_slut_score_enhanced

    def get_full_outfit_slut_score_enhanced(self): #Calculates the sluttiness of this outfit assuming it's a full outfit. Full penalties and such apply.
        new_score = 0
        new_score += self.get_full_outfit_body_parts_slut_score()
        new_score += self.get_total_slut_modifiers()
        return new_score if new_score < 100 else 100

    Outfit.get_full_outfit_slut_score = get_full_outfit_slut_score_enhanced

    def get_slut_value_classification(slut_requirement):
        classifications = ["Conservative", "Timid", "Modest", "Casual", "Trendy", "Stylish", "Enticing", "Provocative", "Sensual", "Sexy", "Seductive", "Sultry", "Slutty"]
        ci = __builtin__.int(slut_requirement * .14)
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
            if self.get_upper_ordered()[0].underwear and not self.get_upper_ordered()[0].layer == 0:
                return True
        return False

    Outfit.wearing_bra = wearing_bra_enhanced

    def get_full_strip_list_enhanced(self, strip_feet = True, strip_accessories = False): #TODO: This should support visible_enough at some point.
        items_to_strip = self.lower_body + [x for x in self.upper_body if x.layer > 0]
        if strip_feet:
            items_to_strip.extend(self.feet)
        if strip_accessories: # exclude make-up and earings
            items_to_strip.extend([x for x in self.accessories if not x in earings_list])
        items_to_strip.sort(key= lambda clothing: clothing.tucked, reverse = True) #Tucked upper body stuff draws after lower body.
        items_to_strip.sort(key= lambda clothing: clothing.layer) #Sort the clothing so it is removed top to bottom based on layer.

        extension_items = []
        for item in items_to_strip:
            if item.is_extension:
                extension_items.append(item)

        for item in extension_items:
            items_to_strip.remove(item) #Don't try and strip extension directly.
        return items_to_strip[::-1] #Put it in reverse order so when stripped it will be done from outside in.

    Outfit.get_full_strip_list = get_full_strip_list_enhanced

    def get_total_slut_modifiers_enhanced(self):
        new_score = 0
        for cloth in self.accessories + self.upper_body + self.lower_body + self.feet:
            new_score += cloth.get_slut_value()

            if cloth in [pinafore]:
                if not any(x for x in self.upper_body if x.layer == 1 or x.layer == 2):
                    new_score += 5 # tits not covered in pinafore
            if cloth in [lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear, leotard]:
                if not any(x for x in self.upper_body if x.layer == 2):
                    new_score += 5 # upper part not covered
                if not any(x for x in self.lower_body if x.layer == 2):
                    new_score += 10 # lower part not covered

        # take transparency of clothing into account for sluttiness score
        for cloth in [x for x  in self.upper_body + self.lower_body if x.colour[3] < 1 and x.layer in [1, 2]]:
            if cloth.layer == 2:
                new_score += __builtin__.int((1 - cloth.colour[3]) * 40)
            elif cloth.layer == 1:
                new_score += __builtin__.int((1 - cloth.colour[3]) * 10)

        return __builtin__.int(new_score  * .9)

    Outfit.get_total_slut_modifiers = get_total_slut_modifiers_enhanced

    #Categorizing outfits based on type
    def has_dress(self):
        return any(self.has_clothing(item) for item in real_dress_list)

    Outfit.has_dress = has_dress

    def has_skirt(self):
        return any(self.has_clothing(item) for item in skirts_list)

    Outfit.has_skirt = has_skirt

    def has_pants(self):
        return any(self.has_clothing(item) for item in pants_list)

    Outfit.has_pants = has_pants

    def has_shirt(self):
        return any(self.has_clothing(item) for item in shirts_list)

    Outfit.has_shirt = has_shirt

    def has_socks(self):
        return any(self.has_clothing(item) for item in only_socks_list)

    Outfit.has_socks = has_socks

    def has_hose(self):
        return any(self.has_clothing(item) for item in real_pantyhose_list)

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
