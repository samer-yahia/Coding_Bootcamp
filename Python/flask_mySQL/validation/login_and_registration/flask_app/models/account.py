from flask import flash
from flask_bcrypt import Bcrypt
import re

from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

bcrypt = Bcrypt(app)

class Account:
    schema = "login_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO accounts (first-name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        
        return connectToMySQL(cls.schema).query_db(query, data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM accounts;"
        results = coonectToMySQL(cls.schema).query_db(query)

        accounts = []
        for row in results:
            accounts.append(cls.row)
        
        return accounts


    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM accounts WHERE email = %(email)s;"
        results = coonectToMySQL(cls.schema).query_db(query, data)

        if len(results) < 1:
            return False

        return cls(results[0])


    @classmethod
    def get_id(cls, data):
        query = "SELECT * FROM accounts WHERE id = %(id)s;"
        results = coonectToMySQL(cls.schema).query_db(query, data)

        return cls(results[0])


    @staticmethod
    def valid_register(post_data):
        is_valid = True

        if len(post_data['first_name']) < 2:
            flash("First name must be longer than 2 characters")
            is_valid = False

        if len(post_data['last_name']) < 2:
            flash("Last name must be longer than 2 characters")
            is_valid = False

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']): 
            flash("Invalid email address!")
            is_valid = False
        elif User.get_email({'email': post_data['email']}):
            flash("Email is already in use.")
            is_valid = False

        if len(post_data['password']) < 8:
            flash('Password must be at least 8 characters long')
            is_valid = False
        elif post_data['password'] != post_data['confirm']:
            flash('Passwords must match')
            is_valid = False

        return is_valid


    @staticmethod
    def login_validate(post_data):
        user = Account.get_email({"email": post_data['email']}) # Ask why are we doing this here as dictionary

        if not user:
            flash("Invalid Credententials")
            return False

        if not bcrpt.check_passowrd_hash(user.password, post_data['password']):
            flash('Invalid Credentials')
            return False
        
        return True




