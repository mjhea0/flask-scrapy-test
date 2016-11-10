from flask import Flask, request, jsonify
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from spiders.DmozSpider import DmozSpider

app = Flask(__name__)

spiders = ['dmoz']

@app.route('/data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        content = request.get_json(silent=True)
        if content['spider'] in spiders:
            configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
            runner = CrawlerRunner()
            d = runner.crawl(DmozSpider, start_url=content['url'])
            d.addBoth(lambda _: reactor.stop())
            reactor.run()
            return('scraping')
        return abort(404)


if __name__ == '__main__':
    app.run(debug=True)
