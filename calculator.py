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
        if None in self.__dict__.values():                            # Проверка на то, что все параметры заданы 
            raise AttributeError('Один из параметров не назначен')
        for key, value in self.__dict__.items():
            if key == '_steel':
                continue
            if float(value) < 0: # Проверка на то, что все параметры положительны. 
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
        numerator = self._P * self._Dvn                                   #ГОСТ 34233.2 (5.3.1.1)
        denominator = 2*steel_ultimate_strength*self._phi - self._P
        self.Sr = round(numerator/denominator,2)
        return self.Sr 

    def calculate_unreinforced_hole(self): # ГОСТ 342233.3-2017 5.3.1.1 (26)
        self.unreinforced_hole = 2*((self._S-self._C)/self.calculate_Sr()-0.8)*sqrt(
            self._Dvn * (self._S-self._C)) 
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
    def __init__(self) -> None:
        super().__init__()
        self.H = None

    def set_H(self, H):
        self.H = H
    
    def check_attributes(self):
        super().check_attributes()
        if self._ratio_to_check > 0.1 or self._ratio_to_check < 0.002: #ГОСТ 34233.2 (6.2.1)
            raise AttributeError('Размеры не по ГОСТ')
        logging.debug(f'Attributes:\n{self.__dict__}')

    def calc_top_radius(self):
        r = self._Dvn**2/(4 * self.H)
        return round(r, 2)
    
    def calculate_Sr(self): # Возвращает расчетную толщину стенки
        self.steel_ultimate_strength = self.us.get_ultimate_strength(
            steel = self._steel,
            t = self._T)
        logging.debug(f'sigma - {self.steel_ultimate_strength}')
        numerator = self._P * self.calc_top_radius()                               #ГОСТ 34233.2 6.3.1.1
        denominator = 2*self.steel_ultimate_strength*self._phi - 0.5*self._P
        self.Sr = round(numerator/denominator,2)
        return self.Sr 


