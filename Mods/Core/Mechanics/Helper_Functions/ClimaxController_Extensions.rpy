init -1 python:
    def manual_clarity_release(self, climax_type = "body", the_person = None):

        multiplier = self.get_climax_multiplier(climax_type)
        if the_person:
            mc.convert_locked_clarity(multiplier, with_novelty = the_person.novelty)
            the_person.change_novelty(-2)
        else:
            mc.convert_locked_clarity(multiplier, with_novelty = mc.masturbation_novelty)
        return

    ClimaxController.manual_clarity_release = manual_clarity_release
