from ultimate_strength import UltimateStrength

def test_09G2S():
    us = UltimateStrength()
    assert us.get_ultimate_strength('09Г2С', 175)

def test_St3():
    us = UltimateStrength()
    assert us.get_ultimate_strength('Ст3', 410, thin=False, durability=20) == 65
