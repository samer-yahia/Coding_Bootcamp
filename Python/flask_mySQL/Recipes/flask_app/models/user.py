from flask import flash
from flask_bcrypt import Bcrypt
import re

from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import recipe

bcrypt = Bcrypt(app)


class User:
    schema = 'recipes_schema'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []


    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """

        return connectToMySQL(cls.schema).query_db(query, data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.schema).query_db(query)

        users = []
        for row in results:
            users.append(cls(row))

        return users


    @classmethod
    def get_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(cls.schema).query_db(query, data)

        if len(results) < 1:
            return False

        return cls(results[0])

    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(cls.schema).query_db(query, data)

        if len(results) < 1:
            return False

        return cls(results[0])

    # Look at this again before the exam to fully understand what the for loop is used for
    @classmethod 
    def join_by_id(cls, data):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = receipes.user_id WHERE id = %(id)s"
        results = connectToMySQL(cls.schema).query_db(query, data)
        user = cls(results[0])

        if results[0]['recipes.id'] != None:
            for row in results:
                rowData = {
                **row,
                'id': row['recipes.id'],
                'user_id': False
            }
            user.recipes.append(recipe.Recipe(rowData))

        return user

    @staticmethod
    def valid_register(post_data):
        is_valid = True

        if len(post_data['first_name']) < 2:
            flash("First name must be longer than 2 characters", "first_name")
            is_valid = False

        if len(post_data['last_name']) < 2:
            flash("Last name must be longer than 2 characters", "last_name")
            is_valid = False

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']): 
            flash("Invalid email address!", "email")
            is_valid = False
        elif User.get_email({'email': post_data['email']}):
            flash("Email is already in use.", "email")
            is_valid = False

        if len(post_data['password']) < 8:
            flash('Password must be at least 8 characters long', "password")
            is_valid = False
        elif post_data['password'] != post_data['confirm']:
            flash('Passwords must match', "confirm")
            is_valid = False

        return is_valid


    @staticmethod
    def valid_login(post_data):
        user = User.get_email({"email": post_data['email']}) # Ask why are we doing this here as dictionary

        if not user:
            flash("Invalid Credententials", 'login_email')
            return False

        if not bcrypt.check_password_hash(user.password, post_data['password']):
            flash('Invalid Credentials', 'login_password')
            return False
        
        return True




