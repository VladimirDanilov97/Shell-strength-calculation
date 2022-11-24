from ultimate_strength import UltimateStrength
import logging
from math import sqrt

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")


class Shell:
    us = UltimateStrength()

    def __init__(self) -> None:
        self.__Dvn = None
        self.__P = None
        self.__T = None
        self.__S = None
        self.__steel = None
        self.__C = None 
        self.__phi = None

    def set_Dvn(self, D):
        self.__Dvn = D
    
    def set_P(self, P):
        self.__P = P

    def set_steel(self, steel_name='09Г2С'):
        self.__steel = steel_name
    
    def set_T(self, T):
        self.__T = T
    
    def set_S(self, S):
        self.__S = S
    
    def get_S(self):
        return self.__S

    def set_C(self, C):
        self.__C = C
    
    def get_C(self):
        return self.__C
    
    def set_phi(self, phi):
        self.__phi = phi

    def check_attributes(self):
        if None in self.__dict__.values():
            raise AttributeError(self.__dict__)

        if self.__Dvn < 0:
            raise ValueError('D < 0')

        self.__ratio_to_check = (self.__S - self.__C)/self.__Dvn

        if self.__Dvn < 200:
            if self.__ratio_to_check > 0.1:
                raise AttributeError('Размеры не по ГОСТ')
        else:
            if self.__ratio_to_check > 0.3:
                raise AttributeError('Размеры не по ГОСТ')
        logging.debug(f'Attributes:\n{self.__dict__}')

    def calculate_Sr(self): # Возвращает расчетную толщину стенки
        steel_ultimate_strength = self.us.get_ultimate_strength(
            steel = self.__steel,
            t = self.__T)
        logging.debug(f'sigma - {steel_ultimate_strength}')
        numerator = self.__P * self.__Dvn                                   #ГОСТ 34233.2 5.3.1.1
        denominator = 2*steel_ultimate_strength*self.__phi - self.__P
        self.Sr = round(numerator/denominator,2)
        return self.Sr 

    def calculate_unreinforced_hole(self): # ГОСТ 342233.3-2017 5.2.8 (24)
        self.unreinforced_hole = 0.4 * sqrt(self.__Dvn*(self.__S - self.__C))
        return round(self.unreinforced_hole, 0)

    def calculate_k_zap(self):
        Sr = self.calculate_Sr()
        return round((self.__S)/(Sr + self.__C), 2)
    
    def calculate_max_pressure(self):
        steel_ultimate_strength = self.us.get_ultimate_strength(
            steel = self.__steel,
            t = self.__T)
        numerator = 2*steel_ultimate_strength*self.__phi*(self.__S - self.__C )
        denominator = self.__Dvn +self.__S - self.__C 
        self.P_max = round(numerator/denominator, 2)
        return self.P_max

class ElepticBottom:
    us = UltimateStrength()

    def __init__(self) -> None:
        self.__Dvn = None
        self.__P = None
        self.__T = None
        self.__S = None
        self.__steel = None
        self.__C = None 
        self.__phi = None

    def calculate_Sr(self): # Возвращает расчетную толщину стенки
        self.steel_ultimate_strength = self.us.get_ultimate_strength(
            steel = self.__steel,
            t = self.__T)
        logging.debug(f'sigma - {self.steel_ultimate_strength}')
        numerator = self.__P * self.__Dvn/2                                   #ГОСТ 34233.2 5.3.1.1
        denominator = 2*self.steel_ultimate_strength*self.__phi - 0.5*self.__P
        self.Sr = round(numerator/denominator,2)
        return self.Sr 

if __name__ == '__main__':

    sh = Shell()
    sh.set_P(1)
    sh.set_T(200)
    sh.set_Dvn(414)
    sh.set_steel('09Г2С')
    sh.set_S(6)
    sh.set_C(1.8)
    sh.set_phi(0.9)    
    sh.check_attributes()
    logging.debug(sh.calculate_Sr())
    logging.debug(sh.calculate_unreinforced_hole())
    logging.debug(sh.calculate_max_pressure())