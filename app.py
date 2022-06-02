from flask import Flask
import logging as logger

import cart_api
logger.basicConfig(level="DEBUG")
from flask_cors import CORS , cross_origin
from config import config



app = Flask(__name__)

CORS_ALLOW_ORIGIN="*,*"
CORS_EXPOSE_HEADERS="*,*"
CORS_ALLOW_HEADERS="content-type,*"
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.after_request

def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Accept,Accept-Encoding,Host')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

if __name__ == '__main__':
    print("started server")
    logger.debug("Starting Flask Server")
    from healthcheck_api import *
    from login_api  import *
    from category import *
    from inventory import *
    from user_api import *
    from cart_api import *
    from orders_api import *
    # app.run()
    app.run(host="0.0.0.0",port=config['host_service']['port'],debug=True)
