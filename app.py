from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")
from flask_cors import CORS , cross_origin
from config import config



app = Flask(__name__)


cors = CORS(app, resources={r"/*": {"origins": "*"}})


if __name__ == '__main__':
    print("started server")
    logger.debug("Starting Flask Server")
    from api import *
    from healthcheck_api import *
    from login_api  import *
    from category import *
    # app.run()
    app.run(host="0.0.0.0",port=config['host_service']['port'],debug=True)
