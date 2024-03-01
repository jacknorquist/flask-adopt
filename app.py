"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def show_homepage():
    """index home page."""
    pets = Pet.query.all()
    return render_template("homepage.html", pets=pets)




@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """add pet info; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        # do stuff with data/insert to db
        print(available, "osihdsipdghsdoighsidoghisodghiosdghoisdghsiodgh")
        pet = Pet(name = name,
                         species = species,
                         photo_url=photo_url,
                         age=age,
                         notes=notes,
                         available=available)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template(
            "add-pet.html", form=form)
