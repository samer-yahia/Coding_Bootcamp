from mysqlconnection import connectToMySQL

class User:
    # Data is a dictionary that contains all of the data from a row in the database
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create(cls, data):
        query = """INSERT INTO users (first_name, last_name, email) 
                VALUES (%(first_name)s, %(last_name)s, %(email)s);
                """
        user_id = connectToMySQL("users_schema").query_db(query, data)
        return user_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL("users_schema").query_db(query)
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        return one_user

