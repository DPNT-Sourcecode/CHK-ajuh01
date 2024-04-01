from collections import defaultdict
import string

# noinspection PyUnusedLocal
# skus = unicode string


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
    "K": {"price": 70, "bundles": [(2, 120)], },
    "L": {"price": 90, "bundles": [], },
    "M": {"price": 15, "bundles": [], },
    "N": {"price": 40, "bundles": [], "free_item": [(3, "M")]},
    "O": {"price": 10, "bundles": [], },
    "P": {"price": 50, "bundles": [(5, 200)], },
    "Q": {"price": 30, "bundles": [(3, 80)], },
    "R": {"price": 50, "bundles": [], "free_item": [(3, "Q")], },
    "S": {"price": 20, "bundles": [], },
    "T": {"price": 20, "bundles": [], },
    "U": {"price": 40, "bundles": [(4, 120)], },
    "V": {"price": 50, "bundles": [(3, 130), (2, 90)], },
    "W": {"price": 20, "bundles": [], },
    "X": {"price": 17, "bundles": [], },
    "Y": {"price": 20, "bundles": [], },
    "Z": {"price": 21, "bundles": [], },
}

group_discounts = {"group": ["Z", "Y", "S", "T", "X", ], "price": 45}


def substract_group_discount(basket):
    all_prices = []
    for item in group_discounts["group"]:
        basket_count = basket[item]
        item_price = item_pricing[item]["price"]
        for _ in range(basket_count):
            all_prices.append(item_price)
    all_prices.sort(reverse=True)
    n = len(all_prices) // 3
    return - sum(all_prices[:n * 3]) + group_discounts["price"] * n


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

    price += substract_group_discount(basket)

    return price

