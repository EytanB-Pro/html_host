from flask import Flask, request, jsonify
from rdb.config import DevConfig
from rdb.model import db, User

app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/users', methods=['POST'])
def create_user():
    if request.is_json:
        data = request.get_json()
    else:
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    name = data.get('name')
    password = data.get('password')

    if not name or not password:
        return jsonify({'error': 'Name and password are required'}), 400

    new_user = User(name=name, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': f'User {name} created successfully'}), 201


if __name__ == '__main__':
    app.run(debug=True)