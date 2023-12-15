from pathlib import Path
import json
import random
import send_code as sc
import string


def _make_call_sign(country):
    prefix_length = random.choice([1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3])
    postfix_length = random.choice([1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3])
    call_sign = ""
    if country.lower() == "usa":
        prefix_length = random.choice([1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3])
        postfix_length = random.choice([1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3])
        first_letter = random.choice(["k", "k", "w", "w" "n", "n", "a"])
        digit = random.choice(string.digits)
        call_sign += first_letter
        for i in range(1, prefix_length):
            char = random.choice(string.ascii_lowercase)
            call_sign += char
        if first_letter == "a" and prefix_length > 1:
            cs = list(call_sign)
            cs[1] = random.choice(string.ascii_lowercase[:12])  # only a-l
            call_sign = "".join(cs)
        call_sign += digit
        for i in range(postfix_length):
            char = random.choice(string.ascii_lowercase)
            call_sign += char
    if country.lower() == "iceland":
        postfix_length = random.choice([1, 2, 2, 2, 2, 2, 2, 3])
        call_sign = "tf"
        digit = random.choice(
            ["1", "2", "3", "3", "3", "3", "3", "3", "3", "4", "5", "6", "7", "8", "9"]
        )
        call_sign += digit
        for i in range(postfix_length):
            char = random.choice(string.ascii_lowercase)
            call_sign += char
        if postfix_length == 3:
            cs = list(call_sign)
            cs[-1] = random.choice(["n", "t", "t"])
            call_sign = "".join(cs)
    return call_sign


def _make_name(country):
    usa_names = [
        "Abel",
        "Adam",
        "Adan",
        "Alan",
        "Aldo",
        "Alec",
        "Amir",
        "Amos",
        "Aram",
        "Ari",
        "Arlo",
        "Arndt",
        "Asa",
        "Axel",
        "Beau",
        "Blaise",
        "Blaine",
        "Boyd",
        "Bram",
        "Brett",
        "Brent",
        "Bryn",
        "Cai",
        "Cain",
        "Carl",
        "Cian",
        "Clark",
        "Claus",
        "Cole",
        "Colm",
        "Craig",
        "Dean",
        "Dion",
        "Eli",
        "Elis",
        "Enzo",
        "Eric",
        "Ernst",
        "Esau",
        "Ezio",
        "Ezra",
        "Euan",
        "Evan",
        "Fulk",
        "Finn",
        "Flynn",
        "Frank",
        "Franz",
        "Gael",
        "Gene",
        "Giles",
        "Glenn",
        "Grant",
        "Greer",
        "Greig",
        "Grey",
        "Guy",
        "Hans",
        "Heath",
        "Hugh",
        "Hugo",
        "Ian",
        "Ioan",
        "Ivan",
        "Ivo",
        "Ivor",
        "Iwan",
        "Jago",
        "Jair",
        "Joah",
        "Joel",
        "Jory",
        "Jude",
        "Kai",
        "Keir",
        "Keith",
        "Kerr",
        "Kurt",
        "Lars",
        "Leif",
        "Lee",
        "Leo",
        "Leon",
        "Lev",
        "Levi",
        "Lex",
        "Liam",
        "Lloyd",
        "Loic",
        "Luke",
        "Luca",
        "Ludo",
        "Mac",
        "Max",
        "Miles",
        "Milo",
        "Neil",
        "Nico",
        "Nils",
        "Noah",
        "Noam",
        "Noel",
        "Otis",
        "Otto",
        "Owen",
        "Rafe",
        "Ralph",
        "Reid",
        "Rex",
        "Rhett",
        "Rhys",
        "Rio",
        "Ross",
        "Saul",
        "Scott",
        "Sean",
        "Seth",
        "Tate",
        "Teo",
        "Theo",
        "Thor",
        "Todd",
        "Urs",
        "Vaughn",
        "Veit",
        "Wolfe",
        "Zeno",
        "Zeus ",
    ]
    icelandic_names = [
        "Alli",
        "Aggi",
        "Alex",
        "Andres",
        "Andri",
        "Anton",
        "Ari",
        "Arnar",
        "Arnor",
        "Aron",
        "Atli",
        "Axel",
        "Agust",
        "Armann",
        "Arni",
        "Asgeir",
        "Asi",
        "Baldur",
        "Baldvin",
        "Benni",
        "Beggi",
        "Biggi",
        "Birkir",
        "Bjarki",
        "Bjarni",
        "Bjoggi",
        "Bjossi",
        "Bragi",
        "Binni",
        "Dadi",
        "Dagur",
        "Danni",
        "David",
        "Eggert",
        "Egill",
        "Einar",
        "Eirikur",
        "Elias",
        "Elvar",
        "Emil",
        "Eythor",
        "Fannar",
        "Finnur",
        "Fridrik",
        "Gardar",
        "Geir",
        "Gisli",
        "Gretar",
        "Gudjon",
        "Gulli",
        "Gummi",
        "Gudni",
        "Gunnar",
        "Gunni",
        "Gylfi",
        "Haffi",
        "Dori",
        "Hannes",
        "Haddi",
        "Haukur",
        "Hakon",
        "Heidar",
        "Heimir",
        "Helgi",
        "Hemmi",
        "Hilmar",
        "Hjalti",
        "Hjalli",
        "Hjortur",
        "Hlynur",
        "Hreinn",
        "Hordur",
        "Ingi",
        "Ingo",
        "Ingvar",
        "Isak",
        "Ivar",
        "Jakob",
        "Jens",
        "Johann",
        "Johannes",
        "Jon",
        "Jonas",
        "Julius",
        "Karl",
        "Kari",
        "Kjartan",
        "Kolbeinn",
        "Kristinn",
        "Kristjan",
        "Kristofer",
        "Larus",
        "Leifur",
        "Magnus",
        "Matti",
        "Oddur",
        "Oli",
        "Omar",
        "Oskar",
        "Pall",
        "Palmi",
        "Petur",
        "Raggi",
        "Reynir",
        "Robert",
        "Runar",
        "Fusi",
        "Siggi",
        "Jonni",
        "Sindri",
        "Skuli",
        "Smari",
        "Snorri",
        "Stefan",
        "Steini",
        "Svavar",
        "Svenni",
        "Sverrir",
        "Saemi",
        "Saevar",
        "Tommi",
        "Trausti",
        "Tryggvi",
        "Valdi",
        "Valli",
        "Valur",
        "Vidar",
        "Vignir",
        "Viktor",
        "Villi",
        "Thor",
        "Thordur",
        "Thorir",
        "Throstur",
        "Orn",
    ]
    if country.lower() == "usa":
        return random.choice(usa_names).lower()
    elif country.lower() == "iceland":
        return random.choice(icelandic_names).lower()


def _make_location(country):
    usa_location = [
        "AL",
        "KY",
        "OH",
        "AK",
        "LA",
        "OK",
        "AZ",
        "ME",
        "OR",
        "AR",
        "MD",
        "PA",
        "AS",
        "MA",
        "PR",
        "CA",
        "MI",
        "RI",
        "CO",
        "MN",
        "SC",
        "CT",
        "MS",
        "SD",
        "DE",
        "MO",
        "TN",
        "DC",
        "MT",
        "TX",
        "FL",
        "NE",
        "TT",
        "GA",
        "NV",
        "UT",
        "GU",
        "NH",
        "VT",
        "HI",
        "NJ",
        "VA",
        "ID",
        "NM",
        "VI",
        "IL",
        "NY",
        "WA",
        "IN",
        "NC",
        "WV",
        "IA",
        "ND",
        "WI",
        "KS",
        "MP",
        "WY",
    ]
    icelandic_location = [
        "reykjavik",
        "reykjavik",
        "reykjavik",
        "reykjavik",
        "reykjavik",
        "reykjavik",
        "akureyri",
        "borgarnes",
        "selfoss",
        "hafnarfjordur",
        "kopavogur",
        "keflavik",
        "seydisfjordur",
    ]
    if country.lower() == "usa":
        return random.choice(usa_location)
    elif country.lower() == "iceland":
        return random.choice(icelandic_location)


def get_persona(country):
    persona = {}
    persona = {
        "call_sign": _make_call_sign(country),
        "name": _make_name(country),
        "qth": _make_location(country),
    }
    return persona


OPERATOR_FILE_NAME = "~/.local_operator.json"


def get_local_persona():
    persona_file = Path(OPERATOR_FILE_NAME).expanduser()
    if persona_file.exists():
        persona = {}
        with open(persona_file, "r") as f:
            persona = json.load(f)
        return persona
    else:
        persona = get_persona("usa")
        with open(persona_file, "w+") as f:
            json.dump(persona, f)
        return persona


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python personas.py <country>")
        sys.exit(1)
    country = sys.argv[1]
    if country.lower() not in ["usa", "iceland"]:
        print("Country must be USA or Iceland")
        sys.exit(1)
    for i in range(100):
        print(get_persona(country))
