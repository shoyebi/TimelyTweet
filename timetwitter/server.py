__author__ = 'shoyeb'

from flask import (Flask,render_template,request)
import os
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from handler.tweet import TweetTimeHandler
from common.config import ConfigManager
from common.log import Logger
logging=None
app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG', False)

@app.route("/")
def home_Page():
    return render_template("home.html")

@app.route("/time",methods=['GET','POST'])
def fetch_time():
    user_id = request.form.get("user_id",None)
    user_name = request.form.get("user_name",None)
    logging.debug("user_id : %s, user_name : %s"%(str(user_id),str(user_name)))
    tth = TweetTimeHandler(app)
    best_time,best_day =  tth.get_best_time_and_day(user_id, user_name)
    return render_template("success.html", best_time=str(best_time),best_day=str(best_day))

@app.route("/ping")
def pingwebhandler():
    return "pong"

if __name__ == "__main__":
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    logging=Logger.getLogger()
    app.config_obj = ConfigManager.get_instance()
    app.run(host='0.0.0.0', port=5000)
