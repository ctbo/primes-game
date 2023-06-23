import subprocess


symbols_unicode = {
    2: "1F34E",
    3: "1FAD0",
    5: "1F34C", # banana; tangerine: "1F34A",
    7: "1F951",
    11: "1F424",
    13: "1F416-bo",
    17: "1F411-bo",
    19: "1F40E",
    23: "1F419",
    29: "1F980",
    31: "1F42C", # dolphin. spouting-whale: "1F433",
    37: "1F41F", # tropical-fish: "1F420",
    41: "1F40A", # crocodile. "1F438", # frog. lizard: "1F98E",
    43: "1F422",
    47: "1F40D",
    53: "1F418-bo",
    59: "1F98F", # rhino. zebra: "1F993",
    61: "1F42A",
    67: "1F992",
    71: "1F41E", # lady-beetle. cockroach: "1FAB3",
    73: "1F41D-bo", # bee. beetle: "1FAB2",
    79: "1F98B", # butterfly. cricket: "1F997",
    83: "1F996",
    89: "1F995",
    97: "1F4A9"
}

for prime, filename in symbols_unicode.items():
    subprocess.run(f"cairosvg emoji_u{filename.lower()}.svg -s 0.5 -o {prime}.eps", shell=True)
