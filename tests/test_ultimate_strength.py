from ultimate_strength import UltimateStrength
import numpy as np
def test_09G2S():
    us = UltimateStrength()
    assert us.get_ultimate_strength('09Г2С', 175)

def test_St3_410():
    us = UltimateStrength()
    assert us.get_ultimate_strength('Ст3', 410, thin=False, durability=20) == 65

def test_St3_430():
    us = UltimateStrength()
    assert us.get_ultimate_strength('Ст3', 430, thin=False, durability=20) == 57

def test_09G2S_440():
    us = UltimateStrength()
    assert us.get_ultimate_strength('09Г2С', 440, thin=True, durability=20) == 66


