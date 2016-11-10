from datetime import datetime
from twisted.web import http
from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from twisted.internet import reactor
from arachne import Arachne

from flask import request, jsonify

app = Arachne(__name__)

@app.route('/data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        content = request.get_json(silent=True)
        # grab URL from payload, pass to scrapy, fire scraper, return data
        return jsonify(content)
    return 'testing a GET request'

resource = WSGIResource(reactor, reactor.getThreadPool(), app)
site = Site(resource)
reactor.listenTCP(8080, site)

if __name__ == '__main__':
    reactor.run()
