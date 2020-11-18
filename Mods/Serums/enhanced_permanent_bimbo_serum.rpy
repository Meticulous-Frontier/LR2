init python:
    permanent_bimbo.exclude_tags = ["Personality"]

    def enhanced_permanent_bimbo_on_apply(the_person, add_to_log):
        if the_person.personality != bimbo_personality:
            the_person.original_personality = the_person.personality
        permanent_bimbo_on_apply(the_person, add_to_log)
        return

    permanent_bimbo.on_apply = enhanced_permanent_bimbo_on_apply
