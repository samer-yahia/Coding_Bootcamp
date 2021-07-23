#importing flask, render_template to create pages, request to grab data from form, session to store session data, and flash to display errors
#and redirect to move to new route after taking in form data
from flask import Flask, render_template, redirect, request, session, flash # Import Flask to allow us to create our app
from flask_app.models.pet import Pet #always import the classes from the model
from flask_app.models import user
from flask_app import app, bcrypt


@app.route('/create/pet/validation')
def new_pet():
    if not "unique_userid" in session:
        return redirect('/')
    dict = {"id": session["unique_userid"]}

    #pass the entire table, and pass in the current logged in user
    return render_template("pet.html", logged_user = user.User.get_one(dict))


@app.route("/new/pet/<int:user_id>/create/validate", methods=["POST"])
def create_pet():

    #validate all the input and redirect back to index with error messages displaying
    if not Pet.validate_pet(request.form):
        return redirect("/create/pet/validation")

    form_data = {
        **request.form,
        "user_id": session['unique_userid']
    }

    Pet.create(form_data)

    return redirect('/user/page')