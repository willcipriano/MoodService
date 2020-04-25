import bcrypt
import MoodService.repositories.user as user_repository
from MoodService.exceptions.user import UserPasswordValidationException
from MoodService.objects.user import User


def register_new_user(username: str, password: str) -> None:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf8'), salt)
    user_repository.create_new_user(username.upper(), hashed_password)


def validate_user_password(username: str, password: str) -> User:
    user = user_repository.get_user_by_id(username.upper())

    if bcrypt.checkpw(password.encode('utf8'), user.password):
        return user
    else:
        raise UserPasswordValidationException("The username or password provided are incorrect")