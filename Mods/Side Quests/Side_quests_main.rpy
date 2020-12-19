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
            self.quest_tracker = quest_tracker #Run this function every turn to update quest status. Needs to assign appropriate events, crisis, actions, etc. and remove them as necessary.
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
            self.quest_tracker()
            return

        def get_quest_flag(self):
            return self.quest_flag

        def quest_init(self):
            renpy.call(self.quest_init_label)

        def quest_completed(self):
            self.quest_complete = True
            self.quest_cleanup()
            return

        #################################################
        # Custom Compare Functions For Side_Quest Class #
        #################################################
        def __cmp__(self, other):
            if isinstance(self, other.__class__):
                if self.quest_name == other.quest_name:
                    return 0

            if self.__hash__() < other.__hash__():
                return -1
            else:
                return 1

        # add side_quest hash function
        def __hash__(self):
            return hash(self.quest_name)

        def __eq__(self, other):
            if isinstance(self, other.__class__):
                return self.quest_name == other.quest_name
            return False

        def __ne__(self, other):
            if isinstance(self, other.__class__):
                return self.quest_name != other.quest_name
            return True


    class Quest_Tracker(renpy.store.object):
        def __init__(self):
            self.quest_list = []
            self.active_quest = None
            self.unavailable_person_identifiers = [] #List of people that are unable to used for quest purposes. Girls get added to this as quests progress, so we don't give multiple quests to same girl
            self.quest_chance = SIDE_QUEST_INITIAL_CHANCE

        def run_day(self): #AT the end of each day.
            if not self.active_quest: #There is no active quest, so have a chance at beginning a new quest.
                ran_num = renpy.random.randint(0,100)
                if ran_num < self.quest_chance:  #Currently a 4% chance of beginning a new quest everyday. SHOULD average out to
                    if not self.start_new_quest():
                        self.quest_chance = SIDE_QUEST_INITIAL_CHANCE  #No quest started because none avail. Reset quest chance.
                else:
                    self.quest_chance += SIDE_QUEST_DAILY_CHANCE_INCREASE #EVery day add an additional chance of a quest. Should eliminate 20+ day quest droughts.
            else:
                if self.active_quest.quest_complete == True: #Quest is done! clear the active and reset daily quest chances.
                    self.active_quest.quest_active = False
                    self.active_quest.quest_cleanup()
                    self.active_quest = None
                    self.quest_chance = SIDE_QUEST_INITIAL_CHANCE

        def run_turn(self):
            if self.active_quest:
                self.active_quest.quest_tracker()
            return

        def start_new_quest(self):
            able_quest_list = []
            for quest in self.quest_list:
                if not quest.quest_complete:
                    if quest.start_requirement():
                        able_quest_list.append(quest)

            self.active_quest = get_random_from_list(able_quest_list)
            if not self.active_quest: #No applicable quests available. Reset quest chance.
                return False

            self.active_quest.quest_init()
            self.quest_active = True
            self.quest_start_day = day
            return True

        def set_quest_flag(flag):
            if self.active_quest:
                self.active_quest.set_quest_flag(flag)
            return

        def add_new_quest(self, new_quest):  #Adds new quest, but only if it is unique. Checks to see if same name quest already exists.
            if not new_quest in self.quest_list:
                self.quest_list.append(new_quest)
                return True
            return False

        def active_quest_name(self):
            if self.active_quest:
                return self.active_quest.quest_name
            return ""

        def add_unavailable_person(self, person):
            if not person.identifier in self.unavailable_person_identifiers:
                self.unavailable_person_identifiers.append(person.identifier)

        def unavailable_people(self):
            result = []
            for person in known_people_in_the_game([mc]):
                if person.identifier in self.unavailable_person_identifiers:
                    result.append(person)
            return result

        def is_person_blocked(self, person):
            return person.identifier in self.unavailable_person_identifiers


        #DEBUG functions

        def debug_text_dump(self):  #Use this command in the console to get a dump of quest tracker status.
            if not self.active_quest:
                renpy.say("","There is currently no active quest.")
            else:
                renpy.say("","The current active quest: " + self.active_quest.quest_name)

            renpy.say("","The current list of quests is:")
            for quest in self.quest_list:
                renpy.say("", quest.quest_name)
            return

        def attempt_force_quest(self, quest_name = None, override_active = False):  #Use this command in the console to attempt to for a new quest. optional param to force a specific quest for debug purpuses.
            if self.active_quest == None or override_active:
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

        def purge_active_quest(self):  #Use this to attempt to clean out an active quest in case it gets buggy during reload
            if self.active_quest:
                self.active_quest.set_quest_flag(0)
                self.active_quest.quest_cleanup()
                self.active_quest = false

    def Quest_tracker_init():
        global quest_director
        quest_director = Quest_Tracker()

        Quest_tracker_update_quest_list()
        return

    def Quest_tracker_update_quest_list():
        for person in unique_character_list:
            quest_director.add_unavailable_person(person)

        quest_production_line = Side_Quest(quest_name = "Chemist's Baby Girl",
            quest_init_label = "quest_production_line_init_label",
            quest_tracker = quest_production_line_tracker,
            start_requirement = quest_production_line_start_requirement,
            quest_cleanup = quest_production_line_cleanup)

        if not quest_production_line in quest_director.quest_list:
            quest_director.add_new_quest(quest_production_line)

        quest_cure_discovery = Side_Quest(quest_name = "Medical Breakthrough",
            quest_init_label = "quest_cure_discovery_init_label",
            quest_tracker = quest_cure_discovery_tracker,
            start_requirement = quest_cure_discovery_start_requirement,
            quest_cleanup = quest_cure_discovery_cleanup)

        if not quest_cure_discovery in quest_director.quest_list:
            quest_director.add_new_quest(quest_cure_discovery)

        quest_cuckold_employee = Side_Quest(quest_name = "Cuckold Employee",
            quest_init_label = "quest_cuckold_employee_init_label",
            quest_tracker = quest_cuckold_employee_tracker,
            start_requirement = quest_cuckold_employee_start_requirement,
            quest_cleanup = quest_cuckold_employee_cleanup)

        if not quest_cuckold_employee in quest_director.quest_list:
            quest_director.add_new_quest(quest_cuckold_employee)

        quest_essential_oils = Side_Quest(quest_name = "Essential Oils",
            quest_init_label = "quest_essential_oils_init_label",
            quest_tracker = quest_essential_oils_tracker,
            start_requirement = quest_essential_oils_start_requirement,
            quest_cleanup = quest_essential_oils_cleanup)

        if not quest_essential_oils in quest_director.quest_list:
            quest_director.add_new_quest(quest_essential_oils)

        quest_arousal_serum = Side_Quest(quest_name = "Arousal Serum",
            quest_init_label = "quest_arousal_serum_init_label",
            quest_tracker = quest_arousal_serum_tracker,
            start_requirement = quest_arousal_serum_start_requirement,
            quest_cleanup = quest_arousal_serum_cleanup)

        if not quest_arousal_serum in quest_director.quest_list:
            quest_director.add_new_quest(quest_arousal_serum)
        return

    def Quest_tracker_update():
        Quest_tracker_update_quest_list()

        # update existing quests to simplify debugging (only tracker and cleanup)
        quest_production_line.quest_tracker = quest_production_line_tracker
        quest_production_line.quest_cleanup = quest_production_line_cleanup

        quest_cure_discovery.quest_tracker = quest_cure_discovery_tracker
        quest_cure_discovery.quest_cleanup = quest_cure_discovery_cleanup

        quest_cuckold_employee.quest_tracker = quest_cuckold_employee_tracker
        quest_cuckold_employee.quest_cleanup = quest_cuckold_employee_cleanup

        quest_essential_oils.quest_tracker = quest_essential_oils_tracker
        quest_essential_oils.quest_cleanup = quest_essential_oils_cleanup
        return
