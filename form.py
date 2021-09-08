from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,  SelectField, BooleanField
from wtforms.validators import InputRequired, URL, Optional, NumberRange, Length

sp=['Cat','Dog','Procupine']
class AddPetForm(FlaskForm):
    '''add pet form'''

    pet_name=StringField("Pet name", validators=[InputRequired()])

    species=SelectField("species", choices=[('cat','Cat'),('dog','Dog'),('procupine','Procupine')])
    photo_url=StringField('Photo_url',validators=[URL(), Optional()])
    age=IntegerField('age', validators=[Optional(), NumberRange(min=0,max=30)])
    note=StringField('Note', validators=[Optional(),Length(min=20,message="Please write 20 words at least")])

class EditPetForm(FlaskForm):
    '''form to edit an existing pet'''
    photo_url=StringField('Photo_url',validators=[URL(), Optional()])
    note=StringField('Note', validators=[Optional(),Length(min=20,message="Please write 20 words at least")])
    available = BooleanField("Available?")