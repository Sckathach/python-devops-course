import os
from flask import Flask
from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = {
    **dotenv_values(".env.shared"),
    **dotenv_values(".env.secret"),
    **os.environ
}

client = Flask(__name__)
client.secret_key = config["FLASK_SECRET_KEY"]


@client.route("/")
def index():
    return "<p>404 Not Found</p>"


@client.route("/api/v1/health")
def healthcheck():
    return {"success": True, "message": "Healthy! Yey!"}


if __name__ == "__main__":
    client.run(host="0.0.0.0")
