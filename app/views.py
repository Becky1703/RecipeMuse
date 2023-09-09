from flask import Blueprint, render_template, request, redirect, flash, url_for
import requests
from urllib.parse import unquote
from flask_login import  current_user, login_required
from .models import db, User, Recipe, SavedRecipe

views = Blueprint('views', __name__)

#My Spoonacular API Key
API_KEY = "5a3a0133ba904a66b9e3a9fa055e52aa"

#Defines route for the home page
@views.route('/', methods=['GET'], strict_slashes=True)
def index():
    """ Renders the index page of the app as a welcome page"""
    #renders the home page with empty recipe list
    return render_template('index.html')

#Defines the main route for the app
@views.route('/search', methods=['GET', 'POST'], strict_slashes=True)
def search():
    """ Implements a search function using POST method """
    if request.method == 'POST':
        #Gets the search query from the form
        query = request.form.get('search_query', '')
        #Gets the recipes from the Spoonacular API
        recipes = get_recipes(query)
        #Renders the home page with the recipes
        return render_template('search.html', recipes=recipes, search_query=query) 

    #if the request method is GET or no form was submitted
    search_query = request.args.get('search_query', '')
    decoded_search_query = unquote(search_query)

    #Perform a search for recipes with the search query
    recipes = get_recipes(decoded_search_query)

    #Renders the home page with the recipes
    return render_template('search.html', recipes=recipes, search_query=decoded_search_query) 

#Function to get recipes from the Spoonacular API
def get_recipes(query):     
    """ Sends a GET request to the Spoonacular API to retrieve the recipe data stored in
     the API """
    url = f"https://api.spoonacular.com/recipes/complexSearch"
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': '10',
        'instructionsRequired': 'True',
        'addRecipeInformation': 'True',
        'fillIngredients': 'True'
    }
    #Sends the request and returns the response
    response = requests.get(url, params=params)

    #If the API call doesnt return an Error
    if response.status_code == 200:
        #Parse the API response as data
        data = response.json()
        #Return list of recipes
        return data['results']
    #if the API call returns an Error
    return []

#Route to view a specific recipe with a given recipe ID
@views.route('/recipe/<int:recipe_id>', methods=['GET', 'POST'], strict_slashes=True)
def recipe(recipe_id):
    """ Implements viewing recipe and displaying recipe details """
    search_query = request.args.get('search_query', '')
    
    if request.method == 'POST':
        if current_user.is_authenticated:
           #Build url using the specific recipe ID
           url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
           params = {
                'apiKey': API_KEY,
           }
           #Send GET request to the Spoonacular API to get the recipe information
           response = requests.get(url, params=params)

           if response.status_code == 200:
               #Parses the API response as data
               recipe_data = response.json()
               
               new_recipe = Recipe(
                   name=recipe_data['title'],
                   ingredients=", ".join(ingredient['name'] for ingredient in recipe_data['extendedIngredients']),
                   instructions=recipe_data['instructions'],
                   image_url=recipe_data['image'],
                   user_id=current_user.id
                )

               #Add the recipe to the current user's list of saved recipes
               db.session.add(new_recipe)
               db.session.commit()

               flash('Recipe saved successfully!', 'success')
               return redirect(url_for('views.saved_recipes', recipe_id=recipe_id))
           else:
               flash("Failed to save the recipe. Please try again", "error")
               #Redirect to the recipe page
               return redirect(url_for('views.recipe', recipe_id=recipe_id))
        else:
            flash("You need to be logged in to save recipes.", "info")
            return redirect(url_for('auth.login'))
        
    #Handles GET request
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params = {'apiKey': API_KEY}
    response = requests.get(url, params=params)

    #If the API call doesnt return an Error
    if response.status_code == 200:
        #Parse the API response as data
        recipe = response.json()
        return render_template('view_recipe.html', recipe=recipe, search_query=search_query)
    return "Recipe not found", 404


@views.route('/saved_recipes', methods=['GET'], strict_slashes=True)
@login_required
def saved_recipes():
    """ Fetches all the recipes from the current user's saved recipes """
    saved_recipes = Recipe.query.filter_by(user_id=current_user.id).all()

    if not saved_recipes:
        flash("You have no saved recipes.", 'no_saved_recipes')

    return render_template('saved_recipes.html', saved_recipes=saved_recipes)

@views.route('/delete_recipe/<int:recipe_id>', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    """ Implements deleting a saved recipe """
    recipe = Recipe.query.get_or_404(recipe_id)

    # Check if the recipe belongs to the current user
    if recipe.user_id == current_user.id:
        db.session.delete(recipe)
        db.session.commit()
        flash('Recipe deleted successfully!', 'success')
    else:
        flash('You can only delete your own recipes.', 'error')

    return redirect(url_for('views.saved_recipes'))

