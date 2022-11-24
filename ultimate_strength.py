from pandas import read_csv
from scipy.interpolate import interp1d
from os import path
from pathlib import Path


class UltimateStrength:
    __df = read_csv(path.join(Path(__file__).parent.resolve(),
                              'constants',
                              'ultimate_strength.csv'), # Таблица составлена по ГОСТ 34233.1-2017 приложение А
                    delimiter=';')
    __temperature = __df['T']
    
    def __init__(self):
        pass

    def get_ultimate_strength(self, steel:str, t, thin=True, durability=10): # durability - в годах (10 или 20 (в таблице 10**5 и 2*10**5 часов)) 
        sign = None                                                          # thin - таблицы имеют по 2 колонки в зависимости от толщины листа       

        if steel == '09Г2С': 
            sign = '>32'
            if thin:
                sign = '<32'
        if steel == 'Ст3':
            sign = '>20'
            if thin:
                sign = '<20'

        ultimate_strength_09G2S = self.__df[f'{steel}{sign}_{durability}']
        interpolated = interp1d(self.__temperature, ultimate_strength_09G2S) # Интерполируем столбцы функцией из scipy
        return interpolated(t) # Возвращается интерполированное значение

    
