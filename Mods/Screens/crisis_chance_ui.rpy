screen crisis_chance_setting(disabled, morning_disabled):
    modal True
    zorder 49

    default current_crisis_base_chance = crisis_base_chance
    default current_morning_crisis_base_chance = morning_crisis_base_chance

    frame: # top frame
        background "#aaaaaa"
        xsize 900
        ysize 400
        yalign 0.4
        xalign 0.5

        vbox:
            yalign 0.1
            text "Crisis Event [[Total: " + str(len(crisis_list) - disabled) + "]" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_crisis_base_chance", 100.0, step = 1.0) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(int(current_crisis_base_chance)) + "%" style "menu_text_style"

        vbox:
            yalign 0.5
            text "Morning Crisis Event [[Total: " + str(len(morning_crisis_list) - morning_disabled) + "]" style "textbutton_text_style"           
            hbox:
                bar value ScreenVariableValue("current_morning_crisis_base_chance", 100.0, step = 1.0) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(int(current_morning_crisis_base_chance)) + "%" style "menu_text_style"

        hbox:
            yalign 0.7
            xsize 900
            text "{size=16}Warning: high values will increase the chance of an event to occur on every time advance in the game." style "warning_text"

        hbox:
            yalign 1.0
            xalign 0.5
            xanchor 0.5
            spacing 50
            textbutton "Cancel" action [Return] style "textbutton_style" text_style "textbutton_text_style" tooltip "" text_text_align 0.5 text_xalign 0.5 xysize (155,60)
            textbutton "Save" action [SetVariable("crisis_base_chance", int(current_crisis_base_chance)),SetVariable("morning_crisis_base_chance",int(current_morning_crisis_base_chance)), Return] style "textbutton_style" text_style "textbutton_text_style" tooltip "" text_text_align 0.5 text_xalign 0.5 xysize (155,60)

style warning_text:
    color "B22222"
    size 16
    xalign 0.5