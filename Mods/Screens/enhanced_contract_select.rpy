init 2:
    screen contract_select():
        add "Science_Menu_Background.png"

        modal True
        hbox:
            spacing 40
            xanchor 0.5
            xalign 0.5
            yalign 0.1
            frame:
                xalign 0.05
                yalign 0.05
                xsize 780
                ysize 800
                background "#1a45a1aa"
                vbox:
                    spacing 20
                    text "Available Contracts:" style "menu_text_title_style"
                    viewport:
                        mousewheel True
                        scrollbars "vertical"
                        vbox:
                            spacing 20
                            for new_contract in mc.business.offered_contracts:
                                use contract_select_button(new_contract):
                                    textbutton "Accept Contract":
                                        xanchor 1.0
                                        xalign 0.90
                                        style "textbutton_style"
                                        text_style "menu_text_style"
                                        action Function(mc.business.accept_contract, new_contract)
                                        sensitive len(mc.business.active_contracts) < mc.business.max_active_contracts

            frame:
                xalign 0.05
                yalign 0.05
                xsize 780
                ysize 800
                background "#1a45a1aa"
                vbox:
                    spacing 20
                    text "Current Contracts (" + str(len(mc.business.active_contracts)) + "/" + str(mc.business.max_active_contracts) + " Max)" style "menu_text_title_style"
                    viewport:
                        mousewheel True
                        scrollbars "vertical"
                        vbox:
                            spacing 20
                            for contract in mc.business.active_contracts:
                                use contract_select_button(contract):
                                    textbutton "Abandon": #TODO: This should probably require a double click or something.
                                        xanchor 1.0
                                        xalign 0.90
                                        style "textbutton_style"
                                        text_style "textbutton_text_style"
                                        action Function(mc.business.abandon_contract, contract)


        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action Hide("contract_select")
            textbutton "Return" align [0.5,0.5] style "return_button_style" text_style "return_button_style"

    screen contract_select_button(the_contract):
        frame:
            background "#00000088"
            xsize 800
            hbox:
                ysize 140
                vbox:
                    xsize 580
                    $ contract_name = the_contract.name
                    if the_contract.contract_started:
                        $ contract_name += " (" + str(the_contract.get_current_serum_count()) + "/"+str(the_contract.amount_desired) + ") Doses"
                    else:
                        $ contract_name += " (" + str(the_contract.amount_desired) + " doses requested)"
                    text the_contract.name:
                        style "textbutton_text_style"
                        size 20

                    use contract_aspect_grid(the_contract)

                    text the_contract.description style "textbutton_text_style" size 12 text_align 0.0


                vbox:
                    yfill False
                    xanchor 1.00
                    xalign 0.95
                    xsize 195
                    transclude #Place things on the right side of this entry for things like accessing the inventory.

    screen contract_aspect_grid(the_thing):
        $ non_zero_aspects = 0
        if the_thing.mental_aspect > 0:
            $ non_zero_aspects += 1
        if the_thing.physical_aspect > 0:
            $ non_zero_aspects += 1
        if the_thing.sexual_aspect > 0:
            $ non_zero_aspects += 1
        if the_thing.medical_aspect > 0:
            $ non_zero_aspects += 1

        hbox:
            text "Doses Required: " + str(the_thing.amount_desired) style "menu_text_style" size 14 color "#fbff00"
            text "Payout: $" + str(the_thing.price_per_dose*the_thing.amount_desired) style "menu_text_style" size 14 color "#85bb65"

            if the_thing.contract_started:
                text "Deliver in: " + str(the_thing.contract_length - the_thing.time_elapsed) + " days" style "menu_text_style" size 14 color "#BBBBBB"
            else:
                text "Deliver in: "+ str(the_thing.contract_length) + " days" style "menu_text_style" size 14 color "#BBBBBB"


        grid non_zero_aspects+2 1:
            if the_thing.mental_aspect > 0:
                text "Men: >=" + str(the_thing.mental_aspect) style "menu_text_style" size 14 color "#387aff"
            if the_thing.physical_aspect > 0:
                text "Phy: >=" + str(the_thing.physical_aspect) style "menu_text_style" size 14 color "#00AA00"
            if the_thing.sexual_aspect > 0:
                text "Sex: >=" + str(the_thing.sexual_aspect) style "menu_text_style" size 14 color "#FFC0CB"
            if the_thing.medical_aspect > 0:
                text "Med: >=" + str(the_thing.medical_aspect) style "menu_text_style" size 14 color "#FFFFFF"
            text "Flw: <=" + str(the_thing.flaws_aspect) style "menu_text_style" size 14 color "#AAAAAA"
            text "Attn: <=" + str(the_thing.attention) style "menu_text_style" size 14 color "#FF6249"
