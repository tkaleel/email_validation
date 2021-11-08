from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO emails ( email_address, created_at, updated_at ) VALUES ( %(email_address)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('emails_schema').query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('emails_schema').query_db(query)
        emails = []
        for email in results:
            emails.append( cls(email) )
        return emails

    @staticmethod
    def validate_email(data):
        is_valid=True
        if not EMAIL_REGEX.match(data['email_address']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid