from flask import Flask
from flask.ext import restful

from . import settings


app = Flask(__name__)
app.config.from_object(settings)
api = restful.Api(app)

from . import routes  # noqa
