from ultimate_strength import UltimateStrength
import logging
from math import sqrt

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")

class Part:
    us = UltimateStrength()

    def __init__(self) -> None:
        self._Dvn = None
        self._P = None
        self._T = None
        self._S = None
        self._steel = None
        self._C = None 
        self._phi = None
    
    def set_Dvn(self, D):
        self._Dvn = D
    
    def set_P(self, P):
        self._P = P

    def set_steel(self, steel_name='09Г2С'):
        self._steel = steel_name
    
    def set_T(self, T):
        self._T = T
    
    def set_S(self, S):
        self._S = S
    
    def get_S(self):
        return self._S

    def set_C(self, C):
        self._C = C
    
    def get_C(self):
        return self._C

    def set_phi(self, phi):
        self._phi = phi

    def check_attributes(self):
        if None in self.__dict__.values():
            raise AttributeError('Один из параметров не назначен')
        for key, value in self.__dict__.items():
            if key == '_steel':
                continue
            if float(value) < 0:
                raise ValueError(f'{key} < 0')

        self._ratio_to_check = (self._S - self._C)/self._Dvn

class Shell(Part):
    def __init__(self) -> None:
        super().__init__()
    
    def check_attributes(self):
        super().check_attributes()

        if self._Dvn < 200:
            if self._ratio_to_check > 0.1:
                raise AttributeError('Размеры не по ГОСТ')
        else:
            if self._ratio_to_check > 0.3:
                raise AttributeError('Размеры не по ГОСТ')
        logging.debug(f'Attributes:\n{self.__dict__}')

    def calculate_Sr(self): # Возвращает расчетную толщину стенки
        steel_ultimate_strength = self.us.get_ultimate_strength(
            steel = self._steel,
            t = self._T)
        logging.debug(f'sigma - {steel_ultimate_strength}')
        numerator = self._P * self._Dvn                                   #ГОСТ 34233.2 5.3.1.1
        denominator = 2*steel_ultimate_strength*self._phi - self._P
        self.Sr = round(numerator/denominator,2)
        return self.Sr 

    def calculate_unreinforced_hole(self): # ГОСТ 342233.3-2017 5.2.8 (24)
        self.unreinforced_hole = 0.4 * sqrt(self._Dvn*(self._S - self._C))
        return round(self.unreinforced_hole, 0)

    def calculate_k_zap(self):
        Sr = self.calculate_Sr()
        return round((self._S)/(Sr + self._C), 2)
    
    def calculate_max_pressure(self):
        steel_ultimate_strength = self.us.get_ultimate_strength(
            steel = self._steel,
            t = self._T)
        numerator = 2*steel_ultimate_strength*self._phi*(self._S - self._C )
        denominator = self._Dvn +self._S - self._C 
        self.P_max = round(numerator/denominator, 2)
        return self.P_max

class ElepticBottom(Part):
    us = UltimateStrength()

   
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