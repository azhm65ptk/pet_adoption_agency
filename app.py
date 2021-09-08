from flask import Flask, request, render_template, flash, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import db, connect_db, Pet
from form import AddPetForm, EditPetForm

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home():
    pet=Pet.query.all()
    return render_template('home.html',pet=pet)

@app.route('/add', methods=['GET','POST'])
def add_pet():
    form=AddPetForm()
    if form.validate_on_submit():
        name=form.pet_name.data
        species=form.species.data
        photo_url=form.photo_url.data
        age=form.age.data
        note=form.note.data

        pet=Pet(name=name, species=species, photo_url=photo_url,age=age, notes=note)
        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} added.")
        return redirect('/')
    else:
        return render_template('add_pet_form.html',form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet=Pet.query.get_or_404(pet_id)
    form= EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.note=form.note.data
        pet.available=form.available.data
        pet.photo_url=form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect('/')
    else:

        return render_template('edit_pet_form.html',form=form, pet=pet)
# """return pet info in jason format"""
@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)