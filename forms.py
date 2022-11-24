from flask_wtf import FlaskForm
from wtforms import DecimalField,StringField, SelectField
from wtforms.validators import DataRequired

class ShellForm(FlaskForm):

    P = DecimalField('P', validators = [DataRequired()])
    Dvn = DecimalField('Dvn', validators = [DataRequired()])
    T = DecimalField('T', validators = [DataRequired()])
    S = DecimalField('S', validators = [DataRequired()])
    phi = DecimalField('phi', validators = [DataRequired()])
    C = DecimalField('C', validators = [DataRequired()])
    steel = SelectField('steel',
            choices=[('09Г2С', '09Г2С'),('Ст3', 'Ст3')],
            validators = [DataRequired()])


    