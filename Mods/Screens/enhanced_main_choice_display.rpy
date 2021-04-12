# The enhanced version will hide columns that have no actions in them.

init 2 python:
    # insert class from bugfix into mod (allows for cleaner and faster menus)
    class MenuItem():
        def __init__(self, title = "", return_value = None, the_tooltip = None, extra_args = None, display = True, is_sensitive = True, display_key = None, display_scale = 0.9, display_func = None, person_preview_args = None):
            self.title = ""
            self.return_value = return_value
            self.the_tooltip = the_tooltip
            self.extra_args = extra_args
            self.display = display
            self.is_sensitive = is_sensitive
            self.display_key = display_key
            self.display_scale = display_scale
            self.display_func = display_func
            self.display_image = None
            self.person_preview_args = person_preview_args

        def load(self):
            if not self.display_func or self.display_image:
                return

            self.display_image = self.display_func(lighting = mc.location.get_lighting_conditions(), **self.person_preview_args)
            # always predict person displayable (the clear_function will remove them from the prediction cache)
            renpy.start_predict(self.display_image)
            return

        def show_person(self):
            if not self.display_func:
                return

            load_time = time.time()
            if not self.display_image:
                self.load()

            renpy.show(self.display_key, at_list=[character_right, self.display_scale], layer="solo", what= self.display_image, tag=self.display_key)

            global last_load_time
            last_load_time = time.time() - load_time
            return

        def hide_person(self):
            if self.display_key:
                renpy.hide(self.display_key, layer="solo")
            return

        def preload(self):
            def load_image(file):
                if file and not "empty_holder.png" in file.filename:
                    file.load()
                return

            def actual_body_type(person, cloth):
                if not cloth.body_dependant:
                    body_type = "standard_body"
                return person.body_type

            def actual_tit_size(person, cloth):
                if cloth.draws_breasts:
                    return person.tits
                return "AA"

            if not self.display_func:
                return

            # pre-load clothing items
            person = self.return_value
            for cloth in person.outfit.generate_clothing_list(person.body_type, person.tits, person.idle_pose):
                if isinstance(cloth, Facial_Accessory):
                    load_image(cloth.position_sets[person.idle_pose].get_image(person.face_style, "default"))
                else:
                    load_image(cloth.position_sets[person.idle_pose].get_image(actual_body_type(person, cloth), actual_tit_size(person, cloth)))
            return

        def clear(self):
            if self.display_image:
                 renpy.stop_predict(self.display_image)
            return

    def build_menu_items(elements_list, draw_person_previews = True, draw_hearts_for_people = True, person_preview_args = None):
        result = []
        for count in __builtin__.range(__builtin__.len(elements_list)):
            if __builtin__.len(elements_list[count]) > 1:
                if not isinstance(elements_list[count][1], MenuItem):
                    result.append(build_menu_item_list(elements_list[count], draw_person_previews, draw_hearts_for_people, person_preview_args))
                else:
                    result.append(elements_list[count])
        return result

    def clear_menu_items_list(menu_items):
        start_time = time.time()
        for count in __builtin__.range(__builtin__.len(menu_items)):
            for item in [x for x in menu_items[count][1:] if x.display_key]:
                item.clear()
        return

    def build_menu_item_list(element_list, draw_person_previews = True, draw_hearts_for_people = True, person_preview_args = None):
        def find_and_replace_tooltip_property(item, extra_args):
            groups = re.search("\[[^]]*\]", item.menu_tooltip)
            if groups and isinstance(extra_args, Person):
                if ".title" in groups.group(0):
                    return re.sub("\[[^]]*\]", extra_args.title, item.menu_tooltip)
                if ".name" in groups.group(0):
                    return re.sub("\[[^]]*\]", extra_args.name, item.menu_tooltip)
            return item.menu_tooltip

        result = []
        result.append(element_list[0])

        column_elements = element_list[1:]
        for item in column_elements:
            mi = MenuItem()

            if isinstance(item, list): #It's a title/return value pair. Show the title, return the value.
                if isinstance(item[0], Action): #It's an action with extra arguments.
                    mi.extra_args = item[1]
                    item = item[0] #Rename item so that this is caught by the action section below.

                else: #It's (probably) a title/return string pair. Show the title, return the value
                    mi.title = item[0]
                    mi.return_value = item[1]

            if isinstance(item,Person): #It's a person. Format it for a person list.
                mi.title = format_titles(item)
                mi.return_value = item

                if item.infractions:
                    mi.title += " {image=infraction_token_small}"
                if draw_hearts_for_people:
                    mi.title += "\n" + get_heart_image_list(item)
                if person_preview_args is None:
                    person_preview_args = {}

                mi.person_preview_args = person_preview_args
                mi.display_key = item.identifier
                mi.display_scale = scale_person(item.height)
                if draw_person_previews:
                    mi.display_func = item.build_person_displayable
                if not renpy.mobile: # don't load person on mobile
                    renpy.invoke_in_thread(mi.preload)

            if isinstance(item, Action):
                mi.title = ""
                mi.return_value = item
                mi.display = False #Default display state for an action is to hide it unless it is enabled or has a disabled slug
                if item.is_action_enabled(mi.extra_args):
                    mi.title = item.name
                    mi.display = True

                elif item.is_disabled_slug_shown(mi.extra_args):
                    mi.title = item.get_disabled_slug_name(mi.extra_args)
                    mi.display = True

                if item.menu_tooltip:
                    mi.the_tooltip = find_and_replace_tooltip_property(item, mi.extra_args)

            if isinstance(item, basestring): #It's just text. Display the text and return the text.
                mi.title = item
                mi.return_value = item

            if " (tooltip)" in mi.title:
                mi.the_tooltip = mi.title.split(" (tooltip)",1)[1]
                mi.title = mi.title.replace(" (tooltip)" + mi.the_tooltip,"")

            if " (disabled)" in mi.title:
                mi.title = mi.title.replace(" (disabled)", "")
                parts = mi.title.split("\n")
                if __builtin__.len(parts) > 1: # color and size disable reason
                    parts[-1] = "{color=#ff0000}{size=16}" + parts[-1] + "{/color}{/size}"
                    mi.title = "\n".join(parts)
                mi.is_sensitive = False

            if mi.display:
                if isinstance(item,Person) and isinstance(item.title, basestring) and isinstance(mi.the_tooltip, basestring):
                    mi.the_tooltip = mi.the_tooltip.replace("[the_person.title]", item.title)
                result.append(mi)
        return result

    def hide_menu_person(item):
        if item.display_key:
            renpy.hide(item.display_key, layer="solo")
            #clear_scene()
        return

init 2:
    screen enhanced_main_choice_display(menu_items): #Elements_list is a list of lists, with each internal list receiving an individual column
        #The first element in a column should be the title, either text or a displayable. After that it should be a tuple of (displayable/text, return_value).

        hbox:
            spacing 10
            xalign 0.518
            yalign 0.2
            xanchor 0.5
            yanchor 0.0
            for count in __builtin__.range(len(menu_items)):
                if __builtin__.len(menu_items[count][1:]) > 0:
                    frame:
                        background "gui/LR2_Main_Choice_Box.png"
                        xsize 380
                        ysize 700
                        $ title_element = menu_items[count][0]
                        if isinstance(title_element, basestring):
                            text title_element xalign 0.5 ypos 45 anchor (0.5,0.5) size 22 style "menu_text_style" xsize 240
                        else:
                            add title_element xalign 0.5 ypos 45 anchor (0.5,0.5)

                        viewport id title_element:
                            #scrollbars "vertical" #But if we aren't on a PC we need to make sure the player can scroll since they won't have a mouse wheel.

                            mousewheel True
                            xalign 0.5
                            xanchor 0.5
                            yanchor 0.0

                            ypos 99
                            xsize 360
                            ysize 588
                            vbox:
                                for item in menu_items[count][1:]:
                                    if item.display:
                                        textbutton item.title:
                                            xsize 360
                                            ysize 80
                                            xalign 0.5
                                            yalign 0.5
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            text_align (0.5,0.5)
                                            if not renpy.mobile and item.display_key:
                                                hovered [Function(item.show_person)]
                                                unhovered [Function(item.hide_person)]
                                            action [
                                                Function(item.hide_person),
                                                Function(clear_menu_items_list, menu_items),
                                                Return(item.return_value)
                                            ]
                                            tooltip item.the_tooltip
                                            sensitive item.is_sensitive
                        vbar:
                            value YScrollValue(title_element)
                            xalign 0.99
                            yalign 0.99
                            ysize 585

transform character_off_screen():
    yalign 0.5
    yanchor 0.5
    xalign 2.0
    xanchor 1.0
