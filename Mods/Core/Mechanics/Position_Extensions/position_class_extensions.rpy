init -1:
    python:
        def build_position_willingness_string_enhanced(self, the_person): #Generates a string for this position that includes a tooltip and coloured willingness for the person given.
            willingness_string = ""
            tooltip_string = ""

            if the_person.effective_sluttiness() >= self.slut_cap:
                if the_person.arousal >= self.slut_cap:
                    willingness_string = "{color=#6b6b6b}Boring{/color}" #No sluttiness gain AND half arousal gain
                    tooltip_string = " (tooltip)This position is too boring to interest her when she is this horny. No sluttiness increase and her arousal gain is halved."
                else:
                    willingness_string = "{color=#3C3CFF}Comfortable{/color}" #No sluttiness
                    tooltip_string = " (tooltip)This position is too tame for her tastes. No sluttiness increase, but it may still be a good way to get warmed up and ready for other positions."
            elif the_person.effective_sluttiness() >= self.slut_requirement:
                willingness_string = "{color=#3DFF3D}Exciting{/color}" #Normal sluttiness gain
                tooltip_string = " (tooltip)This position pushes the boundary of what she is comfortable with. Increases temporary sluttiness, which may become permanent over time or with serum application."
            elif the_person.effective_sluttiness() + the_person.obedience-100 >= self.slut_requirement:
                willingness_string = "{color=#FFFF3D}Willing if Commanded{/color}"
                tooltip_string = " (tooltip)This position is beyond what she would normally consider. She is obedient enough to do it if she is commanded, at the cost of some happiness."
            else:
                willingness_string = "{color=#FF3D3D}Too Slutty{/color}"
                tooltip_string = " (tooltip)This position is so far beyond what she considers appropriate that she would never dream of it."

            if self.check_clothing(the_person):
                return self.name + "\n{size=22}" + willingness_string + "{/size}" + tooltip_string
            else:
                return self.name + "\n{size=22}" + willingness_string + "\nObstructed by Clothing{/size} (disabled)"

        Position.build_position_willingness_string = build_position_willingness_string_enhanced