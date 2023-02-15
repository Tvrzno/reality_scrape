import scrapy
import json
from reality_scrape.items import RealityItem  

# initial spider setting

class Spider1Spider(scrapy.Spider):
    name = "spider1"
    allowed_domains = ["www.sreality.cz"]
    start_urls = []

    # incremental setting of sites in URL

    for i in range(0, 25):
        start_urls.append('https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&sort=0&page=' + str(i))

    # algorithm for collecting data from JSON output of sreality API

    def parse(self, response):
        data = json.loads(response.text)
        reality_item = RealityItem()
        for item in data['_embedded']['estates']:
                reality_item['name'] =  item['name'],
                reality_item['img_url'] =  item['_links']['images'][0]['href']
                yield reality_item
