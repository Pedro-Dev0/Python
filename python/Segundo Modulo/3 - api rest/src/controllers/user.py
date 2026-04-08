from flask import Blueprint, request
from src.app import User, db
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from sqlalchemy import inspect


app = Blueprint('user', __name__, url_prefix='/users')

def _create_user():
    data = request.json
    user = User(username=data["username"], email=data["email"])
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        # Aqui você poderia retornar uma mensagem de erro amigável
        raise Exception("Usuário já cadastrado!")
    
def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }
        for user in users
    ]


@app.route('/', methods=['GET', 'POST'])
def handle_user():
    if request.method == 'POST':
        _create_user()
        return {'message': 'User created!' }, HTTPStatus.CREATED
    else:
        return {'users': [_list_users()]}
    

@app.route('/<int:user_id>')
def get_user(user_id):
    user = db.get_or_404(User, user_id)
    return {
        "id": user_id,
        "username": user.username,
    }


@app.route('/<int:user_id>', methods=['PATCH', 'PUT'])
def update_user(user_id):
    user = db.get_or_404(User, user_id)
    data = request.json #

    # Se o 'data' for None, significa que o corpo da requisição veio vazio
    if not data:
        return {"error": "Corpo da requisição não pode estar vazio"}, 400

    mapper = inspect(User) # Técnica da imagem do professor
    for column in mapper.attrs:
        if column.key in data:
            setattr(user, column.key, data[column.key])
    
    db.session.commit() #
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }

@app.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()
    return '', HTTPStatus.NO_CONTENT