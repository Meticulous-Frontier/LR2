# Overrides part of the existing Position class with enhanced versions
init 5 python:
    # include a visual indication
    def build_position_willingness_string_enhanced(self, the_person): #Generates a string for this position that includes a tooltip and coloured willingness for the person given.
        willingness_string = ""
        tooltip_string = ""

        girl_expected_arousal = str(int(self.girl_arousal * (1 + 0.1 * mc.sex_skills[self.skill_tag]))) #Estimate what they'll gain based on both of your skills to make the predictions as accurate as possible.
        guy_expected_arousal = str(int(self.guy_arousal * (1 + 0.1 * the_person.sex_skills[self.skill_tag])))

        energy_string = "\n{color=#3C3CFF}" + str(self.guy_energy) + "{/color}/{color=#F0A8C0}" + str(self.girl_energy) + "{/color} {image=gui/extra_images/energy_token.png}"
        arousal_string =  ", {color=#3C3CFF}" + guy_expected_arousal + "{/color}/{color=#F0A8C0}" + girl_expected_arousal + "{/color} {image=gui/extra_images/arousal_token.png}"

        disable = False

        slut_modifier = 0
        if self.opinion_tags:
            for opinion_tag in self.opinion_tags:
                slut_modifier += the_person.get_opinion_score(opinion_tag)

        effective_sluttiness = the_person.effective_sluttiness() + slut_modifier 

        if effective_sluttiness > self.slut_cap:
            if the_person.arousal > self.slut_cap:
                willingness_string = "{color=#6b6b6b}Boring{/color}" #No sluttiness gain AND half arousal gain
                tooltip_string = " (tooltip)This position is too boring to interest her when she is this horny. No sluttiness increase and her arousal gain is halved."
            else:
                willingness_string = "{color=#3C3CFF}Comfortable{/color}" #No sluttiness
                tooltip_string = " (tooltip)This position is too tame for her tastes. No sluttiness increase, but it may still be a good way to get warmed up and ready for other positions."
        elif effective_sluttiness > self.slut_requirement:
            willingness_string = "{color=#3DFF3D}Exciting{/color}" #Normal sluttiness gain
            tooltip_string = " (tooltip)This position pushes the boundary of what she is comfortable with. Increases temporary sluttiness, which may become permanent over time or with serum application."
        elif effective_sluttiness + the_person.obedience-100 > self.slut_requirement:
            willingness_string = "{color=#FFFF3D}Likely Willing if Commanded{/color}"
            tooltip_string = " (tooltip)This position is beyond what she would normally consider. She is obedient enough to do it if she is commanded, at the cost of some happiness."
        else:
            willingness_string = "{color=#FF3D3D}Likely Too Slutty{/color}"
            tooltip_string = " (tooltip)This position is so far beyond what she considers appropriate that she would never dream of it."

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
            return self.name + position_opinion + "\n{size=22}"+ willingness_string + "{/size}" + " (disabled)" #Don't show the arousal and energy string if it's disabled to prevent overrun
        else:
            return self.name + position_opinion + "\n{size=22}" + willingness_string + energy_string + arousal_string + "{/size}" + tooltip_string

    Position.build_position_willingness_string = build_position_willingness_string_enhanced