# Overrides part of the existing Position class with enhanced versions
init 5 python:
    def calculate_position_requirements(self, person, ignore_taboo = False, only_known_opinions = False):
        position_taboo = self.associated_taboo
        if ignore_taboo:
            position_taboo = None

        final_slut_requirement = self.slut_requirement
        final_slut_cap = self.slut_cap
        if self.skill_tag == "Anal" and person.has_family_taboo():
            final_slut_requirement -= 5 #It's easier to convince a family member to have anal sex, since it's not "real" incest or something.
            final_slut_cap -= 5
        elif self.skill_tag == "Vaginal" and person.has_family_taboo():
            final_slut_requirement += 10 #It's harder to convince a family member to have vaginal sex
            final_slut_cap += 10

        if self.opinion_tags:
            for opinion_tag in self.opinion_tags:
                final_slut_cap -= (person.get_known_opinion_score(opinion_tag) if only_known_opinions else person.get_opinion_score(opinion_tag)) * 5
                final_slut_requirement -= (person.get_known_opinion_score(opinion_tag) if only_known_opinions else person.get_opinion_score(opinion_tag)) * 5
        if person.has_taboo(position_taboo):
            final_slut_requirement += 10    # when she has a taboo increase slut requirement
            final_slut_cap += 10

        return final_slut_requirement, final_slut_cap

    Position.calculate_position_requirements = calculate_position_requirements

    # include a visual indication
    def build_position_willingness_string_enhanced(self, person, ignore_taboo = False): #NOTE: Returns a list instead of string. If you want it to be a single string then do "".join(position.build_position_willingness_string(person))
    #Generates a list of strings for this position that includes a tooltip and coloured willingness for the person given.

        willingness_string = ""
        tooltip_string = ""

        girl_expected_arousal = str(__builtin__.int(self.girl_arousal * (1 + 0.1 * mc.sex_skills[self.skill_tag]))) #Estimate what they'll gain based on both of your skills to make the predictions as accurate as possible.
        guy_expected_arousal = str(__builtin__.int(self.guy_arousal * (1 + 0.1 * person.sex_skills[self.skill_tag])))

        energy_string = "   {color=#A3A3FF}" + str(self.guy_energy) + "{/color}/{color=#FF6EC7}" + str(self.girl_energy) + "{/color} {image=energy_token_small}"
        arousal_string =  ", {color=#A3A3FF}" + guy_expected_arousal + "{/color}/{color=#FF6EC7}" + girl_expected_arousal + "{/color} {image=arousal_token_small}"

        disable = False
        position_taboo = self.associated_taboo

        if ignore_taboo:
            position_taboo = None

        final_slut_requirement, final_slut_cap = self.calculate_position_requirements(person, ignore_taboo, only_known_opinions = True)

        taboo_break_string = ""
        if person.has_taboo(position_taboo):
            taboo_break_string = " {image=taboo_break} "

        opinion_score = 0
        if self.opinion_tags:
            for opinion_tag in self.opinion_tags:
                opinion_score += person.get_known_opinion_score(opinion_tag)

        #NOTE: Removed the (tooltip) and (disabled) tags as they aren't needed in the screen which is their only use case at the moment, but consider adding those back in if being used in the renpy.display_menu
        if person.effective_sluttiness(position_taboo) > final_slut_cap:
            if opinion_score < 1 and person.arousal > final_slut_cap:
                willingness_string = "{color=#6b6b6b}Boring{/color}" #No sluttiness gain AND half arousal gain
                tooltip_string = " (tooltip) This position is too boring to interest her when she is this horny. No sluttiness increase and her arousal gain is halved."
            else:
                willingness_string = "{color=#A3A3FF}Comfortable{/color}" #No sluttiness
                tooltip_string = " (tooltip) This position is too tame for her tastes. No sluttiness increase, but it may still be a good way to get warmed up and ready for other positions."
        elif person.effective_sluttiness(position_taboo) >= final_slut_requirement:
            willingness_string = "{color=#3DFF3D}Exciting{/color}" #Normal sluttiness gain
            tooltip_string = " (tooltip) This position pushes the boundary of what she is comfortable with. Increases temporary sluttiness, which may become permanent over time or with serum application."
        elif person.effective_sluttiness(position_taboo) + person.obedience-100 >= final_slut_requirement:
            willingness_string = "{color=#FFFF3D}Likely Willing if Commanded{/color}"
            tooltip_string = " (tooltip) This position is beyond what she would normally consider. She is obedient enough to do it if she is commanded, at the cost of some happiness."
        else:
            willingness_string = "{color=#FF3D3D}Likely Too Slutty{/color}"
            tooltip_string = " (tooltip) This position is so far beyond what she considers appropriate that she would never dream of it."

        if person.has_taboo(position_taboo):
            tooltip_string +=" (tooltip) \nSuccessfully selecting this position will break a taboo, making it easier to convince " + (person.title if person.title else "her") + " to do it and similar acts in the future."

        if not self.check_clothing(person):
            disable = True
            willingness_string += "\nObstructed by clothing"
        elif mc.recently_orgasmed and self.requires_hard:
            disable = True
            willingness_string += "\nRecently orgasmed"
        elif mc.energy < self.guy_energy and person.energy < self.girl_energy:
            disable = True
            willingness_string += "\nYou're both too tired"
        elif mc.energy < self.guy_energy:
            disable = True
            willingness_string += "\nYou're too tired"
        elif person.energy < self.girl_energy:
            disable = True
            willingness_string += "\nShe's too tired"

        change_amount = 0
        if self.opinion_tags:
            for opinion_tag in self.opinion_tags:
                opinion_topic = person.get_opinion_topic(opinion_tag)
                if opinion_topic:
                    # renpy.say(None, person.name + ": " + opinion_tag + " => " + str(person.get_opinion_score(opinion_tag)))
                    if opinion_topic[1]: # only show info when opinion is known
                        change_amount += person.get_opinion_score(opinion_tag) * 3 #Add a bonus or penalty if she likes or dislikes the position.

        position_opinion = ""
        if change_amount > 0:
            position_opinion = " {image=thumbs_up}"
        elif change_amount < 0:
            position_opinion = " {image=thumbs_down}"

        if disable:
            return taboo_break_string + self.name + position_opinion + "\n{size=12}" + willingness_string + "{/size}" + " (disabled)" #Don't show the arousal and energy string if it's disabled to prevent overrun
        else:
            return taboo_break_string + self.name + position_opinion + "\n{size=12}" + willingness_string + energy_string + arousal_string + "{/size}" + tooltip_string

    Position.build_position_willingness_string = build_position_willingness_string_enhanced

    def get_position_last_scene(self):
        if not hasattr(self, "_last_scene"):
            self._last_scene = None
        return self._last_scene

    def set_position_last_scene(self, value):
        self._last_scene = value

    # add follow_mc attribute to person class (without sub-classing)
    Position.last_scene = property(get_position_last_scene, set_position_last_scene, None, "Track the last used scene for this position.")

    # choose random next scene (but don't repeat last scene if possible)
    def call_scene_enhanced(self, the_person, the_location, the_object):
        choice_list = [x for x in self.scenes if not x == self.last_scene]
        new_scene = get_random_from_list(choice_list) if choice_list else get_random_from_list(self.scenes)
        self.last_scene = new_scene
        renpy.call(new_scene, the_person, the_location, the_object)

    Position.call_scene = call_scene_enhanced

    # try different types of taboo break, the final choice is the break for the actual position broken
    # added an extra check to make sure the label exists, if not the taboo is broken without dialog
    def call_transition_taboo_break(self, new_position, person, the_location, the_object):
        def get_position_name(position):
            return position.name.lower().replace(" ", "_")

        if not new_position is None:
            transition_scene = "transition_" + get_position_name(self) + "_to_" + get_position_name(new_position) + "_taboo_break_label"
            #renpy.say(None, "Custom taboo break function is: " + transition_scene)
            if renpy.has_label(transition_scene):
                #renpy.say(None, "Calling custom taboo break: " + transition_scene)
                renpy.call(transition_scene, person, the_location, the_object)

            #renpy.say(None, "Default taboo break function: " + new_position.taboo_break_description)
            if renpy.has_label(new_position.taboo_break_description):
                #renpy.say(None, "Calling default taboo break: " + new_position.taboo_break_description)
                renpy.call(new_position.taboo_break_description, person, the_location, the_object)

            transition_scene = new_position.transition_default
            for position_tuple in self.transitions:
                if position_tuple[0] == new_position: ##Does the position match the one we are looking for?
                    transition_scene = position_tuple[1] ##If so, set it's label as the one we are going to change to.

            #renpy.say(None, "Default transition scene is: " + transition_scene)
            if renpy.has_label(transition_scene):
                #renpy.say(None, "Calling default transition scene: " + transition_scene)
                renpy.call(transition_scene, person, the_location, the_object)

        else: # we are calling from the new position (we don't have an old position to start from)
            #renpy.say(None, "Default taboo break function: " + self.taboo_break_description)
            if renpy.has_label(self.taboo_break_description):
                #renpy.say(None, "Calling default taboo break: " + self.taboo_break_description)
                renpy.call(self.taboo_break_description, person, the_location, the_object)

            transition_scene = self.transition_default
            if renpy.has_label(transition_scene):
                #renpy.say(None, "Calling default transition: " + transition_scene)
                renpy.call(transition_scene, person, the_location, the_object)
        return

    Position.call_transition_taboo_break = call_transition_taboo_break

    def get_girl_outro(self):
        if not hasattr(self, "_girl_outro"):
            self._girl_outro = None
        return self._girl_outro

    def set_girl_outro(self, value):
        self._girl_outro = value

    def del_girl_outro(self):
        del self._girl_outro

    # add girl_outro attribute to position class (without sub-classing)
    Position.girl_outro = property(get_girl_outro, set_girl_outro, del_girl_outro, "Girl in charge label")

    def call_outro_enhanced(self, the_person, the_location, the_object):
        if self.girl_outro:  #Rely on girl outro tocall default outro if appropriate
            renpy.call(self.girl_outro,the_person, the_location, the_object)
        else:
            self.call_default_outro(the_person, the_location, the_object)

    def call_default_outro(self, the_person, the_location, the_object):
        renpy.call(self.outro,the_person, the_location, the_object)

    Position.call_outro = call_outro_enhanced
    Position.call_default_outro = call_default_outro

    #Simultaneous orgasm code

    def get_double_orgasm(self):
        if not hasattr(self, "_double_orgasm"):
            self._double_orgasm = None
        return self._double_orgasm

    def set_double_orgasm(self, value):
        self._double_orgasm = value

    def del_double_orgasm(self):
        del self._double_orgasm

    # add double_orgasm attribute to position class (without sub-classing)
    Position.double_orgasm = property(get_double_orgasm, set_double_orgasm, del_double_orgasm, "Double orgasm label")

    def call_orgasm_enhanced(self, the_person, the_location, the_object):
        if self.double_orgasm and mc.arousal >= mc.max_arousal:
            renpy.call(self.double_orgasm, the_person, the_location, the_object)
        else:
            renpy.call(self.orgasm_description, the_person, the_location, the_object)
        return

    Position.call_orgasm = call_orgasm_enhanced

    def post_double_orgasm(person):
        mc.reset_arousal()
        mc.recently_orgasmed = True
        person.change_obedience(5)
        if "report_log" in globals():
            report_log["guy orgasms"] = report_log.get("guy orgasms", 0) + 1
        return
