from settings import *
import json

# Initializing our database
db = SQLAlchemy(app)


# the class Book will inherit the db.Model of SQLAlchemy
class Book(db.Model):
    __tablename__ = 'books'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    def json(self):
        return {'id': self.id, 'title': self.title,
                'year': self.year, 'genre': self.genre}
        # this method we are defining will convert our output to json

    def add_book(_title, _year, _genre):
        '''function to add book to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our Book constructor
        new_book = Book(title=_title, year=_year, genre=_genre)
        db.session.add(new_book)  # add new book to database session
        db.session.commit()  # commit changes to session

    def get_all_books():
        '''function to get all books in our database'''
        return [Book.json(book) for book in Book.query.all()]

    def get_book(_id):
        '''function to get book using the id of the book as parameter'''
        return [Book.json(Book.query.filter_by(id=_id).first())]
        # Book.json() coverts our output to json
        # the filter_by method filters the query by the id
        # the .first() method displays the first value

    def update_book(_id, _title, _year, _genre):
        '''function to update the details of a book using the id, title,
        year and genre as parameters'''
        book_to_update = Book.query.filter_by(id=_id).first()
        book_to_update.title = _title
        book_to_update.year = _year
        book_to_update.genre = _genre
        db.session.commit()

    def delete_book(_id):
        '''function to delete a book from our database using
           the id of the book as a parameter'''
        Book.query.filter_by(id=_id).delete()
        # filter by id and delete
        db.session.commit()  # commiting the new change to our database
