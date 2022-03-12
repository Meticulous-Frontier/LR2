init 2 python:
    def policy_compare(self,other): #
        if isinstance(self, other.__class__):
            if self.name == other.name:
                return 0

        if self.__hash__() < other.__hash__():
            return -1
        else:
            return 1

    Policy.__cmp__ = policy_compare

    def policy_hash(self):
        return hash(self.name)

    Policy.__hash__ = policy_hash
    Policy.hash = policy_hash

    def policy_eq(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name
        return False

    Policy.__eq__ = policy_eq

    def policy_ne(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name
        return True

    Policy.__ne__ = policy_ne

    # alter policy descriptions to match values in get_uniform_limits_enhanced()
    strict_uniform_policy.desc = "Requiring certain styles of attire in the business world is nothing new. Allows you to designate overwear sets of sluttiness 10 or less as part of your business uniform."
    relaxed_uniform_policy.desc = "Corporate dress code is broadened to include more casual apparel. You can designate overwear sets up to sluttiness 20 as part of your business uniform."
    casual_uniform_policy.desc = "Corporate dress code is broadened even further. Overwear sets up to 30 sluttiness are now valid uniforms."
    reduced_coverage_uniform_policy.desc = "The term \"appropriate coverage\" in the employee manual is redefined and subject to employer approval. You can now use full outfits or underwear sets as part of your corporate uniform. Underwear sets must have a sluttiness score of 15 or less, outfits to 40 or less."
    minimal_coverage_uniform_policy.desc = "Corporate dress code is broadened further. Uniforms must now only meet a \"minimum coverage\" requirement, generally nothing more than a set of bra and panties. Full uniforms can have a sluttiness score of 60, underwear sets can go up to 30."
    corporate_enforced_nudity_policy.desc = "Corporate dress code is removed in favor of a \"need to wear\" system. All clothing items that are deemed non-essential are subject to employer approval. Conveniently, all clothing is deemed non-essential. Full outfit sluttiness is limited to 80 or less, underwear sets have no limit."
