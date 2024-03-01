"""Forms for adopt app."""
from flask_wtf import FlaskForm, FileAllowed
from wtforms import StringField, FloatField, FileField, IntegerField, SelectField
from wtforms.validators import InputRequired



class AddPetForm(FlaskForm):
    """Pet."""

    name = StringField("Name", validators=[InputRequired()] )

    species =StringField("Species", validators=[InputRequired()] )
    photo_url = FileField("photo", validators=[FileAllowed(['jpg','jpeg','png'])])


    age = IntegerField("Age", validators=[InputRequired()] )

    notes = StringField("Notes")
    available = SelectField('available',
                            choices=[(True, "Yes"),
                                      (False,"No")])
