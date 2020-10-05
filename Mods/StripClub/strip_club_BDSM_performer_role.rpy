## Stripclub storyline Mod by Corrado
#  BDSM performers role definition.
#  The role is appended to BDSM performers after they start to work for you.

init 3305 python:
    BDSM_performer_wardrobe = wardrobe_from_xml("BDSM_Wardrobe")

    bdsm_performer_role = Role("BDSM performer", [promote_to_manager_action, strip_club_stripper_fire_action, strip_club_stripper_performance_review_action], hidden = False)
