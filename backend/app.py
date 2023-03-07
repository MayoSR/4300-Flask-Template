# save this as app.py
from flask import Flask
from flask_cors import CORS
import sqlalchemy as db
import os
print("ENV VAR",os.environ['DB_NAME'])
engine = db.create_engine(f"mysql+pymysql://admin:admin@{os.environ['DB_NAME']}:3306/sample-db")

conn = engine.connect() 
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"
