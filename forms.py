from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired


class MNISTForm(FlaskForm):
    temp = SelectField(
        'Category',
        choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')


class AttributeForm(FlaskForm):
    collar = SelectField(
        'Collar',
        choices=[('0', 'No'), ('1', 'Yes')]
    )
    gender = SelectField(
        'Gender',
        choices=[('0', 'Male'), ('1', 'Female')],
        validators=[DataRequired()]
    )
    necktie = SelectField(
        'NeckTie',
        choices=[('0', 'No'), ('1', 'Yes')],
        validators=[DataRequired()]
    )
    pattern = SelectField(
        'Pattern',
        choices=[('0', 'Floral'), ('1', 'Graphic'), ('2', 'Plaid'), ('3', 'Solid'), ('4', 'Spot'), ('5', 'Stripe')],
        validators=[DataRequired()]
    )
    placket = SelectField(
        'Placket',
        choices=[('0', 'No'), ('1', 'Yes')],
        validators=[DataRequired()]
    )
    scarf = SelectField(
        'Scarf',
        choices=[('0', 'No'), ('1', 'Yes')],
        validators=[DataRequired()]
    )
    skinexposure = SelectField(
        'Skin Exposure',
        choices=[('0', 'No'), ('1', 'Yes')],
        validators=[DataRequired()]
    )
    category = SelectField(
        'Category',
        choices=[('0', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8')],
        validators=[DataRequired()]
    )
    neckline = SelectField(
        'Neckline',
        choices=[('0', '1'), ('1', '2'), ('2', '3'), ('3', '4')],
        validators=[DataRequired()]
    )
    sleevelength = SelectField(
        'Sleeve Length',
        choices=[('0', '1'), ('1', '2'), ('2', '3')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')

class TrendyForm(FlaskForm):
    img = FileField('Add your image here', [FileAllowed(['jpg','png','svg'])])
    submit = SubmitField('Submit')