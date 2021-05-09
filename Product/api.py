from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
	def get(Self):
		return {
			'product: ['Icream', 'chocolate', 'fruit']
			}
api.add_resource(Product, '/')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debut=True)
