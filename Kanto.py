print("Think of a Pokemon!")

def ask(question):
while True:
answer = input(question + " (yes/no): ").lower()

if answer == "yes":  
        return "yes"  
    elif answer == "no":  
        return "no"  
    else:  
        print("Please answer only yes or no.")

def not_exist():
print("This Pokemon doesn't exist in the 151 Kanto Pokemon.")

def family_3(family, first, second, third):
if ask("Is it part of the " + family + " family?") == "yes":

if ask("Is it " + first + "?") == "yes":  
        print("It's " + first + "!")  
    elif ask("Is it " + second + "?") == "yes":  
        print("It's " + second + "!")  
    elif ask("Is it " + third + "?") == "yes":  
        print("It's " + third + "!")  
    else:  
        not_exist()  

    return True  

return False

def family_2(family, first, second):
if ask("Is it part of the " + family + " family?") == "yes":

if ask("Is it " + first + "?") == "yes":  
        print("It's " + first + "!")  
    elif ask("Is it " + second + "?") == "yes":  
        print("It's " + second + "!")  
    else:  
        not_exist()  

    return True  

return False

def family_1(family, pokemon):
if ask("Is it " + family + "?") == "yes":
print("It's " + pokemon + "!")
return True

return False

def starter_branch():

if ask("Does it belong to Ash Ketchum?") == "yes":  
    print("It's Pikachu!")  
    return  

if family_3("Bulbasaur", "Bulbasaur", "Ivysaur", "Venusaur"):  
    return  

if family_3("Charmander", "Charmander", "Charmeleon", "Charizard"):  
    return  

if family_3("Squirtle", "Squirtle", "Wartortle", "Blastoise"):  
    return  

not_exist()

def legendary_branch():

if family_1("Articuno", "Articuno"):  
    return  

if family_1("Zapdos", "Zapdos"):  
    return  

if family_1("Moltres", "Moltres"):  
    return  

if family_1("Mewtwo", "Mewtwo"):  
    return  

not_exist()

def eeveelution_branch():

if ask("Is it Vaporeon?") == "yes":  
    print("It's Vaporeon!")  
elif ask("Is it Jolteon?") == "yes":  
    print("It's Jolteon!")  
elif ask("Is it Flareon?") == "yes":  
    print("It's Flareon!")  
else:  
    not_exist()

def pokemon_branch():

# Bug families  
if family_3("Caterpie", "Caterpie", "Metapod", "Butterfree"):  
    return  

elif family_3("Weedle", "Weedle", "Kakuna", "Beedrill"):  
    return  

# Flying families  
elif family_3("Pidgey", "Pidgey", "Pidgeotto", "Pidgeot"):  
    return  

elif family_2("Rattata", "Rattata", "Raticate"):  
    return  

elif family_2("Spearow", "Spearow", "Fearow"):  
    return  

# Poison families  
elif family_2("Ekans", "Ekans", "Arbok"):  
    return  

elif family_1("Raichu", "Raichu"):  
    return  

# Ground families  
elif family_2("Sandshrew", "Sandshrew", "Sandslash"):  
    return  

elif family_3("Nidoran Female", "Nidoran Female", "Nidorina", "Nidoqueen"):  
    return  

elif family_3("Nidoran Male", "Nidoran Male", "Nidorino", "Nidoking"):  
    return  

# Fairy families  
elif family_2("Clefairy", "Clefairy", "Clefable"):  
    return  

elif family_2("Vulpix", "Vulpix", "Ninetales"):  
    return  

elif family_2("Jigglypuff", "Jigglypuff", "Wigglytuff"):  
    return  

# Poison / Flying  
elif family_2("Zubat", "Zubat", "Golbat"):  
    return  

# Grass / Poison  
elif family_3("Oddish", "Oddish", "Gloom", "Vileplume"):  
    return  

# Bug / Grass  
elif family_2("Paras", "Paras", "Parasect"):  
    return  

# Bug / Poison  
elif family_2("Venonat", "Venonat", "Venomoth"):  
    return  

# Ground  
elif family_2("Diglett", "Diglett", "Dugtrio"):  
    return  

# Normal  
elif family_2("Meowth", "Meowth", "Persian"):  
    return  

# Water  
elif family_2("Psyduck", "Psyduck", "Golduck"):  
    return  

# Fighting  
elif family_2("Mankey", "Mankey", "Primeape"):  
    return  

# Fire  
elif family_2("Growlithe", "Growlithe", "Arcanine"):  
    return  

# Water families  
elif family_3("Poliwag", "Poliwag", "Poliwhirl", "Poliwrath"):  
    return  

# Psychic  
elif family_3("Abra", "Abra", "Kadabra", "Alakazam"):  
    return  

# Fighting  
elif family_3("Machop", "Machop", "Machoke", "Machamp"):  
    return  

# Grass / Poison  
elif family_3("Bellsprout", "Bellsprout", "Weepinbell", "Victreebel"):  
    return  

# Water / Poison  
elif family_2("Tentacool", "Tentacool", "Tentacruel"):  
    return  

# Rock / Ground  
elif family_3("Geodude", "Geodude", "Graveler", "Golem"):  
    return  

# Fire  
elif family_2("Ponyta", "Ponyta", "Rapidash"):  
    return  

# Water / Psychic  
elif family_2("Slowpoke", "Slowpoke", "Slowbro"):  
    return  

# Electric / Steel  
elif family_2("Magnemite", "Magnemite", "Magneton"):  
    return  

# Normal / Flying  
elif family_1("Farfetch'd", "Farfetch'd"):  
    return  

elif family_2("Doduo", "Doduo", "Dodrio"):  
    return  

# Water / Ice  
elif family_2("Seel", "Seel", "Dewgong"):  
    return  

# Poison  
elif family_2("Grimer", "Grimer", "Muk"):  
    return  

# Water / Ice  
elif family_2("Shellder", "Shellder", "Cloyster"):  
    return  

# Ghost / Poison  
elif family_3("Gastly", "Gastly", "Haunter", "Gengar"):  
    return  

# Rock / Ground  
elif family_1("Onix", "Onix"):  
    return  

# Psychic  
elif family_2("Drowzee", "Drowzee", "Hypno"):  
    return  

# Water  
elif family_2("Krabby", "Krabby", "Kingler"):  
    return  

# Electric  
elif family_2("Voltorb", "Voltorb", "Electrode"):  
    return  

# Grass / Psychic  
elif family_2("Exeggcute", "Exeggcute", "Exeggutor"):  
    return  

# Ground  
elif family_2("Cubone", "Cubone", "Marowak"):  
    return  

# Fighting  
elif family_1("Hitmonlee", "Hitmonlee"):  
    return  

elif family_1("Hitmonchan", "Hitmonchan"):  
    return  

# Normal  
elif family_1("Lickitung", "Lickitung"):  
    return  

# Poison  
elif family_2("Koffing", "Koffing", "Weezing"):  
    return  

# Ground / Rock  
elif family_2("Rhyhorn", "Rhyhorn", "Rhydon"):  
    return  

# Normal  
elif family_1("Chansey", "Chansey"):  
    return  

elif family_1("Tangela", "Tangela"):  
    return  

elif family_1("Kangaskhan", "Kangaskhan"):  
    return  

# Water  
elif family_2("Horsea", "Horsea", "Seadra"):  
    return  

elif family_2("Goldeen", "Goldeen", "Seaking"):  
    return  

elif family_2("Staryu", "Staryu", "Starmie"):  
    return  

# Psychic / Fairy  
elif family_1("Mr. Mime", "Mr. Mime"):  
    return  

# Bug / Flying  
elif family_1("Scyther", "Scyther"):  
    return  

# Ice / Psychic  
elif family_1("Jynx", "Jynx"):  
    return  

# Electric  
elif family_1("Electabuzz", "Electabuzz"):  
    return  

# Fire  
elif family_1("Magmar", "Magmar"):  
    return  

# Bug  
elif family_1("Pinsir", "Pinsir"):  
    return  

# Normal  
elif family_1("Tauros", "Tauros"):  
    return  

# Water / Flying  
elif family_2("Magikarp", "Magikarp", "Gyarados"):  
    return  

elif family_1("Lapras", "Lapras"):  
    return  

# Normal  
elif family_1("Ditto", "Ditto"):  
    return  

# Normal  
elif family_1("Eevee", "Eevee"):  
    return  

# Normal  
elif family_1("Porygon", "Porygon"):  
    return  

# Rock / Water fossils  
elif family_2("Omanyte", "Omanyte", "Omastar"):  
    return  

elif family_2("Kabuto", "Kabuto", "Kabutops"):  
    return  

# Rock / Flying  
elif family_1("Aerodactyl", "Aerodactyl"):  
    return  

# Normal  
elif family_1("Snorlax", "Snorlax"):  
    return  

# Dragon  
elif family_3("Dratini", "Dratini", "Dragonair", "Dragonite"):  
    return  

# Mythical  
elif family_1("Mew", "Mew"):  
    return  

else:  
    not_exist()

Main game

is_starter = ask("Is it a starter Pokemon?")

if is_starter == "yes":
starter_branch()

else:
is_legendary = ask("Is it a Legendary Pokemon?")

if is_legendary == "yes":  
    legendary_branch()  

else:  
    is_eeveelution = ask("Is it an Eeveelution?")  

    if is_eeveelution == "yes":  
        eeveelution_branch()  

    else:  
        pokemon_branch()