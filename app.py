from flask import Flask
import psycopg2

from db import *
from util.blueprints import register_blueprints
from lib.demo_data.demo_data import run_demo_data

app = Flask(__name__)


def create_all(app):
    with app.app_context():
        db.create_all()

        run_demo_data()


def create_app(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://127.0.0.1:5432/apc"

    init_db(app, db)


# def create_tables():
#     with app.app_context():
#         print("Creating tables...")
#         db.create_all()
#         print("Tables created successfully.")


my_app = create_app(app)

# register_blueprints(app)

if __name__ == "__main__":
    create_all(app)
    my_app.run(host="0.0.0.0", port="8086", debug=True)