from flask import Flask 
from flask_restful import Api

from resources.doctor import DoctorListResource

app = Flask(__name__)
api = Api(app)


api.add_resource(DoctorListResource, '/doctors')


if __name__ == "__main__":
    app.run(port=5000, debug=True)