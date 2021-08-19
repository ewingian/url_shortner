from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from url_storage import UrlUtilites

# instantiate the helper class
url_helper = UrlUtilites()

# instantiate argument parser
# might not be necessary
parser = reqparse.RequestParser()
parser.add_argument('url')

# create the flask app
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class UrlGetter(Resource):
    ''' Simple fetch of the normal url '''

    def get(self, id):
        regular_url = url_helper.retrieve_normal_url(id)
        print(regular_url)
        return regular_url


class UrlShortenAndStore(Resource):
    ''' Takes in a regular url, shortens it to an id,
    and stores it away for later retrival '''

    def post(self):
        # result_set is a dictonary of id:url
        args = parser.parse_args()
        result_set = url_helper.shorten_url(args['url'])
        id = next(iter(result_set))
        print(id)
        url_helper.store_url(
            id, result_set[id]['shortened'],
            result_set[id]['normal']
        )
        return f"Successfully stored {result_set[id]} as {id}", 201


api.add_resource(HelloWorld, '/')
api.add_resource(UrlShortenAndStore, '/url_shorten/')
api.add_resource(UrlGetter, '/url/<id>')


if __name__ == '__main__':
    # not a production environment
    app.run(host='127.0.0.1', port=5001, debug=True)
