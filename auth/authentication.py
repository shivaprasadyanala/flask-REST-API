import os
import jwt
from flask import jsonify, request
from flask_babel import lazy_gettext as _
from functools import wraps
from models.student import register


def jwt_get_user_id_from_payload_handler(payload):
    """
    Override this function if user_id is formatted differently in payload
    """
    return payload.get('id')


def jwt_get_user_permissions_from_payload_handler(payload):
    """
    Override this function if permissions is formatted differently in payload
    """
    return payload.get('permissions')


def authenticate_credentials(payload):
    """
    Returns an active user that matches the payload's user id.
    """
    user_id = jwt_get_user_id_from_payload_handler(payload)

    user = None
    if not user_id:
        raise Exception(
            _('Invalid Authorization header. No credentials provided.'))
    else:
        user = register.query.filter_by(id=user_id)
        print("hi in 26")
        print(user)
        # fetch the user data from the database.
        if not user:
            raise Exception(_('Invalid Authorization header. No user found.'))

    permissions = jwt_get_user_permissions_from_payload_handler(payload)

    return user, permissions


def get_authorization_header(header):
    """
    Return request's 'Authorization:' header.
    """
    auth = header.get('Authorization')
    return auth


def authenticate(token):
    """
    Returns a two-tuple of `User` and token if a valid signature has been
    supplied using JWT-based authentication.  Otherwise, returns `None`.
    """
    context = {}
    auth = token.split()
    auth_header_prefix = 'bearer'
    user = None

    if auth[0].lower() != auth_header_prefix:
        raise Exception(_('Invalid prefix.'))

    if len(auth) == 1:
        raise Exception(
            _('Invalid Authorization header. No credentials provided.'))
    elif len(auth) > 2:
        raise Exception(
            _('Invalid Authorization header or Credentials string or should not contain spaces.'))
    jwt_value = auth[1]
    print(jwt_value)
    try:
        payload = jwt.decode(
            jwt_value, 'secret_key', algorithms=['HS256'])

    except jwt.InvalidSignatureError:
        raise Exception(_('Invalid signature.'))
    except jwt.ExpiredSignatureError:
        raise Exception(_("Signature has been expired"))
    except jwt.DecodeError:
        raise Exception(_('Error decoding signature.'))
    except Exception:
        raise Exception(_('Error decoding signature'))

    user, permissions = authenticate_credentials(payload)
    return user, permissions


def is_authenticated(func):
    """
    Decorator for authenticate request,
    If token is authenticated user details added into "request.user".
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        headers = request.headers
        token = get_authorization_header(headers)
        print(token)
        if token:
            try:
                user, permissions = authenticate(token)
                setattr(request, 'user', user)
                setattr(request, 'permissions', permissions)
            except Exception as error:
                return jsonify({"detail": str(error)}), 401
        else:
            response = jsonify(
                {"detail": _("No authentication credentials were provided.")})
            response.status_code = 401
            return response
        return func(*args, **kwargs)

    return wrapper
