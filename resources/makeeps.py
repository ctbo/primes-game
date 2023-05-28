import subprocess

symbols = {
    1: "ghost",
    2: "red-apple",
    3: "blueberries",
    5: "tangerine",
    7: "cucumber",
    11: "hatching-chick",
    13: "baby-chick",
    17: "front-facing-baby-chick",
    19: "chicken",
    23: "octopus",
    29: "crab",
    31: "spouting-whale",
    37: "tropical-fish",
    41: "lizard",
    43: "turtle",
    47: "snake",
    53: "elephant",
    59: "zebra",
    61: "camel",
    67: "two-hump-camel",
    71: "cockroach",
    73: "beetle",
    79: "cricket",
    83: "dragon-face",
    89: "sauropod",
    97: "pile-of-poo"
}

for prime, filename in symbols.items():
    subprocess.run(f"convert {filename}.png -background none -flatten EPS3:{prime}.eps", shell=True)
