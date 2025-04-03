# Gie Game
import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

# Dictionary to represent the dice art
dice_art = {
    1: (
        "┌─────┐",
        "│     │",
        "│  ●  │",
        "│     │",
        "└─────┘"
    ),
    2: (
        "┌─────┐",
        "│●    │",
        "│     │",
        "│    ●│",
        "└─────┘"
    ),
    3: (
        "┌─────┐",
        "│●    │",
        "│  ●  │",
        "│    ●│",
        "└─────┘"
    ),
    4: (
        "┌─────┐",
        "│●   ●│",
        "│     │",
        "│●   ●│",
        "└─────┘"
    ),
    5: (
        "┌─────┐",
        "│●   ●│",
        "│  ●  │",
        "│●   ●│",
        "└─────┘"
    ),
    6: (
        "┌─────┐",
        "│●   ●│",
        "│●   ●│",
        "│●   ●│",
        "└─────┘"
    )
}

dice = []
total = 0
num_of_dice = int(input("How many dice do you want to roll? (1-6): "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)
# ┌─────┐
# │●   ●│
# │  ●  │
# │●   ●│
# └─────┘
# ┌─────┐
# │●    │
# │  ●  │
# │    ●│
# └─────┘

# Print the dice art sing one line
for line in range(5):
    for die in range(num_of_dice):
        print(dice_art.get(dice[die])[line], end=" ")
    print()

for die in dice:
    total += die
print(f"Total: {total}")
