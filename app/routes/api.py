from app import api
from app.resources.hello import Hello


# Resources
api.add_resource(Hello, '/api/hello')
