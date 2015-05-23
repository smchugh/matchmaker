from os import getenv


def get_bool(env_var, default=False):
    value = getenv(env_var, default)
    if value in {'False', 'false'}:
        return False
    return bool(value)


def get_int(env_var, default=None):
    try:
        return int(getenv(env_var, default))
    except:
        return None

# Flask-related settings
APPLICATION_ENV = getenv('APPLICATION_ENV', 'development')
DEBUG = get_bool('DEBUG', False)
PORT = get_int('PORT', 80)

MATCH_API_URL = getenv('MATCH_API_URL', 'http://localhost')
