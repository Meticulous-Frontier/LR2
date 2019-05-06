# if suggestability is enabled now depends on the lysergide_n2o_serum
# the serum adds the role action to a person and removes it when
# the serum wears off

init 1 python:
    suggestable_role = Role("Suggestable", [])

init 2 python:
    suggestable_role.actions.append(influence_opinion)
