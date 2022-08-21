init -1 python:
    ###############################################
    # Custom Compare Functions For Clothing Class #
    ###############################################
    def clothing_compare(self, other):
        if isinstance(self, other.__class__):
            if self.name == other.name and self.is_extension == other.is_extension:
                return 0

        if self.__hash__() < other.__hash__():
            return -1
        else:
            return 1

    Clothing.__cmp__ = clothing_compare

    # add clothing hash function
    def clothing_hash(self):
        return hash((self.name, self.is_extension, self.pattern, self.half_off,
            tuple(x for x in map(hash, self.colour_pattern)),
            tuple(x for x in map(hash, self.colour)),
            ))

    Clothing.__hash__ = clothing_hash
    Clothing.hash = clothing_hash

    def clothing_eq(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name and self.is_extension == other.is_extension
        return False

    Clothing.__eq__ = clothing_eq

    def clothing_ne(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name or self.is_extension != other.is_extension
        return True

    Clothing.__ne__ = clothing_ne

    #######################################
    # Enhanced Methods For Clothing Class #
    #######################################

    def get_slut_value_enhanced(self):
        new_score = self.slut_value
        if WardrobeBuilder.clothing_in_preferences("skimpy outfits", self):
            new_score += 1
        # if WardrobeBuilder.clothing_in_preferences("conservative outfits", self):
        #     new_score -= 3
        if WardrobeBuilder.clothing_in_preferences("showing her tits", self):
            new_score += 2
        if WardrobeBuilder.clothing_in_preferences("showing her ass", self):
            new_score += 2
        if WardrobeBuilder.clothing_in_preferences("lingerie", self):
            new_score += 1
        if WardrobeBuilder.clothing_in_preferences("high heels", self):
            new_score += 1
        if self in [pumps, high_heels, leggings]:
            new_score += 3 # small extra modifier
        if self in [two_part_dress, thin_dress, nightgown_dress, thigh_high_boots, micro_skirt, daisy_dukes, jean_hotpants]:
            new_score += 5 # extremely slutty clothing (applies extra modifier)
        return new_score

    Clothing.get_slut_value = get_slut_value_enhanced