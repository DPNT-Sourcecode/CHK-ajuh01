
from collections import defaultdict
# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    basket = defaultdict(int)
    if not isinstance(skus, str):
        return -1
    for item in skus:
        if item not in "ABCD":
            return -1
        basket[item] += 1

    price = 0
    for key, value in basket.items():
        if key == "C":
            price += value * 20
        elif key == "D":
            price += value * 15
        elif key == "A":
            offer, value = divmod(value, 3)
            price += offer * 130 + value * 50
        elif key == "B":
            offer, value = divmod(value, 2)
            price += offer * 45 + value * 30
    return price


