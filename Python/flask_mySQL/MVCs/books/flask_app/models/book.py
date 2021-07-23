from flask_app.config.mysqlconnection import MySQLConnection

from flask_app.models import author


class Book:
    self.id = data['id']
    self.title = data['title']
    self.num_of_pages = data['num_of_pages']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']


    @classmethod
    def create(cls, data):
        pass


    @classmethod
    def get_all(cls):
        pass


    @classmethod
    def get_one(cls, data):
        pass


    @classmethod
    def update(cls, data):
        pass


    @classmethod
    def delete(cls, data):
        pass