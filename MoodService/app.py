from flask import Flask
from flask import request
from flask import jsonify
import MoodService.repositories.sqlite_util as database_util
from sqlite3 import Error as sqliteError
from MoodService.services import user as user_service
from MoodService.services import session as session_service
from MoodService.exceptions.user import UserPasswordValidationException

app = Flask(__name__)


@app.route('/mood', methods=["GET", "POST"])
def mood():
    return 'test'


@app.route('/login', methods=["POST"])
def login():
    try:
        user = user_service.validate_user_password(request.form["username"], request.form["password"])
        session = session_service.create_session(user.int_id)
    except UserPasswordValidationException:
        return jsonify("Unable to validate credentials")
    return jsonify(session)


@app.route('/register', methods=["POST"])
def register():
    user_service.register_new_user(request.form["username"], request.form["password"])


if __name__ == '__main__':
    app.run()
