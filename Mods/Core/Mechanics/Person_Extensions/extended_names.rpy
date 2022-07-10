init -1 python:
    # prevent choosing name already used in game
    @classmethod
    def get_unused_name(cls):
        names = [person.name for person in all_people_in_the_game()]
        return renpy.random.choice(list(set(Person._list_of_names)-set(names)))

    Person.get_random_name = get_unused_name

    # prevent choosing last_name already used in game
    @classmethod
    def get_unused_last_name(cls):
        names = [person.last_name for person in all_people_in_the_game()]
        return renpy.random.choice(list(set(Person._list_of_last_names)-set(names)))

    Person.get_random_last_name = get_unused_last_name

    # Remove default names for unique characters from possible name list
    if "Candace" in Person._list_of_names:
        Person._list_of_names.remove("Candace")
    if "Ashley" in Person._list_of_names:
        Person._list_of_names.remove("Ashley")
    if "Emily" in Person._list_of_names:
        Person._list_of_names.remove("Emily")
    if "Christina" in Person._list_of_names:
        Person._list_of_names.remove("Christina")
    if "Christine" in Person._list_of_names:
        Person._list_of_names.remove("Christine")
    if "Gabrielle" in Person._list_of_names:
        Person._list_of_names.remove("Gabrielle")
    if "Rebecca" in Person._list_of_names:
        Person._list_of_names.remove("Rebecca")
    if "Stephanie" in Person._list_of_names:
        Person._list_of_names.remove("Stephanie")
    if "Cara" in Person._list_of_names:
        Person._list_of_names.remove("Cara")
    if "Erica" in Person._list_of_names:
        Person._list_of_names.remove("Erica")
    if "Kaya" in Person._list_of_names:
        Person._list_of_names.remove("Kaya")
    if "Sakari" in Person._list_of_names:
        Person._list_of_names.remove("Sakari")
    if "Ellie" in Person._list_of_names:
        Person._list_of_names.remove("Ellie")
    if "Sarah" in Person._list_of_names:
        Person._list_of_names.remove("Sarah")
    if "Ophelia" in Person._list_of_names:
        Person._list_of_names.remove("Ophelia")

    if "Rojas" in Person._list_of_last_names:
        Person._list_of_last_names.remove("Rojas")
    if "Hooper" in Person._list_of_last_names:
        Person._list_of_last_names.remove("Hooper")
    if "Lavardin" in Person._list_of_last_names:
        Person._list_of_last_names.remove("Lavardin")
    if "Greene" in Person._list_of_last_names:
        Person._list_of_last_names.remove("Greene")
    if "von Friseur" in Person._list_of_last_names:
        Person._list_of_last_names.remove("von Friseur")
    if "Cooper" in Person._list_of_last_names:
        Person._list_of_last_names.remove("Cooper")
    if "Walters" in Person._list_of_last_names:
        Person._list_of_last_names.remove("Walters")

    # Extra names provided by LangyMD (based on US consensus)
    Person._list_of_names.append("Mary")
    Person._list_of_names.append("Patricia")
    Person._list_of_names.append("Linda")
    Person._list_of_names.append("Barbara")
    Person._list_of_names.append("Margaret")
    Person._list_of_names.append("Dorothy")
    Person._list_of_names.append("Lisa")
    Person._list_of_names.append("Nancy")
    Person._list_of_names.append("Karen")
    Person._list_of_names.append("Betty")
    Person._list_of_names.append("Donna")
    Person._list_of_names.append("Carol")
    Person._list_of_names.append("Ruth")
    Person._list_of_names.append("Sharon")
    Person._list_of_names.append("Michelle")
    Person._list_of_names.append("Laura")
    Person._list_of_names.append("Kimberly")
    Person._list_of_names.append("Deborah")
    Person._list_of_names.append("Cynthia")
    Person._list_of_names.append("Melissa")
    Person._list_of_names.append("Brenda")
    Person._list_of_names.append("Amy")
    Person._list_of_names.append("Virginia")
    Person._list_of_names.append("Kathleen")
    Person._list_of_names.append("Pamela")
    Person._list_of_names.append("Martha")
    Person._list_of_names.append("Debra")
    Person._list_of_names.append("Amanda")
    Person._list_of_names.append("Carolyn")
    # Popular Names from UK census
    Person._list_of_names.append("Amelia")
    Person._list_of_names.append("Ava")
    Person._list_of_names.append("Mia")
    Person._list_of_names.append("Grace")
    Person._list_of_names.append("Sophia")
    Person._list_of_names.append("Aisha")
    Person._list_of_names.append("Ivy")
    Person._list_of_names.append("Ella")
    Person._list_of_names.append("Florence")
    Person._list_of_names.append("Willow")
    Person._list_of_names.append("Phoebe")
    Person._list_of_names.append("Sienna")
    Person._list_of_names.append("Ruby")
    Person._list_of_names.append("Harper")
    Person._list_of_names.append("Luna")
    Person._list_of_names.append("Eliza")
    Person._list_of_names.append("Chloe")
    Person._list_of_names.append("Maisie")

    # Extra last names provided by LangyMD (based on US consensus)
    Person._list_of_last_names.append("Smith")
    Person._list_of_last_names.append("Johnson")
    Person._list_of_last_names.append("Brown")
    Person._list_of_last_names.append("Davis")
    Person._list_of_last_names.append("Miller")
    Person._list_of_last_names.append("Wilson")
    Person._list_of_last_names.append("Moore")
    Person._list_of_last_names.append("Taylor")
    Person._list_of_last_names.append("Thomas")
    Person._list_of_last_names.append("Jackson")
    Person._list_of_last_names.append("White")
    Person._list_of_last_names.append("Harris")
    Person._list_of_last_names.append("Martin")
    Person._list_of_last_names.append("Thompson")
    Person._list_of_last_names.append("Garcia")
    Person._list_of_last_names.append("Robinson")
    Person._list_of_last_names.append("Clark")
    Person._list_of_last_names.append("Lewis")
    Person._list_of_last_names.append("Walker")
    Person._list_of_last_names.append("Hall")
    Person._list_of_last_names.append("Allen")
    Person._list_of_last_names.append("Young")
    Person._list_of_last_names.append("King")
    Person._list_of_last_names.append("Wright")
    Person._list_of_last_names.append("Hill")
    Person._list_of_last_names.append("Scott")
    Person._list_of_last_names.append("Green")
    Person._list_of_last_names.append("Adams")

    # Extra male names provided by LangyMD (based on US consensus)
    Person._list_of_male_names.append("James")
    Person._list_of_male_names.append("John")
    Person._list_of_male_names.append("Robert")
    Person._list_of_male_names.append("Michael")
    Person._list_of_male_names.append("David")
    Person._list_of_male_names.append("Richard")
    Person._list_of_male_names.append("Charles")
    Person._list_of_male_names.append("Joseph")
    Person._list_of_male_names.append("Christopher")
    Person._list_of_male_names.append("Daniel")
    Person._list_of_male_names.append("Paul")
    Person._list_of_male_names.append("Mark")
    Person._list_of_male_names.append("Donald")
    Person._list_of_male_names.append("George")
    Person._list_of_male_names.append("Kenneth")
    Person._list_of_male_names.append("Steven")
    Person._list_of_male_names.append("Edward")
    Person._list_of_male_names.append("Brian")
    Person._list_of_male_names.append("Ronald")
    Person._list_of_male_names.append("Anthony")
    Person._list_of_male_names.append("Kevin")
    Person._list_of_male_names.append("Jason")
    Person._list_of_male_names.append("Matthew")
    Person._list_of_male_names.append("Gary")
    Person._list_of_male_names.append("Timothy")
    Person._list_of_male_names.append("Jose")
    Person._list_of_male_names.append("Larry")
    Person._list_of_male_names.append("Jeffrey")
    Person._list_of_male_names.append("Frank")
    Person._list_of_male_names.append("Eric")

    # Spanish
    Person._list_of_names.append("Anahi")
    Person._list_of_names.append("Belen")
    Person._list_of_names.append("Dulce")
    Person._list_of_names.append("Esperanza")
    Person._list_of_names.append("Graciela")
    Person._list_of_names.append("Izzabella")
    Person._list_of_names.append("Mireya")
    Person._list_of_names.append("Perla")
    Person._list_of_names.append("Reina")
    Person._list_of_names.append("Savanna")
    Person._list_of_names.append("Yesenia")

    Person._list_of_last_names.append("Alonso")
    Person._list_of_last_names.append("Diaz")
    Person._list_of_last_names.append("Gutierrez")
    Person._list_of_last_names.append("Hernandez")
    Person._list_of_last_names.append("Jimenez")
    Person._list_of_last_names.append("Lopez")
    Person._list_of_last_names.append("Martinez")
    Person._list_of_last_names.append("Navarro")
    Person._list_of_last_names.append("Rodriguez")
    Person._list_of_last_names.append("Sanchez")


    # French
    Person._list_of_names.append("Antoinette")
    Person._list_of_names.append("Claudette")
    Person._list_of_names.append("Dominique")
    Person._list_of_names.append("Fleur")
    Person._list_of_names.append("Josephine")
    Person._list_of_names.append("Noelle")
    Person._list_of_names.append("Solange")
    Person._list_of_names.append("Veronique")
    Person._list_of_names.append("Yvette")
    Person._list_of_names.append("Zara")

    Person._list_of_last_names.append("Baptiste")
    Person._list_of_last_names.append("Belcourt")
    Person._list_of_last_names.append("Dubois")
    Person._list_of_last_names.append("Leclercq")
    Person._list_of_last_names.append("Lefebvre")
    Person._list_of_last_names.append("Moreau")
    Person._list_of_last_names.append("Perrin")
    Person._list_of_last_names.append("Rousseau")
    Person._list_of_last_names.append("Vallet")
    Person._list_of_last_names.append("Vivier")

    # German
    Person._list_of_names.append("Anna")
    Person._list_of_names.append("Charlotte")
    Person._list_of_names.append("Emilie")
    Person._list_of_names.append("Hannah")
    Person._list_of_names.append("Ingrid")
    Person._list_of_names.append("Klara")
    Person._list_of_names.append("Lena")
    Person._list_of_names.append("Mila")
    Person._list_of_names.append("Ramona")
    Person._list_of_names.append("Sabine")
    Person._list_of_names.append("Sophie")

    Person._list_of_last_names.append("Baumann")
    Person._list_of_last_names.append("Fisher")
    Person._list_of_last_names.append("Graf")
    Person._list_of_last_names.append("Engel")
    Person._list_of_last_names.append("Fisher")
    Person._list_of_last_names.append("Krüger")
    Person._list_of_last_names.append("Lehmann")
    Person._list_of_last_names.append("Müller")
    Person._list_of_last_names.append("Richter")
    Person._list_of_last_names.append("Ziegler")

    # Italian
    Person._list_of_names.append("Aurora")
    Person._list_of_names.append("Celine")
    Person._list_of_names.append("Chiara")
    Person._list_of_names.append("Giulia")
    Person._list_of_names.append("Eleonora")
    Person._list_of_names.append("Francesca")
    Person._list_of_names.append("Gaia")
    Person._list_of_names.append("Ginevra")
    Person._list_of_names.append("Ludovica")
    Person._list_of_names.append("Martina")
    Person._list_of_names.append("Noemi")

    Person._list_of_last_names.append("Alfonsi")
    Person._list_of_last_names.append("Bianchi")
    Person._list_of_last_names.append("Cancio")
    Person._list_of_last_names.append("Colombo")
    Person._list_of_last_names.append("De Luca")
    Person._list_of_last_names.append("Ferrari")
    Person._list_of_last_names.append("Marino")
    Person._list_of_last_names.append("Ricci")
    Person._list_of_last_names.append("Russo")
    Person._list_of_last_names.append("Greco")

    # African
    Person._list_of_names.append("Ashanti")
    Person._list_of_names.append("Eshe")
    Person._list_of_names.append("Hadiyya")
    Person._list_of_names.append("Kesia")
    Person._list_of_names.append("Kalisha")
    Person._list_of_names.append("Malaika")
    Person._list_of_names.append("Poni")
    Person._list_of_names.append("Radhiya")
    Person._list_of_names.append("Shani")
    Person._list_of_names.append("Zuri")

    Person._list_of_last_names.append("Abebe")
    Person._list_of_last_names.append("Alasa")
    Person._list_of_last_names.append("Dogo")
    Person._list_of_last_names.append("Jelani")
    Person._list_of_last_names.append("Mensah")
    Person._list_of_last_names.append("Ndiaye")
    Person._list_of_last_names.append("Okoye")
    Person._list_of_last_names.append("Osei")
    Person._list_of_last_names.append("Temitope")
    Person._list_of_last_names.append("Zivai")
