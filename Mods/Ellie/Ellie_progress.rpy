init 10 python:
    def ellie_story_love_list():
        love_story_list = []
        if not ellie_has_been_fingered():
            love_story_list.append("Advance her sluttiness story to continue this story.")
            return love_story_list
        if not ellie_has_given_handjob():
            if ellie.love < 20:
                love_story_list.append("Increase [ellie.title]'s love to continue this story.")
            else:
                love_story.append("[ellie.title] may surprise you at work soon.")
            return love_story_list
        else:
            love_story_list.append("[ellie.title] returned the sexual favor with her first handjob!")
        love_story_list.append("There is nothing more in this story line at this time.")
        return love_story_list

    def ellie_story_lust_list():
        lust_story_list = []
        if not ellie_has_been_fingered():
            if ellie.sluttiness < 20:
                lust_story_list.append("Trying increasing her sluttiness to continue this story.")
            else:
                lust_story_list.append("Try working while she is working on a nanobot proram to continue this story.")
            return lust_story_list
        else:
            lust_story_list.append("Gave [ellie.title] her first orgasm with your fingers in her office!")
        if not ellie_has_given_handjob():   #Requires love story progress
            lust_story_list.append("Try progressing [ellie.title]'s love story to coninute this story.")
            return lust_story_list
        elif not ellie_has_given_blowjob(): #40 sluttiness event
            if ellie.sluttiness < 40:
                lust_story_list.append("Trying increasing her sluttiness to continue this story.")
            elif not get_random_employees(1, exclude_list = [ellie], slut_required = 50):
                lust_story_list.append("[ellie.title] doesn't know anyone we can confide her desires in. Raise another employees sluttiness to atleast 50.")
            else:
                lust_story_list.append("You may overhear a conversation [ellie.title] is having at work soon...")
            return lust_story_list
        else:
            lust_story_list.append("[ellie.title] gave you her first blowjob after you overheard her asking a coworker about oral sex!")

        lust_story_list.append("There is nothing more in this story line at this time.")

        return lust_story_list

    def ellie_story_teamup_list():
        return [[" ", " "]]

    def ellie_story_other_list():
        other_info_list = ["[ellie.title] is thankful you hired her, despite blackmailing you."]
        if ellie_is_a_squirter():
            other_info_list.append("[ellie.title] has extremely wet orgasms!")
        # other_info_list.append("[ellie.title] is not yet willing to go all the way with you. Try advancing her story.")
        return other_info_list
