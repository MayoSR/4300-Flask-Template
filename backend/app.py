# save this as app.py
from flask import Flask
from flask_cors import CORS
import sqlalchemy as db
engine = db.create_engine('mysql+pymysql://admin:admin@4300_TEAM_1_flask_db:3306/sample_db')

conn = engine.connect() 
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

