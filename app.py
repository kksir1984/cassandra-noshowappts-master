import json
from flask import Flask
import recreate_database as recreate_db
import no_show_etl as no_show

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker'

@app.route('/no_show_etl')
def get_widgets() :
  no_show.no_show_etl()

  return "filled db"

@app.route('/recreate_database')
def db_init():
  recreate_db.recreate_database()

  return 'init database'

if __name__ == "__main__":
  app.run(host ='0.0.0.0')