import subprocess
import sys
from pathlib import Path

import pytest


KANTO_FILE = Path(__file__).parent / "Kanto.py"


def run_game(inputs):
    """Run Kanto.py with simulated user input."""
    result = subprocess.run(
        [sys.executable, str(KANTO_FILE)],
        input="\n".join(inputs) + "\n",
        text=True,
        capture_output=True,
        timeout=10,
    )

    return result


def assert_pokemon(inputs, pokemon):
    """Run the game and verify that it identifies the expected Pokémon."""
    result = run_game(inputs)

    assert result.returncode == 0, (
        f"Kanto.py crashed.\n"
        f"STDOUT:\n{result.stdout}\n"
        f"STDERR:\n{result.stderr}"
    )

    assert f"It's {pokemon}!" in result.stdout


# ============================================================
# INPUT VALIDATION
# ============================================================


def test_invalid_input_is_rejected():
    result = run_game([
        "maybe",
        "yes",
        "yes",
    ])

    assert result.returncode == 0
    assert "Please answer only yes or no." in result.stdout
    assert "It's Pikachu!" in result.stdout


def test_uppercase_input_is_accepted():
    result = run_game([
        "YES",
        "YES",
    ])

    assert result.returncode == 0
    assert "It's Pikachu!" in result.stdout


def test_mixed_case_input_is_accepted():
    result = run_game([
        "YeS",
        "yEs",
    ])

    assert result.returncode == 0
    assert "It's Pikachu!" in result.stdout


# ============================================================
# STARTER BRANCH
# ============================================================


def test_pikachu():
    assert_pokemon(
        [
            "yes",  # Starter
            "yes",  # Belongs to Ash
        ],
        "Pikachu",
    )


@pytest.mark.parametrize(
    "pokemon_answers, pokemon",
    [
        (["yes", "no", "yes", "yes"], "Bulbasaur"),
        (["yes", "no", "yes", "no", "yes"], "Ivysaur"),
        (["yes", "no", "yes", "no", "no", "yes"], "Venusaur"),
        (["yes", "no", "no", "yes", "yes"], "Charmander"),
        (["yes", "no", "no", "yes", "no", "yes"], "Charmeleon"),
        (["yes", "no", "no", "yes", "no", "no", "yes"], "Charizard"),
        (["yes", "no", "no", "no", "yes"], "Squirtle"),
        (["yes", "no", "no", "no", "yes", "no", "yes"], "Wartortle"),
        (["yes", "no", "no", "no", "yes", "no", "no", "yes"], "Blastoise"),
    ],
)
def test_starter_pokemon(pokemon_answers, pokemon):
    assert_pokemon(pokemon_answers, pokemon)


def test_invalid_starter():
    assert_pokemon(
        [
            "yes",  # Starter
            "no",   # Ash
            "no",   # Bulbasaur family
            "no",   # Charmander family
            "no",   # Squirtle family
        ],
        "DOES_NOT_EXIST",
    )


# ============================================================
# LEGENDARY BRANCH
# ============================================================


@pytest.mark.parametrize(
    "answers, pokemon",
    [
        (["no", "yes", "yes"], "Articuno"),
        (["no", "yes", "no", "yes"], "Zapdos"),
        (["no", "yes", "no", "no", "yes"], "Moltres"),
        (["no", "yes", "no", "no", "no", "yes"], "Mewtwo"),
    ],
)
def test_legendary_pokemon(answers, pokemon):
    assert_pokemon(answers, pokemon)


def test_invalid_legendary():
    result = run_game([
        "no",   # Starter
        "yes",  # Legendary
        "no",   # Articuno
        "no",   # Zapdos
        "no",   # Moltres
        "no",   # Mewtwo
    ])

    assert result.returncode == 0
    assert "This Pokemon doesn't exist in the 151 Kanto Pokemon." in result.stdout


# ============================================================
# EEVEELUTION BRANCH
# ============================================================


@pytest.mark.parametrize(
    "answers, pokemon",
    [
        (["no", "no", "yes", "yes"], "Vaporeon"),
        (["no", "no", "yes", "no", "yes"], "Jolteon"),
        (["no", "no", "yes", "no", "no", "yes"], "Flareon"),
    ],
)
def test_eeveelutions(answers, pokemon):
    assert_pokemon(answers, pokemon)


def test_invalid_eeveelution():
    result = run_game([
        "no",   # Starter
        "no",   # Legendary
        "yes",  # Eeveelution
        "no",   # Vaporeon
        "no",   # Jolteon
        "no",   # Flareon
    ])

    assert result.returncode == 0
    assert "This Pokemon doesn't exist in the 151 Kanto Pokemon." in result.stdout


# ============================================================
# REGULAR KANTO POKEMON
# ============================================================

# Each entry:
#
# family_type,
# family_name,
# pokemon_answers,
# expected_pokemon
#
# The first three answers are always:
# no = not starter
# no = not legendary
# no = not Eeveelution
#
# The remaining answers navigate the regular Pokemon tree.

REGULAR_POKEMON = [
    # Bug
    ("family_3", "Caterpie", ["yes", "yes"], "Caterpie"),
    ("family_3", "Caterpie", ["yes", "no", "yes"], "Metapod"),
    ("family_3", "Caterpie", ["yes", "no", "no", "yes"], "Butterfree"),

    ("family_3", "Weedle", ["yes", "yes"], "Weedle"),
    ("family_3", "Weedle", ["yes", "no", "yes"], "Kakuna"),
    ("family_3", "Weedle", ["yes", "no", "no", "yes"], "Beedrill"),

    # Flying
    ("family_3", "Pidgey", ["yes", "yes"], "Pidgey"),
    ("family_3", "Pidgey", ["yes", "no", "yes"], "Pidgeotto"),
    ("family_3", "Pidgey", ["yes", "no", "no", "yes"], "Pidgeot"),

    ("family_2", "Rattata", ["yes", "yes"], "Rattata"),
    ("family_2", "Rattata", ["yes", "no", "yes"], "Raticate"),

    ("family_2", "Spearow", ["yes", "yes"], "Spearow"),
    ("family_2", "Spearow", ["yes", "no", "yes"], "Fearow"),

    # Poison
    ("family_2", "Ekans", ["yes", "yes"], "Ekans"),
    ("family_2", "Ekans", ["yes", "no", "yes"], "Arbok"),

    ("family_1", "Raichu", ["yes"], "Raichu"),

    # Ground
    ("family_2", "Sandshrew", ["yes", "yes"], "Sandshrew"),
    ("family_2", "Sandshrew", ["yes", "no", "yes"], "Sandslash"),

    ("family_3", "Nidoran Female", ["yes", "yes"], "Nidoran Female"),
    ("family_3", "Nidoran Female", ["yes", "no", "yes"], "Nidorina"),
    ("family_3", "Nidoran Female", ["yes", "no", "no", "yes"], "Nidoqueen"),

    ("family_3", "Nidoran Male", ["yes", "yes"], "Nidoran Male"),
    ("family_3", "Nidoran Male", ["yes", "no", "yes"], "Nidorino"),
    ("family_3", "Nidoran Male", ["yes", "no", "no", "yes"], "Nidoking"),

    # Fairy
    ("family_2", "Clefairy", ["yes", "yes"], "Clefairy"),
    ("family_2", "Clefairy", ["yes", "no", "yes"], "Clefable"),

    ("family_2", "Vulpix", ["yes", "yes"], "Vulpix"),
    ("family_2", "Vulpix", ["yes", "no", "yes"], "Ninetales"),

    ("family_2", "Jigglypuff", ["yes", "yes"], "Jigglypuff"),
    ("family_2", "Jigglypuff", ["yes", "no", "yes"], "Wigglytuff"),

    # Poison / Flying
    ("family_2", "Zubat", ["yes", "yes"], "Zubat"),
    ("family_2", "Zubat", ["yes", "no", "yes"], "Golbat"),

    # Grass / Poison
    ("family_3", "Oddish", ["yes", "yes"], "Oddish"),
    ("family_3", "Oddish", ["yes", "no", "yes"], "Gloom"),
    ("family_3", "Oddish", ["yes", "no", "no", "yes"], "Vileplume"),

    # Bug / Grass
    ("family_2", "Paras", ["yes", "yes"], "Paras"),
    ("family_2", "Paras", ["yes", "no", "yes"], "Parasect"),

    # Bug / Poison
    ("family_2", "Venonat", ["yes", "yes"], "Venonat"),
    ("family_2", "Venonat", ["yes", "no", "yes"], "Venomoth"),

    # Ground
    ("family_2", "Diglett", ["yes", "yes"], "Diglett"),
    ("family_2", "Diglett", ["yes", "no", "yes"], "Dugtrio"),

    # Normal
    ("family_2", "Meowth", ["yes", "yes"], "Meowth"),
    ("family_2", "Meowth", ["yes", "no", "yes"], "Persian"),

    # Water
    ("family_2", "Psyduck", ["yes", "yes"], "Psyduck"),
    ("family_2", "Psyduck", ["yes", "no", "yes"], "Golduck"),

    # Fighting
    ("family_2", "Mankey", ["yes", "yes"], "Mankey"),
    ("family_2", "Mankey", ["yes", "no", "yes"], "Primeape"),

    # Fire
    ("family_2", "Growlithe", ["yes", "yes"], "Growlithe"),
    ("family_2", "Growlithe", ["yes", "no", "yes"], "Arcanine"),

    # Water
    ("family_3", "Poliwag", ["yes", "yes"], "Poliwag"),
    ("family_3", "Poliwag", ["yes", "no", "yes"], "Poliwhirl"),
    ("family_3", "Poliwag", ["yes", "no", "no", "yes"], "Poliwrath"),

    # Psychic
    ("family_3", "Abra", ["yes", "yes"], "Abra"),
    ("family_3", "Abra", ["yes", "no", "yes"], "Kadabra"),
    ("family_3", "Abra", ["yes", "no", "no", "yes"], "Alakazam"),

    # Fighting
    ("family_3", "Machop", ["yes", "yes"], "Machop"),
    ("family_3", "Machop", ["yes", "no", "yes"], "Machoke"),
    ("family_3", "Machop", ["yes", "no", "no", "yes"], "Machamp"),

    # Grass / Poison
    ("family_3", "Bellsprout", ["yes", "yes"], "Bellsprout"),
    ("family_3", "Bellsprout", ["yes", "no", "yes"], "Weepinbell"),
    ("family_3", "Bellsprout", ["yes", "no", "no", "yes"], "Victreebel"),

    # Water / Poison
    ("family_2", "Tentacool", ["yes", "yes"], "Tentacool"),
    ("family_2", "Tentacool", ["yes", "no", "yes"], "Tentacruel"),

    # Rock / Ground
    ("family_3", "Geodude", ["yes", "yes"], "Geodude"),
    ("family_3", "Geodude", ["yes", "no", "yes"], "Graveler"),
    ("family_3", "Geodude", ["yes", "no", "no", "yes"], "Golem"),

    # Fire
    ("family_2", "Ponyta", ["yes", "yes"], "Ponyta"),
    ("family_2", "Ponyta", ["yes", "no", "yes"], "Rapidash"),

    # Water / Psychic
    ("family_2", "Slowpoke", ["yes", "yes"], "Slowpoke"),
    ("family_2", "Slowpoke", ["yes", "no", "yes"], "Slowbro"),

    # Electric / Steel
    ("family_2", "Magnemite", ["yes", "yes"], "Magnemite"),
    ("family_2", "Magnemite", ["yes", "no", "yes"], "Magneton"),

    # Normal / Flying
    ("family_1", "Farfetch'd", ["yes"], "Farfetch'd"),

    ("family_2", "Doduo", ["yes", "yes"], "Doduo"),
    ("family_2", "Doduo", ["yes", "no", "yes"], "Dodrio"),

    # Water / Ice
    ("family_2", "Seel", ["yes", "yes"], "Seel"),
    ("family_2", "Seel", ["yes", "no", "yes"], "Dewgong"),

    # Poison
    ("family_2", "Grimer", ["yes", "yes"], "Grimer"),
    ("family_2", "Grimer", ["yes", "no", "yes"], "Muk"),

    # Water / Ice
    ("family_2", "Shellder", ["yes", "yes"], "Shellder"),
    ("family_2", "Shellder", ["yes", "no", "yes"], "Cloyster"),

    # Ghost / Poison
    ("family_3", "Gastly", ["yes", "yes"], "Gastly"),
    ("family_3", "Gastly", ["yes", "no", "yes"], "Haunter"),
    ("family_3", "Gastly", ["yes", "no", "no", "yes"], "Gengar"),

    # Rock / Ground
    ("family_1", "Onix", ["yes"], "Onix"),

    # Psychic
    ("family_2", "Drowzee", ["yes", "yes"], "Drowzee"),
    ("family_2", "Drowzee", ["yes", "no", "yes"], "Hypno"),

    # Water
    ("family_2", "Krabby", ["yes", "yes"], "Krabby"),
    ("family_2", "Krabby", ["yes", "no", "yes"], "Kingler"),

    # Electric
    ("family_2", "Voltorb", ["yes", "yes"], "Voltorb"),
    ("family_2", "Voltorb", ["yes", "no", "yes"], "Electrode"),

    # Grass / Psychic
    ("family_2", "Exeggcute", ["yes", "yes"], "Exeggcute"),
    ("family_2", "Exeggcute", ["yes", "no", "yes"], "Exeggutor"),

    # Ground
    ("family_2", "Cubone", ["yes", "yes"], "Cubone"),
    ("family_2", "Cubone", ["yes", "no", "yes"], "Marowak"),

    # Fighting
    ("family_1", "Hitmonlee", ["yes"], "Hitmonlee"),
    ("family_1", "Hitmonchan", ["yes"], "Hitmonchan"),

    # Normal
    ("family_1", "Lickitung", ["yes"], "Lickitung"),

    # Poison
    ("family_2", "Koffing", ["yes", "yes"], "Koffing"),
    ("family_2", "Koffing", ["yes", "no", "yes"], "Weezing"),

    # Ground / Rock
    ("family_2", "Rhyhorn", ["yes", "yes"], "Rhyhorn"),
    ("family_2", "Rhyhorn", ["yes", "no", "yes"], "Rhydon"),

    # Normal
    ("family_1", "Chansey", ["yes"], "Chansey"),
    ("family_1", "Tangela", ["yes"], "Tangela"),
    ("family_1", "Kangaskhan", ["yes"], "Kangaskhan"),

    # Water
    ("family_2", "Horsea", ["yes", "yes"], "Horsea"),
    ("family_2", "Horsea", ["yes", "no", "yes"], "Seadra"),

    ("family_2", "Goldeen", ["yes", "yes"], "Goldeen"),
    ("family_2", "Goldeen", ["yes", "no", "yes"], "Seaking"),

    ("family_2", "Staryu", ["yes", "yes"], "Staryu"),
    ("family_2", "Staryu", ["yes", "no", "yes"], "Starmie"),

    # Psychic / Fairy
    ("family_1", "Mr. Mime", ["yes"], "Mr. Mime"),

    # Bug / Flying
    ("family_1", "Scyther", ["yes"], "Scyther"),

    # Ice / Psychic
    ("family_1", "Jynx", ["yes"], "Jynx"),

    # Electric
    ("family_1", "Electabuzz", ["yes"], "Electabuzz"),

    # Fire
    ("family_1", "Magmar", ["yes"], "Magmar"),

    # Bug
    ("family_1", "Pinsir", ["yes"], "Pinsir"),

    # Normal
    ("family_1", "Tauros", ["yes"], "Tauros"),

    # Water / Flying
    ("family_2", "Magikarp", ["yes", "yes"], "Magikarp"),
    ("family_2", "Magikarp", ["yes", "no", "yes"], "Gyarados"),

    ("family_1", "Lapras", ["yes"], "Lapras"),

    # Normal
    ("family_1", "Ditto", ["yes"], "Ditto"),

    ("family_1", "Eevee", ["yes"], "Eevee"),

    ("family_1", "Porygon", ["yes"], "Porygon"),

    # Rock / Water fossils
    ("family_2", "Omanyte", ["yes", "yes"], "Omanyte"),
    ("family_2", "Omanyte", ["yes", "no", "yes"], "Omastar"),

    ("family_2", "Kabuto", ["yes", "yes"], "Kabuto"),
    ("family_2", "Kabuto", ["yes", "no", "yes"], "Kabutops"),

    # Rock / Flying
    ("family_1", "Aerodactyl", ["yes"], "Aerodactyl"),

    # Normal
    ("family_1", "Snorlax", ["yes"], "Snorlax"),

    # Dragon
    ("family_3", "Dratini", ["yes", "yes"], "Dratini"),
    ("family_3", "Dratini", ["yes", "no", "yes"], "Dragonair"),
    ("family_3", "Dratini", ["yes", "no", "no", "yes"], "Dragonite"),

    # Mythical
    ("family_1", "Mew", ["yes"], "Mew"),
]


def build_regular_inputs(family_name, answers):
    """
    Build the complete input sequence for a regular Pokemon.

    The game first asks:
        1. Starter?
        2. Legendary?
        3. Eeveelution?

    All regular Pokemon answer 'no' to those questions.

    Then we answer 'no' to every family until reaching
    the requested family.
    """

    # Main game questions
    inputs = ["no", "no", "no"]

    # Family order exactly matches pokemon_branch() in Kanto.py.
    family_order = [
        "Caterpie",
        "Weedle",
        "Pidgey",
        "Rattata",
        "Spearow",
        "Ekans",
        "Raichu",
        "Sandshrew",
        "Nidoran Female",
        "Nidoran Male",
        "Clefairy",
        "Vulpix",
        "Jigglypuff",
        "Zubat",
        "Oddish",
        "Paras",
        "Venonat",
        "Diglett",
        "Meowth",
        "Psyduck",
        "Mankey",
        "Growlithe",
        "Poliwag",
        "Abra",
        "Machop",
        "Bellsprout",
        "Tentacool",
        "Geodude",
        "Ponyta",
        "Slowpoke",
        "Magnemite",
        "Farfetch'd",
        "Doduo",
        "Seel",
        "Grimer",
        "Shellder",
        "Gastly",
        "Onix",
        "Drowzee",
        "Krabby",
        "Voltorb",
        "Exeggcute",
        "Cubone",
        "Hitmonlee",
        "Hitmonchan",
        "Lickitung",
        "Koffing",
        "Rhyhorn",
        "Chansey",
        "Tangela",
        "Kangaskhan",
        "Horsea",
        "Goldeen",
        "Staryu",
        "Mr. Mime",
        "Scyther",
        "Jynx",
        "Electabuzz",
        "Magmar",
        "Pinsir",
        "Tauros",
        "Magikarp",
        "Lapras",
        "Ditto",
        "Eevee",
        "Porygon",
        "Omanyte",
        "Kabuto",
        "Aerodactyl",
        "Snorlax",
        "Dratini",
        "Mew",
    ]

    target_index = family_order.index(family_name)

    # Answer "no" to every family before the target.
    inputs.extend(["no"] * target_index)

    # Answer "yes" to the target family.
    inputs.extend(answers)

    return inputs


@pytest.mark.parametrize(
    "family_type, family_name, answers, pokemon",
    REGULAR_POKEMON,
)
def test_every_regular_kanto_pokemon(
    family_type,
    family_name,
    answers,
    pokemon,
):
    inputs = build_regular_inputs(family_name, answers)
    assert_pokemon(inputs, pokemon)


# ============================================================
# REGULAR BRANCH FAILURE PATHS
# ============================================================


def test_regular_branch_unknown_pokemon():
    """
    All regular families are rejected.
    The game should reach the final not_exist() branch.
    """

    inputs = [
        "no",  # Not starter
        "no",  # Not legendary
        "no",  # Not Eeveelution
    ]

    # There are 73 regular families in pokemon_branch().
    inputs.extend(["no"] * 73)

    result = run_game(inputs)

    assert result.returncode == 0
    assert "This Pokemon doesn't exist in the 151 Kanto Pokemon." in result.stdout


# ============================================================
# FAMILY HELPER NEGATIVE PATHS
# ============================================================


@pytest.mark.parametrize(
    "family_answers",
    [
        # family_1
        ["yes", "no"],

        # family_2
        ["yes", "no", "no"],

        # family_3
        ["yes", "no", "no", "no"],
    ],
)
def test_family_can_reach_not_exist(family_answers):
    """
    Verify that a family branch can reach not_exist()
    when none of its listed Pokemon matches.
    """

    # Use the Caterpie branch because it is the first regular family.
    inputs = [
        "no",  # Not starter
        "no",  # Not legendary
        "no",  # Not Eeveelution
        *family_answers,
    ]

    result = run_game(inputs)

    assert result.returncode == 0
    assert "This Pokemon doesn't exist in the 151 Kanto Pokemon." in result.stdout


# ============================================================
# PROGRAM EXECUTION
# ============================================================


def test_kanto_file_exists():
    """Kanto.py must exist beside the test file."""
    assert KANTO_FILE.exists()


def test_kanto_program_starts_successfully():
    """
    Basic smoke test: the program should start and accept input
    without crashing.
    """

    result = run_game([
        "yes",
        "yes",
    ])

    assert result.returncode == 0
    assert "Think of a Pokemon!" in result.stdout


# ============================================================
# END-TO-END TEST
# ============================================================


def test_complete_pikachu_game_flow():
    """
    Complete end-to-end test of the shortest successful path.
    """

    result = run_game([
        "yes",
        "yes",
    ])

    assert result.returncode == 0
    assert "Think of a Pokemon!" in result.stdout
    assert "It's Pikachu!" in result.stdout