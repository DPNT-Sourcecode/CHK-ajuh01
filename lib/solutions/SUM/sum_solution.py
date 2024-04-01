# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x < 0 or x > 100:
        raise ValueError("x is not in range")
    if y < 0 or y > 100:
        raise ValueError("y is not in range")
    return x + y

