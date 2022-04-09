#Requirement Functions
init 1 python:
    def cum_fetish_myra_intro_requirement():
        pass
        return False

    def exhibition_fetish_myra_intro_requirement():
        pass
        return False

    def breeding_fetish_myra_intro_requirement():
        pass
        return False

    def anal_fetish_myra_intro_requirement():
        pass
        return False


#Actions
init 2 python:
    cum_fetish_myra_intro = Fetish_Action("Myra Cum Fetish Intro", cum_fetish_myra_intro_requirement, "cum_fetish_myra_intro_label", fetish_type = "cum")
    exhibition_fetish_myra_intro = Fetish_Action("Myra Exhibitionism Fetish Intro", exhibition_fetish_myra_intro_requirement, "exhibition_fetish_myra_intro_label", fetish_type = "exhibition")
    breeding_fetish_myra_intro = Fetish_Action("Myra Breeding Fetish Intro", breeding_fetish_myra_intro_requirement, "breeding_fetish_myra_intro_label", fetish_type = "breeding")
    anal_fetish_myra_intro = Fetish_Action("Myra Anal Fetish Intro", anal_fetish_myra_intro_requirement, "anal_fetish_myra_intro_label", fetish_type = "anal")

label cum_fetish_myra_intro_label():
    $ the_person = myra

    $ add_cum_fetish(the_person)
    return

label exhibition_fetish_myra_intro_label():
    $ the_person = myra
    return


label breeding_fetish_myra_intro_label():
    $ the_person = myra

    $ add_breeding_fetish(the_person)
    return

label anal_fetish_myra_intro_label():
    $ the_person = myra

    $ add_anal_fetish(the_person)
    return
