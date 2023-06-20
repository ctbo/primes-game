import subprocess


symbols_unicode = {
    2: "1F34E-bo",
    3: "1FAD0-bo",
    5: "1F34C-bo", # banana; tangerine: "1F34A",
    7: "1F951-bo",
    11: "1F424-bo", # chick
    13: "1F416-bo",
    17: "1F411-bo", # sheep
    19: "1F40E-bo",
    23: "1F419-bo",
    29: "1F980-bo",
    31: "1F42C-bo", # dolphin. spouting-whale: "1F433",
    37: "1F41F-bo", # tropical-fish: "1F420",
    41: "1F40A-bo", # crocodile. "1F438", # frog. lizard: "1F98E",
    43: "1F422-bo",
    47: "1F40D-bo",
    53: "1F418-bo",
    59: "1F98F-bo", # rhino. zebra: "1F993",
    61: "1F42A-bo",
    67: "1F992-bo",
    71: "1F41E-bo", # lady-beetle. cockroach: "1FAB3",
    73: "1F41D-bo", # bee. beetle: "1FAB2",
    79: "1F98B-bo", # butterfly. cricket: "1F997",
    83: "1F996-bo",
    89: "1F995-bo",
    97: "1F4A9-bo"
}

for prime, filename in symbols_unicode.items():
    subprocess.run(f"cairosvg emoji_u{filename.lower()}.svg -s 0.5 -o {prime}.eps", shell=True)
