import subprocess


symbols_unicode = {
    2: "emoji_u1F99C-bo", # "emoji_u1F426",
    3: "emoji_u1f407-bo",
    5: "frog",
    7: "emoji_u1F408",
    11: "emoji_u1F424",
    13: "emoji_u1F416-bo",
    17: "emoji_u1F411-bo",
    19: "emoji_u1F40E",
    23: "emoji_u1F419",
    29: "emoji_u1F980",
    31: "emoji_u1F42C", # dolphin. spouting-whale: "emoji_u1F433",
    37: "emoji_u1F41F", # tropical-fish: "emoji_u1F420",
    41: "emoji_u1F40A", # crocodile. "emoji_u1F438", # frog. lizard: "emoji_u1F98E",
    43: "emoji_u1F422",
    47: "emoji_u1F40D",
    53: "emoji_u1F418",
    59: "emoji_u1F98F", # rhino. zebra: "emoji_u1F993",
    61: "emoji_u1F42A",
    67: "emoji_u1F992",
    71: "emoji_u1F41E", # lady-beetle. cockroach: "emoji_u1FAB3",
    73: "emoji_u1F41D-bo", # bee. beetle: "emoji_u1FAB2",
    79: "emoji_u1F98B", # butterfly. cricket: "emoji_u1F997",
    83: "emoji_u1F996",
    89: "emoji_u1F995",
    97: "emoji_u1F4A9"
}

for prime, filename in symbols_unicode.items():
    subprocess.run(f"cairosvg {filename.lower()}.svg -s 0.5 -o {prime}.eps", shell=True)
