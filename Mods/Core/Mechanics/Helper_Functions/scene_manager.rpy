init -2 python:

    def hide_ui(): # Hides the UI
        renpy.scene("Active")
        renpy.hide_screen("main_ui")
        renpy.hide_screen("phone_hud_ui")
        renpy.hide_screen("business_ui")
        renpy.hide_screen("goal_hud_ui")

    def show_ui(): # Show the UI
        renpy.scene("Active")
        renpy.show_screen("main_ui")
        renpy.show_screen("phone_hud_ui")
        renpy.show_screen("business_ui")
        renpy.show_screen("goal_hud_ui")

    class Scene():
        def __init__(self):
            self.actors = []

        def add_actor(self, person, position = None, emotion = None, special_modifier = None, character_placement = None):
            self.actors.append(Actor(person, position, emotion, special_modifier, character_placement))
            self.draw_scene()

        # Removes all actors from the scene
        def clear_scene(self):
            people_in_scene = [actor.person for actor in self.actors]
            for person in people_in_scene:
                self.remove_actor(person)

        def update_actor(self, person, position = None, emotion = None, special_modifier = None, character_placement = None):
            actor = find_in_list(lambda x: x.person is person, self.actors)
            if actor is None:
                return
            if not position is None:
                actor.position = position
            if not emotion is None:
                actor.emotion = emotion
            if not special_modifier is None:
                actor.special_modifier = special_modifier
            if not character_placement is None:
                actor.character_placement = character_placement
            self.draw_scene()

        def strip_actor_outfit_to_max_sluttiness(self, person, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, narrator_messages = None, temp_sluttiness_boost = 0):
            actor = find_in_list(lambda x: x.person is person, self.actors)
            if not actor is None:
                #mc.log_event("Strip " + actor.person.title, "gray_float_text")
                actor.person.strip_outfit_to_max_sluttiness(top_layer_first = top_layer_first, exclude_upper = exclude_upper, exclude_lower = exclude_lower, exclude_feet = exclude_feet, narrator_messages = narrator_messages, character_placement = actor.character_placement, temp_sluttiness_boost = temp_sluttiness_boost,  position = actor.position, emotion = actor.emotion, scene_manager = self)

        def draw_animated_removal(self, person, the_clothing): #A special version of draw_person, removes the_clothing and animates it floating away. Otherwise draws as normal.
            actor = find_in_list(lambda x: x.person is person, self.actors)
            if not actor is None:
                #mc.log_event("Remove clothing " + actor.person.title, "gray_float_text")
                actor.person.draw_animated_removal(the_clothing, position = actor.position, emotion = actor.emotion, special_modifier = actor.special_modifier, character_placement = actor.character_placement, scene_manager = self)

        def get_free_position_tuple(self):
            if find_in_list(lambda x: x.character_placement == character_right, self.actors) is None and find_in_list(lambda x: x.character_placement == character_right_flipped, self.actors) is None:
                return [character_right, character_right_flipped]
            if find_in_list(lambda x: x.character_placement == character_center, self.actors) is None and find_in_list(lambda x: x.character_placement == character_center_flipped, self.actors) is None:
                return [character_center, character_center_flipped]
            if find_in_list(lambda x: x.character_placement == character_left, self.actors) is None and find_in_list(lambda x: x.character_placement == character_left_flipped, self.actors) is None:
                return [character_left, character_left_flipped]
            return None

        # removes specific actor from scene
        def remove_actor(self, person, reset_actor = True):
            actor_to_remove = find_in_list(lambda x: x.person is person, self.actors)
            if not actor_to_remove is None:
                if reset_actor:
                    # reset actor clothing and arousal
                    actor_to_remove.person.review_outfit(show_review_message = False)
                    actor_to_remove.person.reset_arousal()
                self.actors.remove(actor_to_remove)
                self.draw_scene()

        def draw_info_ui(self):
            renpy.scene("Active")
            if len(self.actors) > 1:
                renpy.show_screen("multi_person_info_ui", self.actors)
            elif len(self.actors) == 1:
                renpy.show_screen("person_info_ui", self.actors[0].person)

        def draw_scene(self):
            self.draw_info_ui()
            for actor in self.actors:
                actor.draw_actor()

        # helper function for strip and animated removal functions
        def draw_scene_without(self, person):
            self.draw_info_ui()
            actor_missing = find_in_list(lambda x: x.person is person, self.actors)
            for actor in self.actors:
                if not actor is actor_missing:
                    actor.draw_actor()

    class Actor():
        def __init__(self, person, position = None, emotion = None, special_modifier = None, character_placement = None):
            self.person = person
            self.position = position
            self.emotion = emotion
            self.special_modifier = special_modifier
            self.character_placement = character_placement
            self.sort_order = 2

            if position is None:
                self.position = person.idle_pose

            if emotion is None:
                self.emotion = person.get_emotion()

            if character_placement is None:
                self.character_placement = character_right

            if character_placement == character_center or character_placement == character_center_flipped:
                self.sort_order = 1
            if character_placement == character_left or character_placement == character_left_flipped:
                self.sort_order = 0

        def draw_actor(self):
            self.person.draw_person(position = self.position, emotion = self.emotion, special_modifier = self.special_modifier, character_placement = self.character_placement, from_scene = True)


##########################################
# Transformation for character_placement #
##########################################
init -1:
    transform character_right_flipped():
        yalign 1.0
        yanchor 1.0
        xalign 1.0
        xanchor 1.0
        xzoom -1

    transform character_center():
        yalign 1.0
        yanchor 1.0
        xalign 0.75
        xanchor 1.0

    transform character_center_flipped():
        yalign 1.0
        yanchor 1.0
        xalign 0.75
        xanchor 1.0
        xzoom -1

    transform character_left():
        yalign 1.0
        yanchor 1.0
        xalign 0.5
        xanchor 1.0

    transform character_left_flipped():
        yalign 1.0
        yanchor 1.0
        xalign 0.5
        xanchor 1.0
        xzoom -1
