from flask import render_template, redirect, request, session, flash


from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route('/dashboard')
def dashboard():
    if "uuid" not in session:
        return redirect('/')
    
    dict = {'id': session['uuid']}

    return render_template('dashboard.html', logged_in = User.get_id(dict), all_recipes = Recipe.get_all())



#The two routes to fill in and create a recipe
@app.route('/recipes/new')
def new_recipe():
    if "uuid" not in session:
        return redirect ('/')

    return render_template('new_recipe.html', logged_in = User.get_id({'id': session['uuid']}))


@app.route('/recipes/create', methods = ['POST'])
def create_recipe():
    if not Recipe.valid_recipe(request.form):
        return redirect('/recipes/new')

    post_data = {
        **request.form,
        'user_id': session['uuid']
    }

    Recipe.create(post_data)

    return redirect('/dashboard')



#View the specific recipe selected
@app.route('/recipes/view/<int:id>')
def view_recipe(id):
    if 'uuid' not in session:
        return redirect('/')

    dict_user = {'id': session['uuid']}
    dict = {'id': id}

    return render_template('view_recipe.html', logged_in = User.get_id(dict_user), recipe = Recipe.get_one(dict))



#The two routes to edit the recipe and then update it
@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'uuid' not in session:
        return redirect('/')

    dict_user = {'id': session['uuid']}
    dict = {'id': id}

    return render_template('edit_recipe.html', logged_in = User.get_id(dict_user), recipe = Recipe.get_one(dict))


@app.route('/recipes/update/<int:id>', methods = ['POST'])
def update_recipe(id):
    if not Recipe.valid_recipe(request.form):
        return redirect(f'/recipes/edit/{id}') #REMEMBER THIS TOMORROW. F STRING DUDE
    
    post_data = {
        **request.form,
        'id': id,
        'user_id': session['uuid']
    }

    Recipe.update(post_data)

    return redirect('/dashboard')


#Deletes a specific recipe
@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    
    dict = {'id': id}
    Recipe.delete(dict)

    return redirect('/dashboard')