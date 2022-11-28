from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField
from wtforms.validators import DataRequired, NumberRange, ValidationError



class ShellForm(FlaskForm): # Добавить валидатор положительного значения! # Добавить валидатор S > C
    
    P = DecimalField('P', validators = [DataRequired(), NumberRange(min=0.01)]) # Давление внутреннее 
    Dvn = DecimalField('Dvn', validators = [DataRequired(), NumberRange(min=0.01)]) # Диаметр внутренний
    T = DecimalField('T', validators = [DataRequired(), NumberRange(min=0.01, max=430)]) # Расчетная температура
    S = DecimalField('S', validators = [DataRequired(), NumberRange(min=0.01)]) # Толщина стенки
    phi = DecimalField('phi', validators = [DataRequired(), NumberRange(min=0.01)]) # Коэффициент прочности сварного шва 
    C = DecimalField('C', validators = [DataRequired(), NumberRange(min=0.01)]) # Суммарна прибавка к толщине стенки
    steel = SelectField('steel',
            choices=[('09Г2С', '09Г2С'),('Ст3', 'Ст3')],
            validators = [DataRequired()]) # Материал 

    
        


class BottomForm(ShellForm):
    H = DecimalField('C', validators = [DataRequired(), NumberRange(min=0.01)]) # Высота днища

    