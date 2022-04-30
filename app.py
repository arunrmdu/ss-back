from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")
from flask_cors import CORS , cross_origin



app = Flask(__name__)


cors = CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == '__main__':

    logger.debug("Starting Flask Server")
    from api import *
    from healthcheck_api import *
    from login_api  import *

    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
