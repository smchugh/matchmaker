from flask.ext.restful import Resource


class Hello(Resource):
    def get(self):
        return {'message': 'Hello!'}, 200
