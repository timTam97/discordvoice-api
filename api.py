import auth
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class User(Resource):
    def get(self):
        members = []
        with open("voice_lst", "r") as f:
            for line in f:
                members.append(line.strip())
        return members, 200


def main():
    api.add_resource(User, auth.API_URL)
    app.run(debug=False)


if __name__ == "__main__":
    main()
