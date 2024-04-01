from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_ABC(self):
        assert checkout_solution.checkout("ABC") == 100

    def test_checkout_offer(self):
        assert checkout_solution.checkout("ABBC") == 115

    def test_checkout_offer_2(self):
        assert checkout_solution.checkout("AABBCD") == 180
