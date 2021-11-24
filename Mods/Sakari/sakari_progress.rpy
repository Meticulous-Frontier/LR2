# Use this file to hold information relating to Sakari's story progress and hint system.

init 10 python:
    def sakari_story_love_list():
        love_story_list = []
        love_story_list.append("There is nothing more in this story line at this time.")
        return love_story_list

    def sakari_story_lust_list():
        lust_story_list = []

        lust_story_list.append("There is nothing more in this story line at this time.")

        return lust_story_list

    def sakari_story_teamup_list():
        return [[kaya, "Hmm, [kaya.title] is [sakari.title]'s daughter... surely nothing could happen there... right?'"]]

    def sakari_story_other_list():
        return["[sakari.title] has started working at the clothing store again. Look for her there in the morning."]
