from calculator import Shell
import pytest

@pytest.fixture()
def shell():
    sh = Shell()
    sh.set_P(1)
    sh.set_T(200)
    sh.set_Dvn(414)
    sh.set_steel('09Г2С')
    sh.set_S(6)
    sh.set_C(1.8)
    sh.set_phi(0.9)    
    return sh

def test_check_attribute(shell):
    shell.check_attributes()
    assert True
    

def test_check_attribute_2(shell):
    with pytest.raises(AttributeError) as exception:
        shell.set_P(None)
        shell.check_attributes()
    assert 'Один из параметров не назначен' in str(exception.value) 
    
def test_check_attribute_negative(shell):
    with pytest.raises(ValueError) as exception:
        shell.set_T(-100)
        shell.check_attributes()
    assert 'T < 0' in str(exception.value) 

def test_calculate_Sr(shell):
    assert shell.calculate_Sr() == 1.40

def test_calculate_unreinforced_hole(shell):
    assert shell.calculate_unreinforced_hole() == 17

def test_calculate_k_zap(shell):
    assert shell.calculate_k_zap() == 1.88

def test_calculate_pressure(shell):
    assert shell.calculate_max_pressure() == 2.98

