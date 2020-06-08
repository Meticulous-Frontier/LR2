#COPY paste this to create a new quest.
#At the beginning, give a description of how the quest should play, etc.
#Now describe if there are any long term benefits

#Flags
#Use numbers to describe quest flags
#1 Init
#11 Any flag ending in 1 is after a story portion.
#19 Any flag ending in a 9 is a bad end
#101 Any flag >100 is a good end

#TODO don't forget to add the quest to the list of quests in Side_quests_main.rpy

label quest_QUEST_NAME_init_label(): #Use this function to set quest specific variables.
    pass
    return

### The next three functions define the quest progress tracker, init requirements, and how we clean up after quest is done.
init 1 python:
    def quest_QUEST_NAME_tracker():
        pass
        return

    def quest_QUEST_NAME_start_requirement():
        pass
        return False

    def quest_QUEST_NAME_cleanup():
        pass
        return

###Declare any requirement functions now
    def quest_QUEST_NAME_intro_requirement(the_person):
        pass
        return True

###Functions unique to the quest
    def quest_QUEST_NAME_person_function_thing(the_person):
        pass
        return True

###Declare quest actions###


#Quest Labels. This is the story you want to tell!
