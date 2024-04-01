from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string


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
