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

    def vagina_visible_enhanced(self):
            return self.get_lower_body_transparency_factor() >= 1.0

    Outfit.vagina_visible = vagina_visible_enhanced

    def tits_visible_enhanced(self):
            return self.get_upper_body_transparency_factor() >= 1.0

    Outfit.tits_visible = tits_visible_enhanced


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

    def is_easier_access(self):
        return not any(x for x in self.lower_body if x.layer >= 2 and x.anchor_below)
    Outfit.is_easier_access = is_easier_access

    def make_easier_access(self):
        changed = False
        if self.has_pants():
            swap_outfit_bottoms(self)
            changed = True

        for item in self.upper_body:
            if item.is_similar(pinafore):
                new_item_top = vest.get_copy()
                new_item_top.colour = item.colour
                new_item_bottom = skirt.get_copy()
                new_item_bottom.colour = item.colour
                self.remove_clothing(item)
                self.add_upper(new_item_top)
                self.add_lower(new_item_bottom)
                changed = True
        for item in self.lower_body:
            if item.is_similar(long_skirt) or item.is_similar(pencil_skirt):
                new_item = skirt.get_copy()
                new_item.colour = item.colour
                self.remove_clothing(item)
                self.add_lower(new_item)
                changed = True
        return changed
    Outfit.make_easier_access = make_easier_access

    def remove_bra_and_panties(self):
        if self.wearing_panties():
            self.remove_clothing(self.get_panties())
        if self.wearing_bra():
            self.remove_clothing(self.get_bra())
        # Special handling for leotards
        # TODO: delete when `remove_clothing()` can remove using extensions
        for clothing in self.upper_body:
            if clothing.is_similar(leotard):
                self.remove_clothing(clothing)
        return
    Outfit.remove_bra_and_panties = remove_bra_and_panties

    def get_overwear(self):
        overwear = Outfit(self.name + " Overwear")
        overwear.upper_body = list(x for x in self.upper_body if x.layer >= 2)
        overwear.lower_body = list(x for x in self.lower_body if x.layer >= 2)
        overwear.feet = list(x for x in self.feet if x.layer >= 2)
        overwear.accessories = list(x for x in self.accessories if x.layer >= 2)
        return overwear
    Outfit.get_overwear = get_overwear

    def get_underwear(self):
        underwear = Outfit(self.name + " Underwear")
        underwear.upper_body = list(x for x in self.upper_body if x.layer < 2)
        underwear.lower_body = list(x for x in self.lower_body if x.layer < 2)
        underwear.feet = list(x for x in self.feet if x.layer < 2)
        underwear.accessories = list(x for x in self.accessories if x.layer < 2)
        return underwear
    Outfit.get_underwear = get_underwear

    def is_within_dress_code(self, slut_limit = None, underwear_limit = None, easier_access = None, commando = None):
        business_slut_limit, business_underwear_limit, _limited_to_top = mc.business.get_uniform_limits()
        if slut_limit is None:
            slut_limit = business_slut_limit + 5 # A bit of leeway
        if underwear_limit is None:
            underwear_limit = business_underwear_limit + 5 # A bit of leeway
        if easier_access is None:
            easier_access = easier_access_policy.is_active()
        if commando is None:
            commando = commando_uniform_policy.is_active()

        if self.get_full_outfit_slut_score() > slut_limit:
            if self.get_overwear().get_overwear_slut_score() > slut_limit:
                return False
            if self.get_underwear().get_underwear_slut_score() > underwear_limit:
                return False
        if easier_access and not self.is_easier_access():
            return False
        if commando and (self.wearing_bra() or self.wearing_panties()):
            return False
        return True
    Outfit.is_within_dress_code = is_within_dress_code

    # Calculates transparency on a scale 0.0--1.0, with 0.0 being opaque
    def get_lower_body_transparency(self):
        transparency = 1.0
        for cloth in self.lower_body:
            if cloth.hide_below and not (cloth.half_off and cloth.half_off_gives_access):
                transparency *= 1 - cloth.colour[3]
        return transparency

    Outfit.get_lower_body_transparency = get_lower_body_transparency

    # Calculates body part effective visibility, where 1.0 is fully visible (66% opacity)
    def get_lower_body_transparency_factor(self):
        trans = self.get_lower_body_transparency()
        factor = (trans - .05)/(.33 - .05) # 5% transparency is opaque, 33% transparency is visible
        return __builtin__.max(0.0, __builtin__.min(1.0, factor))

    Outfit.get_lower_body_transparency_factor = get_lower_body_transparency_factor

    # Calculates transparency on a scale 0.0--1.0, with 0.0 being opaque
    def get_upper_body_transparency(self):
        transparency = 1.0
        for cloth in self.upper_body:
            if cloth.hide_below and not cloth in [vest, suit_jacket] and not (cloth.half_off and cloth.half_off_gives_access):
                transparency *= 1 - cloth.colour[3]
        return transparency

    Outfit.get_upper_body_transparency = get_upper_body_transparency

    # Calculates body part effective visibility, where 1.0 is fully visible (66% opacity)
    def get_upper_body_transparency_factor(self):
        trans = self.get_upper_body_transparency()
        factor = (trans - .05)/(.33 - .05) # 5% transparency is opaque, 33% transparency is visible
        return __builtin__.max(0.0, __builtin__.min(1.0, factor))

    Outfit.get_upper_body_transparency_factor = get_upper_body_transparency_factor

    def get_underwear_body_parts_slut_score(self):
        # No underwear is 32 slut
        # 16 from bra, 16 from panties
        new_score = 0
        if self.tits_available():
            new_score += 16
        else:
            new_score += __builtin__.int(16 * self.get_upper_body_transparency_factor())
        if self.vagina_available():
            new_score += 16
        else:
            new_score += __builtin__.int(16 * self.get_lower_body_transparency_factor())
        return new_score

    Outfit.get_underwear_body_parts_slut_score = get_underwear_body_parts_slut_score

    def get_overwear_body_parts_slut_score(self):
        # No overwear is 48 slut
        # 12 from upper body, 12 from lower body, 24 from general visibility
        new_score = 0
        u_factor = self.get_upper_body_transparency_factor()
        l_factor = self.get_lower_body_transparency_factor()
        new_score += __builtin__.int(24 * __builtin__.max(u_factor, l_factor)) # The most visible body part contributes the most to sluttiness
        new_score += __builtin__.int(12 * u_factor)
        new_score += __builtin__.int(12 * l_factor)
        return new_score

    Outfit.get_overwear_body_parts_slut_score = get_overwear_body_parts_slut_score

    def get_full_outfit_body_parts_slut_score(self):
        # Full nudity should be no more than 80 sluttiness, per corporate_enforced_nudity_policy
        # 32 slut from underwear, 24 slut from overwear, 24 slut from general visibility
        # Tries to be the sum of underwear/overwear scores
        # Exception: when not wearing panties, pants slightly less slutty than sum, skirts more slutty
        # Exception: opacity is subtractive, not additive. The math gets a bit weird, but it should be continuous

        new_score = 0
        u_factor = self.get_upper_body_transparency_factor()
        l_factor = self.get_lower_body_transparency_factor()

        new_score += __builtin__.int(24 * __builtin__.max(u_factor, l_factor)) # The most visible body part contributes the most to sluttiness

        tits_score = 0
        if self.wearing_bra():
            if not self.bra_covered():
                tits_score += 24
        else:
            tits_score = 16
        new_score += __builtin__.max(tits_score, __builtin__.int((12 + 16) * u_factor)) # Floor at tits visibility slut score. 12 from overwear scores, 16 from underwear.

        vagina_score = 0
        if self.vagina_available():
            vagina_score += 8
        if self.wearing_panties():
            if not self.panties_covered():
                vagina_score += 24
        else:
            vagina_score += 12 # This is lower than tits equivalent by half "vagina_available" factor
        new_score += __builtin__.max(vagina_score, __builtin__.int((12 + 16) * l_factor)) # Floor at vagina visibility slut score. 12 from overwear scores, 16 from underwear.

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
        return __builtin__.int(new_score * 0.9)

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
