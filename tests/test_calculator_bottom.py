from calculator import ElepticBottom
import pytest


@pytest.fixture()
def bt():
    bt = ElepticBottom()
    bt.set_P(1)
    bt.set_T(200)
    bt.set_Dvn(309)
    bt.set_S(8)
    bt.set_C(3)
    bt.set_phi(1)
    bt.set_steel('09Г2С')
    bt.set_H(81.25)
    return bt

def test_check_attribute(bt):
    bt.check_attributes()
    assert True
    

def test_check_attribute_2(bt):
    with pytest.raises(AttributeError) as exception:
        bt.set_P(None)
        bt.check_attributes()
    assert 'Один из параметров не назначен' in str(exception.value) 
    
def test_check_attribute_negative(bt):
    with pytest.raises(ValueError) as exception:
        bt.set_T(-100)
        bt.check_attributes()
    assert 'T < 0' in str(exception.value) 

def test_top_radius(bt):
    assert bt.calc_top_radius() == 293.79

def test_calculate_Sr(bt):
    assert bt.calculate_Sr() == 0.89

def test_calculate_unreinforced_hole(bt):
    assert bt.calculate_unreinforced_hole() == 522

def test_calculate_pressure(bt):
    assert bt.calculate_max_pressure() == 5.57

