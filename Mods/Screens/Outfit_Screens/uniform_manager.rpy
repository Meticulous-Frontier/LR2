init 2:
    screen uniform_manager():
        add "Paper_Background.png"
        modal True
        $ slide_amount = 120 #Easier modification for where the headers sit.

        frame:
            background "#0a142688"
            xpos 1520
            ypos 0
            xysize (400, 1080)

        vbox:
            spacing 10
            hbox:
                null width 425 + slide_amount
                text "Uniform Style" style "menu_text_style" size 30
                null width 400
                text "Used By"  style "menu_text_style" size 30

            null height -25
            hbox:
                spacing 56

                #text "Name" style "menu_text_style" size 30
                null width 315 + slide_amount

                text "Full" style "menu_text_style" size 25 xsize 50 #TODO: Make these textbuttons so we can have tooltips
                text "Over" style "menu_text_style" size 25 xsize 50
                text "Under" style "menu_text_style" size 25  xsize 50

                null# width 50

                text "Market" style "menu_text_style" size 25 xsize 50
                text "R&D" style "menu_text_style" size 25 xsize 50
                text "Prod" style "menu_text_style" size 25 xsize 50
                text "Supply" style "menu_text_style" size 25 xsize 50
                text "HR" style "menu_text_style" size 25 xsize 50
            viewport:
                xalign 0.05
                yalign 0.05
                scrollbars "vertical"
                ysize 750
                mousewheel True
                vbox:
                    for a_uniform in mc.business.business_uniforms:
                        use uniform_entry(a_uniform)

            textbutton "Add Uniform":
                style "textbutton_style"
                text_style "textbutton_text_style"
                xysize (160, 46)
                yanchor 0.5
                yalign 0.5
                background "#43B197"
                hover_background "#143869"
                action Return("Add")

        frame:
            background None
            anchor [0.5,0.5]
            align [0.39,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action [mc.business.update_uniform_wardrobes(), Return(None)]
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"

    screen uniform_entry(given_uniform):
        frame:
            background "#0a142688"
            hbox:
                spacing 70
                hbox:
                    spacing 10
                    textbutton given_uniform.outfit.name:
                        xsize 250
                        yanchor 0.5
                        yalign 0.5
                        sensitive True
                        hovered Function(draw_average_mannequin, given_uniform.outfit)
                        unhovered Function(hide_mannequin)
                        action NullAction()
                        style "textbutton_style"
                        text_style "textbutton_text_style"
                    textbutton "Remove":
                        xsize 150
                        text_xanchor 0.5
                        text_xalign 0.5
                        yanchor 0.5
                        yalign 0.5
                        sensitive True
                        hovered Function(draw_average_mannequin, given_uniform.outfit)
                        unhovered Function(hide_mannequin)
                        action [Function(hide_mannequin), RemoveFromSet(mc.business.business_uniforms, given_uniform)]
                        style "textbutton_style"
                        text_style "textbutton_text_style"
                        background "#B14365"
                        hover_background "#143869"
                #null
                use uniform_button(state = given_uniform.full_outfit_flag, is_sensitive = given_uniform.can_toggle_full_outfit_state(), toggle_function = given_uniform.set_full_outfit_flag, outfit_preview = given_uniform.outfit)
                use uniform_button(state = given_uniform.overwear_flag, is_sensitive = given_uniform.can_toggle_overwear_state(), toggle_function = given_uniform.set_overwear_flag, outfit_preview = given_uniform.outfit)
                use uniform_button(state = given_uniform.underwear_flag, is_sensitive = given_uniform.can_toggle_underwear_state(), toggle_function = given_uniform.set_underwear_flag, outfit_preview = given_uniform.outfit)

                null #Spacing purposes
                use uniform_button(state = given_uniform.marketing_flag, is_sensitive = True, toggle_function = given_uniform.set_marketing_flag, outfit_preview = given_uniform.outfit)
                use uniform_button(state = given_uniform.research_flag, is_sensitive = True, toggle_function = given_uniform.set_research_flag, outfit_preview = given_uniform.outfit)
                use uniform_button(state = given_uniform.production_flag, is_sensitive = True, toggle_function = given_uniform.set_production_flag, outfit_preview = given_uniform.outfit)
                use uniform_button(state = given_uniform.supply_flag, is_sensitive = True, toggle_function = given_uniform.set_supply_flag, outfit_preview = given_uniform.outfit)
                use uniform_button(state = given_uniform.hr_flag, is_sensitive = True, toggle_function = given_uniform.set_hr_flag, outfit_preview = given_uniform.outfit)

    screen uniform_button(state, is_sensitive, toggle_function, outfit_preview = None):
        $ button_colour = "#666666"
        $ hovered_button_colour = "#aaaaaa"

        if is_sensitive:
            if state:
                $ button_colour = "#449044"
                $ hovered_button_colour = "#66a066"

        else:
            $ button_colour = "#00000088"
            #$ hovered_button_colour = "#888888"

        button:
            background button_colour
            hover_background hovered_button_colour
            sensitive is_sensitive
            if outfit_preview:
                hovered Function(draw_average_mannequin, outfit_preview)
                unhovered Function(hide_mannequin)
            action Function(toggle_function, not state)
            xsize 50 ysize 40
            yanchor 0.5 yalign 0.5
