from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
"""
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |

| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |

"""

item_pricing = {
    "A": {"price": 50, "bundles": [(5, 200), (3, 130), ], },
    "B": {"price": 30, "bundles": [(2, 45), ], },
    "C": {"price": 20, "bundles": [], },
    "D": {"price": 15, "bundles": [], },
    "E": {"price": 40, "bundles": [], "free_item": [(2, "B")]},
    "F": {"price": 10, "bundles": [(3, 20)], },
    "G": {"price": 20, "bundles": [], },
    "H": {"price": 10, "bundles": [(10, 80), (5, 45)], },
    "I": {"price": 35, "bundles": [], },
    "J": {"price": 60, "bundles": [], },
    "K": {"price": 80, "bundles": [(2, 150)], },
    "L": {"price": 90, "bundles": [], },
    "M": {"price": 15, "bundles": [], },
    "N": {"price": 40, "bundles": [], "free_item": [(3, "M")]},
    "O": {"price": 10, "bundles": [], },
    "P": {"price": 50, "bundles": [(5, 200)], }, "Q": {"price": 30, "bundles": [(3, 80)], },
    "R": {"price": 50, "free_item": [(3, "Q")], },
    "S": {"price": 30, "bundles": [], },
    "T": {"price": 20, "bundles": [], },
    "U": {"price": 40, "bundles": [(3, 80)], },
    "V": {"price": 50, "bundles": [(3, 130), (2, 90)], },
    "W": {"price": 20, "bundles": [], },
    "X": {"price": 90, "bundles": [], }, "Y": {"price": 10, "bundles": [], },
    "Z": {"price": 50, "bundles": [], },
}


def checkout(skus):
    basket = defaultdict(int)
    if not isinstance(skus, str):
        return -1
    for item in skus:
        if item not in "ABCDEF":
            return -1
        basket[item] += 1

    price = 0
    e_values = basket["E"]
    for key, value in basket.items():

        if key == "C":
            price += value * 20
        elif key == "E":
            price += value * 40
        elif key == "F":
            offer, value = divmod(value, 3)
            price += offer * 2 * 10 + value * 10
        elif key == "D":
            price += value * 15
        elif key == "A":
            offer1, value = divmod(value, 5)
            offer2, value = divmod(value, 3)
            price += offer1 * 200 + offer2 * 130 + value * 50
        elif key == "B":
            value = max(0, value - e_values // 2)
            offer, value = divmod(value, 2)
            price += offer * 45 + value * 30

    return price


