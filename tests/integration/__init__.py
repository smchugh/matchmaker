from app import app

HELLO_URL = "{}/api/hello".format(app.config.get('MATCH_API_URL', 'http://localhost'))
