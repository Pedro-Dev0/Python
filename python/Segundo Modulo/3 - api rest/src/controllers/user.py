from flask import Blueprint, request
from src.app import User, db
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

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
    