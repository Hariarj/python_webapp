from flask import Flask, jsonify, request
from english.generator import generate_sentence, generate_word
app = Flask(__name__)

# Sample data for testing
books = [
    {'id': 1, 'title': 'Python for Beginners', 'author': 'John Smith'},
    {'id': 2, 'title': 'Flask Web Development', 'author': 'Jane Doe'},
    {'id': 3, 'title': 'Data Science with Python', 'author': 'Alice Brown'}
]

# English based services
@app.route('/sentence', methods=['GET'])
def get_sentense():
    return generate_sentence()

# Define routes for the API
# @app.route('/books', methods=['GET'])
# def get_books():
#     return jsonify({'books': books})

# @app.route('/books/<int:id>', methods=['GET'])
# def get_book(id):
#     book = [book for book in books if book['id'] == id]
#     return jsonify({'book': book})

# @app.route('/books', methods=['POST'])
# def add_book():
#     book = {'id': request.json['id'], 'title': request.json['title'], 'author': request.json['author']}
#     books.append(book)
#     return jsonify({'book': book}), 201

# @app.route('/books/<int:id>', methods=['PUT'])
# def update_book(id):
#     book = [book for book in books if book['id'] == id]
#     book[0]['title'] = request.json.get('title', book[0]['title'])
#     book[0]['author'] = request.json.get('author', book[0]['author'])
#     return jsonify({'book': book[0]})

# @app.route('/books/<int:id>', methods=['DELETE'])
# def delete_book(id):
#     book = [book for book in books if book['id'] == id]
#     books.remove(book[0])
#     return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
