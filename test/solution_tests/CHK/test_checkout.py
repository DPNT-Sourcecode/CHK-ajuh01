from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_ABC(self):
        assert checkout_solution.checkout("ABC") == 100

    def test_checkout_offer(self):
        assert checkout_solution.checkout("ABBC") == 115

    def test_checkout_offer_2(self):
        assert checkout_solution.checkout("AABBCD") == 180

    def test_checkout_offer_4A(self):
        assert checkout_solution.checkout("AAAA") == 180

    def test_checkout_offer_8A(self):
        assert checkout_solution.checkout("AAAAAAAA") == 330

    def test_checkout_offer_double_E(self):
        assert checkout_solution.checkout("AABBEE") == 100 + 30 + 80

    def test_checkout_offer_double_F(self):
        assert checkout_solution.checkout("FFF") == 20

    def test_checkout_offer_double_U(self):
        assert checkout_solution.checkout("UUU") == 120

    def test_checkout_offer_7F(self):
        assert checkout_solution.checkout("FFFFFFF") == 50

    def test_checkout_group_discount(self):
        assert checkout_solution.checkout("STX") == 45

    def test_checkout_group_discount_favor(self):
        assert checkout_solution.checkout("STXZ") == 45 + 17

