from flask import Flask, render_template, session
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

app.config['DEBUG'] = True

if __name__ == "index":
    app.run(debug=True)


class HelloWorld(Resource):
    def get(self):
        return {"data": "HelloWorldResource"}
        raise TypeError

api.add_resource(HelloWorld, "/helloworld")

@app.route('/')
def hello_world():
    if not session.get('token'):
        return render_template('login.html')
    else:
        return 'Hello Boss'

