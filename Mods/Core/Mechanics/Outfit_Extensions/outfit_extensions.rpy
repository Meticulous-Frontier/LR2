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

    def outfit_iterator(self):
        return iter(self.upper_body + self.lower_body + self.feet + self.accessories)

    Outfit.__iter__ = outfit_iterator

    #####################################
    # Enhanced Methods for Outfit Class #
    #####################################

    def generate_clothing_list_enhanced(self):
        def _cloth_sort_key(cloth):
            key = cloth.layer
            if cloth == leotard:
                key = 1.2 # for sorting to layer 1.2 (over underwear but under layer 2)
            if cloth == garter_with_fishnets:
                key = 1.3 # also draw above leotard
            if cloth in shirts_list + bracelet_list: # draw shirts over pants
                key += .1
            if cloth in neckwear_list: # move from layer 2 to 3.5 (between clothing and overwear)
                key += 1.5
            if cloth.tucked: # tucked is always a between layer value
                key += .5
            return key

        return sorted(self, key= lambda x: _cloth_sort_key(x))

    Outfit.generate_clothing_list = generate_clothing_list_enhanced

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

    def is_suitable_underwear_set_enhanced(self): #Returns true if the outfit could qualify as an underwear set.
        return not any(x for x in self if x.layer > 2)

    Outfit.is_suitable_underwear_set = is_suitable_underwear_set_enhanced

    def is_suitable_overwear_set_enhanced(self): #Returns true if the outfit could qualify as an overwear set.
        return not any(x for x in self if x.layer < 2)

    Outfit.is_suitable_overwear_set = is_suitable_overwear_set_enhanced

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
        for proper_name in ["Collar_Breed", "Collar_Cum_Slut", "Collar_Fuck_Doll", "Spiked_Choker"]:
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

    # Quickly make her show tits
    # ignores stripping logic where skirt / pants might be removed to show tits
    def remove_all_upper_clothing(self):
        for item in self.get_upper_ordered():
            self.remove_clothing(item)
        return
    Outfit.remove_all_upper_clothing = remove_all_upper_clothing

    def remove_bra(self):
        if self.wearing_bra():
            self.remove_clothing(self.get_bra())
        return
    Outfit.remove_bra = remove_bra

    def remove_panties(self):
        if self.wearing_panties():
            self.remove_clothing(self.get_panties())
        return
    Outfit.remove_panties = remove_panties

    def remove_bra_and_panties(self):
        self.remove_bra()
        self.remove_panties()
        return
    Outfit.remove_bra_and_panties = remove_bra_and_panties

    def get_overwear(self, exclude_upper = False, exclude_lower = False, exclude_feet = False, exclude_accessories = False, exclude_shoes = False):
        overwear = Outfit(self.name + " Overwear")
        if not exclude_upper:
            for item in [x for x in self.upper_body if x.layer >= 2 and not x.is_extension]:
                overwear.add_upper(item.get_copy())
        if not exclude_lower:
            for item in [x for x in self.lower_body if x.layer >= 2 and not x.is_extension]:
                overwear.add_lower(item.get_copy())
        if not exclude_feet:
            for item in [x for x in self.feet if x.layer >= (3 if exclude_shoes else 2)]:
                overwear.add_feet(item.get_copy())
        if not exclude_accessories:
            for item in [x for x in self.accessories if x.layer >= 2]:
                overwear.add_accessory(item.get_copy())
        return overwear
    Outfit.get_overwear = get_overwear

    def get_underwear(self, exclude_upper = False, exclude_lower = False, exclude_feet = False, exclude_accessories = False, exclude_shoes = False):
        underwear = Outfit(self.name + " Underwear")
        if not exclude_upper:
            for item in [x for x in self.upper_body if x.layer <= 2 and not x.is_extension]:
                underwear.add_upper(item.get_copy())
        if not exclude_lower:
            for item in [x for x in self.lower_body if x.layer <= 2 and not x.is_extension]:
                underwear.add_lower(item.get_copy())
        if not exclude_feet:
            for item in [x for x in self.feet if x.layer <= (1 if exclude_shoes else 2)]:
                underwear.add_feet(item.get_copy())
        if not exclude_accessories:
            for item in [x for x in self.accessories if x.layer <= 2]:
                underwear.add_accessory(item.get_copy())
        return underwear
    Outfit.get_underwear = get_underwear

    def is_wearing_underwear(self):
        return self.wearing_bra() or self.wearing_panties()
    Outfit.is_wearing_underwear = is_wearing_underwear

    def is_bra_visible(self):
        return self.wearing_bra() and not self.bra_covered()
    Outfit.is_bra_visible = is_bra_visible

    def are_panties_visible(self):
        return self.wearing_panties() and not self.panties_covered()
    Outfit.are_panties_visible = are_panties_visible

    def is_within_dress_code(self):
        slut_limit, underwear_limit, limited_to_top = mc.business.get_uniform_limits()
        easier_access = easier_access_policy.is_active()
        commando = commando_uniform_policy.is_active()

        # check if within sluttiness range (allow for slight overshoot)
        if self.get_full_outfit_slut_score() > slut_limit + 5:
            if self.get_overwear_slut_score() > slut_limit + 5:
                return False
            if not limited_to_top and self.get_underwear_slut_score() > underwear_limit + 5:
                return False
        if easier_access and not self.is_easier_access():
            return False
        if commando and self.wearing_panties():
            return False
        return True
    Outfit.is_within_dress_code = is_within_dress_code

    def get_body_parts_slut_score(self):
        tits_score = 0
        if self.tits_visible():
            tits_score += 30
        elif self.tits_available():
            tits_score += 15
        else:
            tits_score += (30 * _get_transparency_factor([x for x in self.upper_body]))

        vagina_score = 0
        if self.vagina_visible():
            vagina_score += 30
        elif self.vagina_available():
            vagina_score += 15
        else:
            vagina_score += 30 * _get_transparency_factor([x for x in self.lower_body])

        return __builtin__.int(tits_score + vagina_score)

    Outfit.get_body_parts_slut_score = get_body_parts_slut_score

    def get_underwear_slut_score_enhanced(self): #Calculates the sluttiness of this outfit assuming it's an underwear set. We assume a modest overwear set is used (ie. one that covers visibility).
        # showing tits or ass has ony 50% impact on underwear slut score (fully naked == 30 slut)
        new_score = __builtin__.int(self.get_body_parts_slut_score() * .5)
        new_score += self.get_total_slut_modifiers()
        return new_score if new_score < 100 else 100
    Outfit.get_underwear_slut_score = get_underwear_slut_score_enhanced

    def get_overwear_slut_score_enhanced(self): #Calculates the sluttiness of this outfit assuming it's an overwear set. That means we assume a modest underwear set is used (ie. one that denies access).
        new_score = self.get_body_parts_slut_score()
        new_score += self.get_total_slut_modifiers()
        return new_score if new_score < 100 else 100
    Outfit.get_overwear_slut_score = get_overwear_slut_score_enhanced

    def get_full_outfit_slut_score_enhanced(self): #Calculates the sluttiness of this outfit assuming it's a full outfit. Full penalties and such apply.
        new_score = self.get_body_parts_slut_score()
        new_score += self.get_total_slut_modifiers()
        # penalty for not having an overwear item
        if not any(x.layer >= 3 for x in self.upper_body):
            new_score += 15
        if not any(x.layer >= 3 for x in self.lower_body):
            new_score += 15
        return new_score if new_score < 100 else 100
    Outfit.get_full_outfit_slut_score = get_full_outfit_slut_score_enhanced

    def get_total_slut_modifiers_enhanced(self):
        return sum(x.get_slut_value() for x in self)
    Outfit.get_total_slut_modifiers = get_total_slut_modifiers_enhanced

    # Calculates effective visibility of body part under passed list
    # returns 1.0 (fully visible / 33% opacity)
    # returns 0 (fully hidden / >= 95% opacity)
    def _get_transparency_factor(cloth_list, overwear = False):
        alpha_values = [x.get_alpha() for x in cloth_list if x.hide_below and not (x.half_off and x.half_off_gives_access) and (not overwear or x.layer >= 2)]
        if not alpha_values:
            alpha_values = [0.0]

        avg_transparency = reduce(lambda x, y: x + y, alpha_values) / float(len(alpha_values))

        return 1.0 - __builtin__.min(1.0, __builtin__.max(0.0, (avg_transparency - .33))/(.95 - .33))

    def get_slut_value_classification(slut_requirement):
        classifications = ["Conservative", "Timid", "Modest", "Casual", "Trendy", "Stylish", "Enticing", "Provocative", "Sensual", "Sexy", "Seductive", "Sultry", "Slutty"]
        ci = __builtin__.int(slut_requirement * .14)
        if ci >= __builtin__.len(classifications):
            return classifications[-1]
        return classifications[ci]

    def build_outfit_name_custom(self):
        def get_clothing_items(outfit_part):
            return sorted([x for x in outfit_part if not x.is_extension and (x in [pinafore] or x.layer < 4)], key = lambda x: x.layer, reverse = True)

        outfitname = ""
        upper = get_clothing_items(self.upper_body)
        if upper:
            outfitname += upper[0].name

        lower = get_clothing_items(self.lower_body)
        if upper and lower:
            outfitname += " and "
        if lower:
            outfitname += lower[0].name

        feet = get_clothing_items(self.feet)
        if feet:
            if len(outfitname) == 0:
                outfitname = " with ".join([x.name for x in feet])
            else:
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
        return any(x for x in self.upper_body if (x.underwear and not x.layer == 0))
    Outfit.wearing_bra = wearing_bra_enhanced

    def get_bra_enhanced(self):
        return next((x for x in self.upper_body if x.underwear and not x.layer == 0), None)
    Outfit.get_bra = get_bra_enhanced

    def wearing_panties_enhanced(self):
        return any(x for x in self.lower_body if x.underwear and not x.layer == 0) \
            or any(x for x in self.upper_body if x in [leotard])
    Outfit.wearing_panties = wearing_panties_enhanced

    def get_panties_enhanced(self):
        return next((x for x in self.lower_body if x.underwear and not x.layer == 0), \
                next((x for x in self.upper_body if x in [leotard]), None))
    Outfit.get_panties = get_panties_enhanced

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

    # enhances original function to only return items
    # on layer 1 and higher
    def get_tit_strip_list_extended(org_func):
        def get_tit_strip_list_wrapper(outfit, visible_enough = True):
            result = org_func(outfit, visible_enough)
            # only return items not on layer 0 (for now cincher, heart_pasties)
            return [x for x in result if x.layer != 0]

        return get_tit_strip_list_wrapper

    Outfit.get_tit_strip_list = get_tit_strip_list_extended(Outfit.get_tit_strip_list)

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

    def shows_off_her_ass(self):
        if self.has_overwear():
            outfit = self.get_overwear()
            return any(x for x in outfit if x in WardrobeBuilder.preferences["showing her ass"]["lower_body"] + WardrobeBuilder.preferences["showing her ass"]["upper_body"])
        else:
            return any(x for x in self if x in WardrobeBuilder.preferences["showing her ass"]["lower_body"] + WardrobeBuilder.preferences["showing her ass"]["upper_body"])

    Outfit.shows_off_her_ass = shows_off_her_ass

    def shows_off_her_tits(self):
        if self.has_overwear():
            outfit = self.get_overwear()
            return any(x for x in outfit if x in WardrobeBuilder.preferences["showing her tits"])
        else:
            return any(x for x in self if x in WardrobeBuilder.preferences["showing her tits"])

    Outfit.shows_off_her_tits = shows_off_her_tits
