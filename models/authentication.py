from auth_users.authentication.models import AuthenticateModel

from app import db
from helpers.utils import HelperModel


class AuthTokens(db.Model, HelperModel, AuthenticateModel):
    """Represents the authtokens table."""

    pass
