from collections import defaultdict
import string

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
    "P": {"price": 50, "bundles": [(5, 200)], },
    "Q": {"price": 30, "bundles": [(3, 80)], },
    "R": {"price": 50, "bundles": [], "free_item": [(3, "Q")], },
    "S": {"price": 30, "bundles": [], },
    "T": {"price": 20, "bundles": [], },
    "U": {"price": 40, "bundles": [(3, 80)], },
    "V": {"price": 50, "bundles": [(3, 130), (2, 90)], },
    "W": {"price": 20, "bundles": [], },
    "X": {"price": 90, "bundles": [], },
    "Y": {"price": 10, "bundles": [], },
    "Z": {"price": 50, "bundles": [], },
}


def checkout(skus):
    basket = defaultdict(int)
    if not isinstance(skus, str):
        return -1
    for item in skus:
        if item not in string.ascii_uppercase:
            return -1
        basket[item] += 1

    price = 0

    for item in string.ascii_uppercase[::-1]:
        value = basket[item]
        if value <= 0:
            continue
        pricing_info = item_pricing[item]

        free_items = pricing_info.get("free_item", [])
        for free_count, item_name in free_items:
            basket[item_name] -= value // free_count
        for bundle_count, bundle_price in pricing_info.get("bundles", []):
            offer, value = divmod(value, bundle_count)
            price += offer * bundle_price
        price += value * pricing_info["price"]

    return price




