from database.connection import db_connection
from database.setup import create_tables
from lib.models.book import Book
from lib.models.user import User
from lib.models.bookcheckout import Bookcheckout


def create_user(cursor):
    username = input("Enter user name: ")
    user = User(None)


def main():
    
    create_tables()

if __name__ == "__main__":
    main()
