from flask_app.config.mysqlconnection import connectToMySQL


class Email:
    def __init__(self, data):
        self.id = name['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.password_confirmation = data['password_confirmation']







    import re	# the regex module



    @staticmethod


    def validate_user( user ):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

