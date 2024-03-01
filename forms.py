"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, FileField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL



class AddPetForm(FlaskForm):
    """Pet model."""

    name = StringField("Name", validators=[InputRequired()] )
    species =SelectField("Species",
                         choices=[('cat', 'Cat'),
                                  ('porcupine', 'Porcupine'),
                                  ('dog', 'Dog'),],
                                  validators=[InputRequired()])
    photo_url = StringField("Photo", validators=[Optional(),
                                                 URL()])
    age = SelectField("Age",
                      choices=[('baby', 'Baby'),
                                  ('young', 'Young'),
                                  ('adult', 'Adult'),
                                  ('senior', 'Senior')],
                      validators=[InputRequired()])
    notes = StringField("Notes")
    available = SelectField('available',
                            choices=[(True, "Yes"),
                                      (False,"No")])
