from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField
from wtforms.validators import DataRequired


class ShellForm(FlaskForm): # Добавить валидатор положительного значения! # Добавить валидатор S > C
    P = DecimalField('P', validators = [DataRequired()]) # Давление внутреннее 
    Dvn = DecimalField('Dvn', validators = [DataRequired()]) # Диаметр внутренний
    T = DecimalField('T', validators = [DataRequired()]) # Расчетная температура
    S = DecimalField('S', validators = [DataRequired()]) # Толщина стенки
    phi = DecimalField('phi', validators = [DataRequired()]) # Коэффициент прочности сварного шва 
    C = DecimalField('C', validators = [DataRequired()]) # Суммарна прибавка к толщине стенки
    steel = SelectField('steel',
            choices=[('09Г2С', '09Г2С'),('Ст3', 'Ст3')],
            validators = [DataRequired()]) # Материал 


class BottomForm(ShellForm):
    H = DecimalField('C', validators = [DataRequired()]) # Высота днища

    