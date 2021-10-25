from books import *


# route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    '''Function to get all the books in the database'''
    return jsonify({'books': Book.get_all_books()})


# route to get book by id
@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    return_value = Book.get_book(id)
    return jsonify(return_value)


# route to add new book
@app.route('/books', methods=['POST'])
def add_book():
    '''Function to add new book to our database'''
    request_data = request.get_json()  # getting data from client
    Book.add_book(request_data["title"], request_data["year"],
                    request_data["genre"])
    response = Response("book added", 201, mimetype='application/json')
    return response


# route to update book with PUT method
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    '''Function to edit book in our database using book id'''
    request_data = request.get_json()
    Book.update_book(id, request_data['title'], request_data['year'], request_data['genre'])
    response = Response("book Updated", status=200, mimetype='application/json')
    return response


# route to delete book using the DELETE method
@app.route('/books/<int:id>', methods=['DELETE'])
def remove_book(id):
    '''Function to delete book from our database'''
    Book.delete_book(id)
    response = Response("book Deleted", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(port=1234, debug=True)
