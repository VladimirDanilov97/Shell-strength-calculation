from shell import Shell
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

def test_calculate_Sr(shell):
    shell.check_attributes()
    assert shell.calculate_Sr() == 1.40

def test_calculate_unreinforced_hole(shell):
    shell.check_attributes()
    assert shell.calculate_unreinforced_hole() == 17