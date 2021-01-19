init 5 python:
    add_label_hijack("normal_start", "activate_strip_club_set_uniforms_label")
    add_label_hijack("after_load", "activate_strip_club_set_uniforms_label")

    def strip_club_set_uniforms_requirement():
        if get_strip_club_foreclosed_stage() >= 5:
            return True
        return False

    strip_club_set_uniforms_action = Action("Manage Stripclub Uniforms",strip_club_set_uniforms_requirement,"strip_club_set_uniforms_label")

label activate_strip_club_set_uniforms_label(stack):
    python:
        strip_club.add_action(strip_club_set_uniforms_action)
        execute_hijack_call(stack)
    return

label strip_club_set_uniforms_label():
    call screen import_outfit_manager(mc.designed_wardrobe, slut_limit = 999, underwear_limit = 999, show_export = False, use_strip_club_wardrobe = True)
    return
