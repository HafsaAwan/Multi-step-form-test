from flask import Blueprint, render_template, request
import random

from models.user import User

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')

@users_blueprint.route("/form1", methods=['get', 'post'])
def form1():
  return render_template("users/form_step_1.html")

@users_blueprint.route("/form2", methods=['get', 'post'])
def form2():
    params = request.form

    username =params.get("username")
    password = params.get("password")
    email = params.get("email")

    new_user = User(username=username,password=password, email=email)

    new_user.save()

    user = User.get_or_none(User.username == username)

    return render_template("users/form_step_2.html", user=user)

@users_blueprint.route("/form3/<userid>", methods=['get', 'post'])
def form3(userid):
    user = User.get_or_none(User.id == userid)

    user.first_name = request.form.get("first")
    user.last = request.form.get("last")
    user.address = request.form.get("address")
    user.city = request.form.get("city")
    user.state = request.form.get("state")

    return render_template("users/form_step_3.html", user=user)



@users_blueprint.route('/new', methods=['GET'])
def new():
    pass


@users_blueprint.route('/', methods=['POST'])
def create():
    pass


@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
