# Fixes the nora traits names, since we only compare by name
# the mastery of all serums with the same name is raised when observing results
# since the nora traits have the same name, it causes the research
# Nora trait game mechanic to fail.

init 5 python:
    add_label_hijack("normal_start", "fix_nora_serum_traits")
    add_label_hijack("after_load", "fix_nora_serum_traits")

    def fix_nora_serum_traits_names():
        nora_suggest_up.name = "Nora's Research Trait XRC"
        nora_nightmares.name = "Nora's Research Trait CBX"
        nora_obedience_swing.name = "Nora's Research Trait XBR"
        nora_sluttiness_boost.name = "Nora's Research Trait RXC"
        # nora_suggest_up.tier = 1
        # nora_nightmares.tier = 1
        # nora_obedience_swing.tier = 1
        # nora_sluttiness_boost.tier = 1
        return

    def add_extra_capability_to_clinical_testing_trait():
        clinical_testing = find_serum_by_name("Clinical Testing Procedures")
        if clinical_testing:
            clinical_testing.attention = -1
            clinical_testing.desc = "A set of careful tests rather than any single ingredient or process. Serums may be put through formal clinical testing, significantly boosting their value to the general public. This also significantly raises the research cost of each serum design, but also lowers overall attention of design by 1."
        return


label fix_nora_serum_traits(stack):
    python:
        fix_nora_serum_traits_names()
        add_extra_capability_to_clinical_testing_trait()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
