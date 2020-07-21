init 2 python:
    def get_existing_parents(self, person):
        return_list = []
        for relationship in self.get_relationship_type_list(person):
            if relationship[1] == "Mother": #The only people we keep track of as characters are women, so the only parent relationship we care about are mothers
                return_list.append(relationship[0])
        return return_list

    RelationshipArray.get_existing_parents = get_existing_parents

    def get_existing_parent_count(self, person): #Returns a count of how many children this character has who are "real" characters, vs just a stat.
        return __builtin__.len(self.get_existing_parents(person))

    RelationshipArray.get_existing_parent_count = get_existing_parent_count

    def get_existing_sisters(self, person):
        return_list = []
        for relationship in self.get_relationship_type_list(person):
            if relationship[1] == "Sister": #The only people we keep track of as characters are women, so the only sibling relationships we care about are sisters
                return_list.append(relationship[0])
        return return_list

    RelationshipArray.get_existing_sisters = get_existing_sisters

    def get_family_members(self, person):
        return_list = []
        for relationship in self.get_relationship_type_list(person):
            if relationship[1] in ["Mother", "Daughter", "Sister", "Cousin", "Niece", "Aunt", "Grandmother", "Granddaughter"]: #The only people we keep track of as characters are women
                return_list.append(relationship[0])
        return return_list

    RelationshipArray.get_family_members = get_family_members
