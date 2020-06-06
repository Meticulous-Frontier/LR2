#Side quests are an attempt to inject more personality into the personality free worker drones of MC.business
#Generally, we want side quests to last approximately one week of in game time and to be able to be completed with whatever tools MC has available
#The quest should generally have some sort of lasting impact on the character involved
#Quests should be assigned randomly. Only one quest should be active at a time, so a quest should have a tracker for when it is active/inactive/complete
#Care should be taken so that quests are not given out too often. Resolution to a give quest should be obvious from dialogue
#RNG should be a part of quest assignment to make every play through unique. Not every side quest will be available in every game.
init python: #For now default init. May change later if we know better.
    SIDE_QUEST_INITIAL_CHANCE = 1
    SIDE_QUEST_DAILY_CHANCE_INCREASE = 1
    class Side_Quest(renpy.store.object):
        def __init__(self, quest_name, quest_init_label, quest_tracker, start_requirement, quest_cleanup):
            #TODO
            self.quest_name = quest_name #Not sure if we even need this but its here for now.
            self.quest_init_label = quest_init_label #Run this function if this quest is selected to begin.
            self.quest_tracker = quest_tracker #Run this function evey turn to update quest status. Needs to assign appropriate events, crisis, actions, etc. and remove them as necessary.
            self.start_requirement = start_requirement #This function determines if the side quest is available to be run.
            self.quest_cleanup = quest_cleanup  #Function that will be run when the quest goes inactive, to cleanup any appropriate leftover variables, crisis, actions, etc.
            self.quest_flag = 0 #an int used to describe the current state of the quest. Comments in new quest file should explain different flag params
            #Generally, any flag <100 that ends in 9 is a bad end. Any flag > 100 is good end.
            #flag increments in large steps in increments of 10,small in increments of 1.
            self.quest_event_dict = {}  #A dict for storing variables related to the quest.
            self.quest_active = False #bool for if the quest is currently active.
            self.quest_complete = False #bool, set to true when the quest is finished so it doesn't get triggered again during this play through.

            self.quest_start_day = -1 #Just in case quest is timed, make it easy to get start date.

        def set_quest_flag(self, flag):
            self.quest_flag = flag
            return

        def get_quest_flag(self):
            return self.quest_flag

        def quest_init(self):
            renpy.call(self.quest_init_label)

    class Quest_Tracker(renpy.store.object):
        def __init__(self):
            self.quest_list = []
            self.active_quest = None
            self.unavailable_persons = [] #List of people that are unable to used for quest purposes. Girls get added to this as quests progress, so we don't give multiple quests to same girl
            self.quest_chance = SIDE_QUEST_INITIAL_CHANCE


        def run_day(self): #AT the end of each day.
            if self.active_quest == None: #There is no active quest, so have a chance at beginning a new quest.
                ran_num = renpy.random.randint(0,100)
                if ran_num < self.quest_chance:  #Currently a 4% chance of beginning a new quest everyday. SHOULD average out to
                    if self.start_new_quest():
                        pass
                    else:
                        self.quest_chance = SIDE_QUEST_INITIAL_CHANCE  #No quest started because none avail. Reset quest chance.
                else:
                    self.quest_chance += SIDE_QUEST_DAILY_CHANCE_INCREASE #EVery day add an additional chance of a quest. Should elminate 20+ day quest droughts.
            else:
                if self.active_quest.quest_complete == True: #Quest is done! clear the active and reset daily quest chances.
                    self.active_quest.quest_active = False
                    self.active_quest.quest_cleanup()
                    self.active_quest = None
                    self.quest_chance = SIDE_QUEST_INITIAL_CHANCE

        def run_turn(self):
            if self.active_quest != None:
                self.active_quest.quest_tracker()
            return

        def start_new_quest(self):
            able_quest_list = []
            for quest in self.quest_list:
                if not quest.quest_complete:
                    if quest.start_requirement():
                        able_quest_list.append(quest)
            if len(able_quest_list) == 0: #No applicable quests available. Reset quest chance.
                return False
            else:
                self.active_quest = get_random_from_list(able_quest_list)
                self.active_quest.quest_init()
                self.quest_active = True
                self.quest_start_day = day
            return True

        def get_current_quest(self):
            return self.active_quest

        def set_quest_flag(flag):
            self.active_quest.set_quest_flag(flag)
            return

        def add_new_quest(self, new_quest):  #Adds new quest, but only if it is unique. Checks to see if same name quest already exists.
            for quest in self.quest_list:
                if new_quest.quest_name == quest.quest_name:
                    return False
            self.quest_list.append(new_quest)

        #DEBUG functions

        def debug_text_dump(self):  #Use this command in the console to get a dump of quest tracker status.
            cur_quest = self.get_current_quest()
            if self.get_current_quest() == None:
                renpy.say("","There is currently no active quest.")
            else:
                renpy.say("","The current active quest is [cur_quest.quest_name].")
            renpy.say("","The current list of quests is:")
            for quest in self.quest_list:
                renpy.say("","[quest.quest_name].")
            return


        def attempt_force_quest(self, quest_name = None, override_active = False):  #Use this command in the console to attempt to for a new quest. optional param to force a specific quest for debug purpuses.
            if self.active_quest == None or override_action:
                if quest_name == None:
                    return self.start_new_quest()

                else:
                    for quest in self.quest_list:
                        if quest_name == quest.quest_name:
                            self.active_quest = quest
                            self.active_quest.quest_complete = False
                            self.active_quest.quest_init()
                            self.quest_active = True
                            self.quest_start_day = day
                            return True
            return "Unable to force quest"

    def Quest_tracker_init():
        global quest_director
        quest_director = Quest_Tracker()

        global quest_production_line
        quest_production_line = Side_Quest(quest_name = "Chemists's Baby Girl",
        quest_init_label = "quest_production_line_init_label",
        quest_tracker = quest_production_line_tracker,
        start_requirement = quest_production_line_start_requirement,
        quest_cleanup = quest_production_line_cleanup)

        global quest_cure_discovery
        quest_cure_discovery = Side_Quest(quest_name = "Medical Breakthrough",
        quest_init_label = "quest_cure_discovery_init_label",
        quest_tracker = quest_cure_discovery_tracker,
        start_requirement = quest_cure_discovery_start_requirement,
        quest_cleanup = quest_cure_discovery_cleanup)

        quest_director.add_new_quest(quest_production_line)
        quest_director.add_new_quest(quest_cure_discovery)
        quest_director.unavailable_persons = [sarah, mom, lily, starbuck, nora, cousin, aunt, salon_manager]

        return
