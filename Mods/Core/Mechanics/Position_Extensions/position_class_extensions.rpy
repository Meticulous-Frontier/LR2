# Overrides part of the existing Position class with enhanced versions
init 5 python:
    # include a visual indication
    def build_position_willingness_string_enhanced(self, the_person, ignore_taboo = False): #NOTE: Returns a list instead of string. If you want it to be a single string then do "".join(position.build_position_willingness_string(the_person))
    #Generates a list of strings for this position that includes a tooltip and coloured willingness for the person given.

        willingness_string = ""
        tooltip_string = ""

        girl_expected_arousal = str(int(self.girl_arousal * (1 + 0.1 * mc.sex_skills[self.skill_tag]))) #Estimate what they'll gain based on both of your skills to make the predictions as accurate as possible.
        guy_expected_arousal = str(int(self.guy_arousal * (1 + 0.1 * the_person.sex_skills[self.skill_tag])))

        energy_string = "   {color=#A3A3FF}" + str(self.guy_energy) + "{/color}/{color=#FF6EC7}" + str(self.girl_energy) + "{/color} {image=energy_token_small}"
        arousal_string =  ", {color=#A3A3FF}" + guy_expected_arousal + "{/color}/{color=#FF6EC7}" + girl_expected_arousal + "{/color} {image=arousal_token_small}"

        disable = False
        position_taboo = self.associated_taboo

        if ignore_taboo:
            position_taboo = None

        final_slut_requirement = self.slut_requirement
        final_slut_cap = self.slut_cap
        if self.skill_tag == "Anal" and the_person.has_family_taboo():
            final_slut_requirement += -10 #It's easier to convince a family member to have anal sex, since it's not "real" incest or something.
            final_slut_cap += -10
        elif self.skill_tag == "Vaginal" and the_person.has_family_taboo():
            final_slut_requirement += 10 #It's harder to convince a family member to have vaginal sex
            final_slut_cap += 10

        if self.opinion_tags:
            for opinion_tag in self.opinion_tags:
                final_slut_cap += the_person.get_opinion_score(opinion_tag)
                final_slut_requirement += the_person.get_opinion_score(opinion_tag)

        taboo_break_string = ""
        if the_person.has_taboo(position_taboo):
            taboo_break_string = " {image=taboo_break} "

        #NOTE: Removed the (tooltip) and (disabled) tags as they aren't needed in the screen which is their only use case at the moment, but consider adding those back in if being used in the renpy.display_menu
        if the_person.effective_sluttiness(position_taboo) > final_slut_cap:
            if the_person.arousal > final_slut_cap:
                willingness_string = "{color=#6b6b6b}Boring{/color}" #No sluttiness gain AND half arousal gain
                tooltip_string = " (tooltip) This position is too boring to interest her when she is this horny. No sluttiness increase and her arousal gain is halved."
            else:
                willingness_string = "{color=#A3A3FF}Comfortable{/color}" #No sluttiness
                tooltip_string = " (tooltip) This position is too tame for her tastes. No sluttiness increase, but it may still be a good way to get warmed up and ready for other positions."
        elif the_person.effective_sluttiness(position_taboo) >= final_slut_requirement:
            willingness_string = "{color=#3DFF3D}Exciting{/color}" #Normal sluttiness gain
            tooltip_string = " (tooltip) This position pushes the boundary of what she is comfortable with. Increases temporary sluttiness, which may become permanent over time or with serum application."
        elif the_person.effective_sluttiness(position_taboo) + the_person.obedience-100 >= final_slut_requirement:
            willingness_string = "{color=#FFFF3D}Likely Willing if Commanded{/color}"
            tooltip_string = " (tooltip) This position is beyond what she would normally consider. She is obedient enough to do it if she is commanded, at the cost of some happiness."
        else:
            willingness_string = "{color=#FF3D3D}Likely Too Slutty{/color}"
            tooltip_string = " (tooltip) This position is so far beyond what she considers appropriate that she would never dream of it."

        if the_person.has_taboo(position_taboo):
            tooltip_string +=" (tooltip) \nSuccessfully selecting this position will break a taboo, making it easier to convince " + the_person.title + " to do it and similar acts in the future."

        if not self.check_clothing(the_person):
            disable = True
            willingness_string += "\nObstructed by clothing"
        elif mc.recently_orgasmed and self.requires_hard:
            disable = True
            willingness_string += "\nRecently orgasmed"
        elif mc.energy < self.guy_energy and the_person.energy < self.girl_energy:
            disable = True
            willingness_string += "\nYou're both too tired"
        elif mc.energy < self.guy_energy:
            disable = True
            willingness_string += "\nYou're too tired"
        elif the_person.energy < self.girl_energy:
            disable = True
            willingness_string += "\nShe's too tired"

        change_amount = 0
        if self.opinion_tags:
            for opinion_tag in self.opinion_tags:
                opinion_topic = the_person.get_opinion_topic(opinion_tag)
                if opinion_topic:
                    # renpy.say("", the_person.name + ": " + opinion_tag + " => " + str(the_person.get_opinion_score(opinion_tag)))
                    if opinion_topic[1]: # only show info when opinion is known
                        change_amount += the_person.get_opinion_score(opinion_tag) #Add a bonus or penalty if she likes or dislikes the position.

        position_opinion = ""
        if change_amount > 0:
            position_opinion = " {image=thumbs_up}"
        elif change_amount < 0:
            position_opinion = " {image=thumbs_down}"

        if disable:
            return taboo_break_string + self.name + position_opinion + "\n{size=22}" + willingness_string + "{/size}" + " (disabled)" #Don't show the arousal and energy string if it's disabled to prevent overrun
        else:
            return taboo_break_string + self.name + position_opinion + "\n{size=22}" + willingness_string + energy_string + arousal_string + "{/size}" + tooltip_string

    Position.build_position_willingness_string = build_position_willingness_string_enhanced
