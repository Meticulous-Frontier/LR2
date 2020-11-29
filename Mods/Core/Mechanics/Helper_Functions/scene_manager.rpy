init -2 python:

    def hide_ui(): # Hides the UI
        renpy.hide_screen("main_ui")
        renpy.hide_screen("phone_hud_ui")
        renpy.hide_screen("business_ui")
        renpy.hide_screen("goal_hud_ui")
        return

    def show_ui(): # Show the UI
        renpy.show_screen("main_ui")
        renpy.show_screen("phone_hud_ui")
        renpy.show_screen("business_ui")
        renpy.show_screen("goal_hud_ui")
        return

    class Scene(renpy.store.object):
        def __init__(self):
            self.actors = []

        def add_group(self, people, position = None, emotion = None, special_modifier = None, lighting = None, z_order = None):
            xoffset = 0.1
            for person in people:
                self.actors.append(Actor(person, position, emotion, special_modifier, lighting, character_center(xoffset), z_order))
                xoffset -= .1
            self.draw_scene()

        def add_actor(self, person, position = None, emotion = None, special_modifier = None, lighting = None, display_transform = None, z_order = None):
            self.actors.append(Actor(person, position, emotion, special_modifier, lighting, display_transform, z_order))
            self.draw_scene()

        # Removes all actors from the scene
        def clear_scene(self, reset_actor = True):
            people_in_scene = [actor.person for actor in self.actors]
            for person in people_in_scene:
                self.remove_actor(person, reset_actor = reset_actor)

        def update_actor(self, person, position = None, emotion = None, special_modifier = None, lighting = None, display_transform = None, z_order = None):
            actor = find_in_list(lambda x: x.person is person, self.actors)
            if actor is None:
                return
            if not position is None:
                actor.position = position
            if not emotion is None:
                actor.emotion = emotion
            if not special_modifier is None:
                actor.special_modifier = special_modifier
            if not lighting is None:
                actor.lighting = lighting
            if not display_transform is None:
                actor.display_transform = display_transform
            if not z_order is None:
                actor.z_order = z_order
            self.draw_scene()

        def strip_actor_outfit_to_max_sluttiness(self, person, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, narrator_messages = None, temp_sluttiness_boost = 0):
            actor = find_in_list(lambda x: x.person is person, self.actors)
            if not actor is None:
                #mc.log_event("Strip " + actor.person.title, "gray_float_text")
                return actor.person.strip_outfit_to_max_sluttiness(top_layer_first = top_layer_first, exclude_upper = exclude_upper, exclude_lower = exclude_lower, exclude_feet = exclude_feet, narrator_messages = narrator_messages, display_transform = actor.display_transform, lighting = actor.lighting, temp_sluttiness_boost = temp_sluttiness_boost, position = actor.position, emotion = actor.emotion, scene_manager = self)
            return False

        def strip_actor_outfit(self, person, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, delay = 1):
            actor = find_in_list(lambda x: x.person is person, self.actors)
            if not actor is None:
                actor.person.strip_outfit(top_layer_first = top_layer_first, exclude_upper = exclude_upper, exclude_lower = exclude_lower, exclude_feet = exclude_feet, display_transform = actor.display_transform, lighting = actor.lighting, position = actor.position, emotion = actor.emotion, delay = delay, scene_manager = self, wipe_scene = False)

        def strip_actor_strip_list(self, person, strip_list, lighting = None, half_off_instead = False):
            actor = find_in_list(lambda x: x.person is person, self.actors)
            if not actor is None:
                for item in strip_list:
                    actor.person.draw_animated_removal(item, position = actor.position, emotion = actor.emotion, special_modifier = actor.special_modifier, lighting = lighting, display_transform = actor.display_transform, scene_manager = self, half_off_instead = half_off_instead)

        def draw_animated_removal(self, person, the_clothing, lighting = None, half_off_instead = False): #A special version of draw_person, removes the_clothing and animates it floating away. Otherwise draws as normal.
            actor = find_in_list(lambda x: x.person is person, self.actors)
            if not actor is None:
                #mc.log_event("Remove clothing " + actor.person.title, "gray_float_text")
                actor.person.draw_animated_removal(the_clothing, position = actor.position, emotion = actor.emotion, special_modifier = actor.special_modifier, lighting = lighting, display_transform = actor.display_transform, scene_manager = self, half_off_instead = half_off_instead)

        def get_free_position_tuple(self):
            if find_in_list(lambda x: x.display_transform == character_right, self.actors) is None and find_in_list(lambda x: x.display_transform == character_right_flipped, self.actors) is None:
                return [character_right, character_right_flipped]
            if find_in_list(lambda x: x.display_transform == character_center, self.actors) is None and find_in_list(lambda x: x.display_transform == character_center_flipped, self.actors) is None:
                return [character_center, character_center_flipped]
            if find_in_list(lambda x: x.display_transform == character_left, self.actors) is None and find_in_list(lambda x: x.display_transform == character_left_flipped, self.actors) is None:
                return [character_left, character_left_flipped]
            return None

        # removes specific actor from scene
        def remove_actor(self, person, reset_actor = True):
            actor_to_remove = find_in_list(lambda x: x.person is person, self.actors)
            if not actor_to_remove is None:
                if reset_actor:
                    # reset actor clothing
                    actor_to_remove.person.apply_planned_outfit()
                self.actors.remove(actor_to_remove)
                self.draw_scene()

        def draw_info_ui(self):
            clear_scene()
            if __builtin__.len(self.actors) > 3:
                return  # we cannot display more info than 3

            if __builtin__.len(self.actors) > 1:
                renpy.show_screen("multi_person_info_ui", self.actors)
            elif __builtin__.len(self.actors) == 1:
                renpy.show_screen("person_info_ui", self.actors[0].person)

        def draw_scene(self):
            self.draw_info_ui()
            for actor in sorted(self.actors, key = lambda x: x.z_order):
                actor.draw_actor()

        # helper function for strip and animated removal functions
        def draw_scene_without(self, person):
            self.draw_info_ui()
            actor_missing = find_in_list(lambda x: x.person is person, self.actors)
            for actor in self.actors:
                if not actor is actor_missing:
                    actor.draw_actor()

    # z_order determines the order in which the actors are drawn, low number first, high number later
    class Actor(renpy.store.object):
        def __init__(self, person, position = None, emotion = None, special_modifier = None, lighting = None, display_transform = None, z_order = None):
            self.person = person
            self.position = position
            self.emotion = emotion
            self.special_modifier = special_modifier
            self.lighting = lighting
            self.display_transform = display_transform
            self.sort_order = 2
            self.z_order = 0

            if position is None:
                self.position = person.idle_pose

            if emotion is None:
                self.emotion = person.get_emotion()

            if lighting is None:
                lighting = mc.location.get_lighting_conditions()

            if display_transform is None:
                self.display_transform = character_right

            if not z_order is None:
                self.z_order = z_order

            if display_transform == character_center or display_transform == character_center_flipped:
                self.sort_order = 1
            if display_transform == character_left or display_transform == character_left_flipped:
                self.sort_order = 0

        def draw_actor(self):
            self.person.draw_person(position = self.position, emotion = self.emotion, special_modifier = self.special_modifier, lighting = self.lighting, display_transform = self.display_transform, wipe_scene = False)


##########################################
# Transformation for display_transform   #
##########################################
init -1:
    transform character_right(xoffset = 0, yoffset = 0, zoom = 1):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (1.0 + xoffset)
        xanchor 1.0
        zoom zoom


    transform character_right_flipped(xoffset = 0, yoffset = 0, zoom = 1):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (1.0 + xoffset)
        xanchor 1.0
        xzoom -(zoom)
        yzoom zoom

    transform character_center(xoffset = 0, yoffset = 0, zoom = 1):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (0.75 + xoffset)
        xanchor 1.0
        zoom zoom

    transform character_center_flipped(xoffset = 0, yoffset = 0, zoom = 1):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (0.75 + xoffset)
        xanchor 1.0
        xzoom -(zoom)
        yzoom zoom

    transform character_left(xoffset = 0, yoffset = 0, zoom = 1):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (0.5 + xoffset)
        xanchor 1.0
        zoom zoom

    transform character_left_flipped(xoffset = 0, yoffset = 0, zoom = 1):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (0.5 + xoffset)
        xanchor 1.0
        xzoom -(zoom)
        yzoom zoom

    transform character_69_bottom():
        yalign 0.62
        yanchor 0.5
        xalign 1.0
        xanchor 0.95
        zoom 0.8

    transform character_69_on_top():
        yalign 0.38
        yanchor 0.5
        xalign 1.0
        xanchor 1.02
        zoom 0.75
