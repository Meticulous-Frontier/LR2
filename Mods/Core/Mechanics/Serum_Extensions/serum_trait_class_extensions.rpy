init -1 python:

    def serum_trait_compare(self,other):
        if isinstance(other, other.__class__):
            if self.name == other.name:
                return 0

        if self.__hash__() < other.__hash__():
            return -1
        else:
            return 1

    SerumTrait.__cmp__ = serum_trait_compare

    def serum_trait_hash(self):
        return hash(self.name)

    SerumTrait.__hash__ = serum_trait_hash
    SerumTrait.hash = serum_trait_hash

    def serum_trait_eq(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name
        return False

    SerumTrait.__eq__ = serum_trait_eq

    def serum_trait_ne(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name
        return True

    SerumTrait.__ne__ = serum_trait_ne

    def build_negative_slug_enhanced(self):
        return_slug = []

        if self.negative_slug:
            return_slug.append(self.negative_slug)

        if self.research_added > 0:
            return_slug.append("+" + str(self.research_added) + " Serum Research")

        if self.clarity_added > 0:
            return_slug.append("+" + str(self.clarity_added) + " Clarity to Unlock")

        if self.is_side_effect:
            return_slug.append("+" + str(self.flaws_aspect) + " Flaws")

        return ", ".join(return_slug)

    SerumTrait.build_negative_slug = build_negative_slug_enhanced
