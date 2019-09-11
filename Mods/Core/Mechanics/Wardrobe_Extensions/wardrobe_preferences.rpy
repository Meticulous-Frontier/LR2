init 0 python:
    # insert new opinions in list

    class WardrobePreference():
        makeup_list = [light_eye_shadow, heavy_eye_shadow, blush, lipstick]
        hide_ass_list = [lace_skirt, long_skirt, lab_coat, suitpants, long_tshirt, camisole]
        hide_tits_list = [lab_coat, dress_shirt, long_sleeve_blouse, tie_sweater, long_sweater, bath_robe]
        boots_list = [boot_heels, tall_boots, thigh_high_boots]
        high_heels_list = [pumps, heels, high_heels, boot_heels, thigh_high_boots]

        def __init__(self, person = None):
            if person is None:
                self.exclude_skirts = False
                self.exclude_pants = False
                self.exclude_dresses = False
                self.lingerie = False
                self.no_lingerie = False
                self.skimpy_outfits = False
                self.skimpy_uniforms = False
                self.conservative_outfits = False
                self.make_up = False
                self.no_make_up = False
                self.show_tits = False
                self.no_show_tits = False
                self.show_ass = False
                self.no_show_ass = False
                self.no_underwear = False
                self.prefer_boots = False
                self.no_boots = False
                self.prefer_high_heels = False
                self.no_high_heels = False
                self.no_clothes = False
                self.prefer_clothes = False
                return

            self.exclude_skirts, self.exclude_pants, self.exclude_dresses = self.get_skirt_dress_and_pants_preference(person)
            self.lingerie = person.get_opinion_score("lingerie") > 0
            self.no_lingerie = person.get_opinion_score("lingerie") < 0
            self.skimpy_outfits = person.get_opinion_score("skimpy outfits") > person.get_opinion_score("conservative outfits")
            self.skimpy_uniforms = person.get_opinion_score("skimpy uniforms") > person.get_opinion_score("conservative outfits")
            self.conservative_outfits = person.get_opinion_score("conservative outfits") > person.get_opinion_score("skimpy outfits")
            self.make_up = person.get_opinion_score("makeup") > 0
            self.no_make_up = person.get_opinion_score("makeup") < 0
            self.show_tits = person.get_opinion_score("showing her tits") > 0
            self.no_show_tits = person.get_opinion_score("showing her tits") < 0
            self.show_ass = person.get_opinion_score("showing her ass") > 0
            self.no_show_ass = person.get_opinion_score("showing her ass") < 0
            self.no_underwear = person.get_opinion_score("not wearing underwear") > 0 and person.get_opinion_score("lingerie") < person.get_opinion_score("not wearing underwear")
            self.prefer_boots = person.get_opinion_score("boots") > 0
            self.no_boots = person.get_opinion_score("boots") < 0
            self.prefer_high_heels = person.get_opinion_score("high heels") > 0
            self.no_high_heels = person.get_opinion_score("high heels") < 0
            self.no_clothes = person.get_opinion_score("not wearing anything") > 0
            self.prefer_clothes = person.get_opinion_score("not wearing anything") < 0

            # skimpy preference overrides conservative outfit choice
            if (self.skimpy_outfits or self.skimpy_uniforms):
                self.conservative_outfits = False

            #renpy.say("", "Person: " + person.name + "  " + person.last_name)
            # renpy.say("",  person.name + "  " + person.last_name + ": " + (self.exclude_skirts and "no skirts, " or "") + (self.exclude_pants and "no pants, " or "") + (self.lingerie and "lingerie, " or "") 
            #       + (self.skimpy_outfits and "skimpy outfits, " or "") + (self.conservative_outfits and "conservative outfits, " or "") + (self.make_up and "make-up, " or "") + (self.no_make_up and "no make-up, " or "")
            #       + (self.prefer_boots and "boots, " or "") + (self.no_boots and "no boots, " or "") + (self.prefer_high_heels and "high heels, " or "") + (self.no_high_heels and "no heels, " or ""))

        def evaluate_outfit(self, outfit, sluttiness_limit, sluttiness_min = 0):
            is_overwear = outfit.is_suitable_overwear_set()
            slut_score = is_overwear and outfit.get_overwear_slut_score() or outfit.get_full_outfit_slut_score()

            if not (slut_score <= sluttiness_limit and slut_score >= sluttiness_min):
                return False
            if len(outfit.upper_body + outfit.lower_body + outfit.feet) == 0:
                return False # No clothing at all should not be in person wardrobe by default
            if self.no_clothes and len(outfit.upper_body + outfit.lower_body + outfit.feet) > (is_overwear and 3 or 5):
                return False
            if self.prefer_clothes and len(outfit.upper_body + outfit.lower_body + outfit.feet) < (is_overwear and 2 or 4):
                return False
            if self.exclude_skirts and any(outfit.has_clothing(item) for item in skirts_list):
                return False
            if self.exclude_dresses and any(outfit.has_clothing(item) for item in dress_list):
                return False
            if self.exclude_pants and any(outfit.has_clothing(item) for item in pants_list):
                return False
            if (self.show_tits and any(outfit.has_clothing(item) for item in self.hide_tits_list)) or (self.no_show_tits and not any(outfit.has_clothing(item) for item in self.hide_tits_list)):
                return False
            if (self.show_ass and any(outfit.has_clothing(item) for item in self.hide_ass_list)) or (self.no_show_ass and not any(outfit.has_clothing(item) for item in self.hide_ass_list)):
                return False
            if (self.prefer_high_heels and not any(outfit.has_clothing(item) for item in self.high_heels_list)) or (self.no_high_heels and any(outfit.has_clothing(item) for item in self.high_heels_list)):
                return False
            if (self.prefer_boots and not any(outfit.has_clothing(item) for item in self.boots_list)) or (self.no_boots and any(outfit.has_clothing(item) for item in self.boots_list)):
                return False
            
            slut_modifier = person.get_opinion_score("conservative outfits")
            # checks differ when overwear or full outfit
            if is_overwear:
                if self.conservative_outfits and (slut_score > (15 + slut_modifier) or (outfit.tits_available() or outfit.vagina_available() or not outfit.bra_covered() or not outfit.panties_covered())):
                    return False
                if (self.skimpy_outfits or self.skimpy_uniforms) and not slut_score > (10 + slut_modifier) and (not outfit.tits_available() or not outfit.vagina_available()):
                    return False
            else:
                if self.conservative_outfits and (slut_score > (10 + slut_modifier) or (not outfit.wearing_panties() or not outfit.bra_covered() or not outfit.panties_covered())):
                    return False
                if (self.skimpy_outfits or self.skimpy_uniforms) and not slut_score > (5 + slut_modifier):
                    return False
                # only makeup check for full outfit
                if (self.no_make_up and any(outfit.has_clothing(item) for item in self.makeup_list)) or (self.make_up and not any(outfit.has_clothing(item) for item in self.makeup_list)):
                    return False

            #renpy.say("", "Add: " + outfit.name)
            return True

        def evaluate_underwear(self, underwear, sluttiness_limit, sluttiness_min = 0):
            slut_score = underwear.get_underwear_slut_score()

            if not (underwear.get_underwear_slut_score() <= sluttiness_limit and underwear.get_underwear_slut_score() >= sluttiness_min):
                return False
            if (not self.no_underwear and len(underwear.upper_body + underwear.lower_body + underwear.feet) < 1) or (self.no_underwear and len(underwear.upper_body + underwear.lower_body + underwear.feet)) > 1:
                return False
            if self.lingerie and (any(item.slut_value < 1 for item in underwear.lower_body) or any(item.slut_value < 1 for item in underwear.upper_body) or not underwear.wearing_panties()):
                return False
            if (self.no_lingerie or self.conservative_outfits) and (any(item.slut_value > 1 for item in underwear.lower_body) or any(item.slut_value > 1 for item in underwear.upper_body)):
                return False
            if (self.skimpy_outfits or self.skimpy_uniforms) and slut_score < 10:
                return False
            # no makeup check, default wardrobe has no underwear with makeup
            return True

        def get_skirt_dress_and_pants_preference(self, person):
            skirts_score = person.get_opinion_score("skirts")
            pants_score = person.get_opinion_score("pants")
            dress_score = person.get_opinion_score("dresses")
            exclude_skirts = skirts_score == -2
            exclude_pants = pants_score == -2
            exclude_dresses = dress_score == -2

            # break tigh when they don't like both.
            if exclude_skirts and exclude_pants and exclude_skirts:
                if pants_score > skirts_score and pants_score > dress_score:
                    exclude_pants = False
                elif skirts_score > pants_score and pants_score > dress_score: 
                    exclude_skirts = False
                elif dress_score > skirts_score and dress_score > pants_score:
                    exclude_dresses = False
            if exclude_skirts and exclude_pants and exclude_skirts:
                if dress_score > skirts_score:
                    exclude_dresses = False
                else:
                    exclude_skirts = False

            return (exclude_skirts, exclude_pants, exclude_dresses)