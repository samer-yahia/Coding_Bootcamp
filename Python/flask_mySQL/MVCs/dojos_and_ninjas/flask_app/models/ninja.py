from flask_app.config.mysqlconnection import connectToMySQL


from flask_app.models import dojo # Pulling the object from this line

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        # self.dojo_id = data['dojo_id']
        if "dojo_id" in data:
            self.dojo = dojo.Dojo.get_one({'id': data['dojo_id']})
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create(cls, data):
        query = """INSERT INTO ninjas (dojo_id, first_name, last_name, age) 
                VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);
                """
        dojo_id = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return dojo_id


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        all_ninjas = []
        for row in results:
            all_ninjas.append(cls(row))
        return all_ninjas


    @classmethod
    def get_one(cls, data):
        pass


    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass
