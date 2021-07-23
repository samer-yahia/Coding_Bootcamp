from flask import flash

#Ask why app does not go here
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class Recipe:
    schema = 'recipes_schema'

    def __init__(self, data):
        self.id = data['id']

        if data['user_id']:
            self.user = user.User.get_id({'id': data['user_id']})

        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under_30_minutes = data['under_30_minutes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO recipes (user_id, name, description, instruction, under_30_minutes)
        VALUES (%(user_id)s, %(name)s, %(description)s, %(instruction)s, %(under_30_minutes)s);
        """

        return connectToMySQL(cls.schema).query_db(query, data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.schema).query_db(query)

        recipes = []
        for row in results:
            recipes.append(cls(row))

        return recipes


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results = connectToMySQL(cls.schema).query_db(query, data)

        #if the selection does not exist, return false 
        if len(results) < 1:
            return False
        else:
            return cls(results[0])


    @classmethod
    def update(cls, data):
        query = """
            UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, under_30_minutes = %(under_30_minutes)s 
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.schema).query_db(query, data)


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"

        return connectToMySQL(cls.schema).query_db(query, data)


    @staticmethod
    def valid_recipe(post_data):
        is_valid = True

        if len(post_data['name']) < 3:
            flash("Name must be longer than 3 characters", "name")
            is_valid = False

        if len(post_data['description']) < 3:
            flash("Description must be longer than 3 characters", "description")
            is_valid = False
        
        if len(post_data['instruction']) < 3:
            flash("Instruction must be longer than 3 characters", "instruction")
            is_valid = False

        if len(post_data['under_30_minutes']) < 3:
            flash("Must select yes or no", "under_30_minutes")
            is_valid = False

        return is_valid
