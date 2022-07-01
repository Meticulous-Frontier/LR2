# Enables extra functions for SerumDesign / SerumTraits.
init 2 python:
   def anorexia_serum_on_turn(person, the_serum, add_to_log):
      return person.change_weight(amount = -0.5, chance = 50)

   def hypothyroidism_serum_on_turn(person, the_serum, add_to_log):
      return person.change_weight(amount = 0.5, chance = 50)

   def height_increase_on_turn(person, the_serum, add_to_log):
      if renpy.random.randint(0,100) < 3: # 3% chance of breast size increase
         new_tits = Person.get_larger_tit(person.tits)
         if new_tits != person.tits: #Double check we don't already have them to avoid increasing breast weight infinitely
            person.tits = new_tits
            person.personal_region_modifiers["breasts"] += 0.1 #Her breasts receive a boost in region weight because they're natural.
      return person.change_height(.01693, 20)

   def height_decrease_on_turn(person, the_serum, add_to_log):
      if renpy.random.randint(0,100) < 3: # 3% chance of breast size decrease
            new_tits = Person.get_smaller_tit(person.tits)
            if new_tits != person.tits:
               person.tits = new_tits
               person.personal_region_modifiers["breasts"] -= 0.1 #Her breasts receive a boost in region weight because they're natural.
      return person.change_height(-.01693, 20)

   # Override base game serum functions
   if 'weight_loss' in dir():
      weight_loss.desc = "Decrease target subject body mass, using peptide YY3-36 as a serum component that acts on the hypothalamic feeding centers to inhibit hunger and calorie intake."
      weight_loss.positive_slug = "50% Chance/Turn to reduce body mass by 500 grams"
      weight_loss.on_turn = anorexia_serum_on_turn

      weight_gain.desc = "Increase target subject body mass, by reducing hormones from the thyroid gland slowing down metabolism, thus causing weight gain."
      weight_gain.positive_slug = "50% Chance/Turn to increase body mass by 500 grams"
      weight_gain.on_turn = hypothyroidism_serum_on_turn

   if 'height_increase' in dir():
      height_increase.on_day = None
      height_increase.on_turn = height_increase_on_turn
   if 'height_decrease' in dir():
      height_decrease.on_day = None
      height_decrease.on_turn = height_decrease_on_turn
