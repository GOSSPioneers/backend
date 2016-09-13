"""
This is a simple backend for the Innovaton project
"""

import os
import sys
import datetime
import logging
import metrics
import importlib

from flask import Flask, request, send_from_directory, make_response, Response
from flask.ext.elasticsearch import FlaskElasticsearch

app = Flask(__name__)
#es = FlaskElasticsearch(app)
#es = ElasticSearch()

logging.basicConfig(
    handlers=[logging.StreamHandler(sys.stdout)],
    level=logging.DEBUG,
    format='%(asctime)-15s|%(levelname)-8s|%(process)d|%(name)s|%(module)s|%(message)s')

@app.route('/api/metric/<name>', methods=['GET'])
def get_metrics(name):
    """
    return metrics by name
    """
    mod = importlib.import_module('metrics.' + name, 'metrics')
    logging.info('loaded module %s', mod)
    return Response(mod.get_results(request.args), mimetype='application/json')    

@app.before_first_request
def main():
    """
    This method is executed before the first request
    """

    logging.info("starting up")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
