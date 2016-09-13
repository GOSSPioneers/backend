import os
import sys
import datetime
import logging


from flask import Flask, request, send_from_directory, make_response

app = Flask(__name__)

logging.basicConfig(
    handlers=[logging.StreamHandler(sys.stdout)],
    level=logging.DEBUG,
    format='%(asctime)-15s|%(levelname)-8s|%(process)d|%(name)s|%(module)s|%(message)s')

@app.route('/', methods=['GET'])
def dashboard():
    """
    dashboard
    """
    
    return send_from_directory(app.static_folder, 'index.html')

@app.before_first_request
def main():
    """
    This method is executed before the first request
    """

    logging.info("starting up")

if __name__ == '__main__':
    app.run(host='0.0.0.0')