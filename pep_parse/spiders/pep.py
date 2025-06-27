from urllib.parse import urlparse

import scrapy

from pep_parse.constants import EMPTY_STRING, ONE, TWO, ZERO
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Собирает номер, название и статус PEP-документов."""

    name = 'pep'
    start_urls = ['https://peps.python.org/']
    allowed_domains = [urlparse(url).netloc for url in start_urls]

    def parse(self, response):
        links = response.css(
            'table.pep-zero-table td:nth-child(3) a::attr(href)').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        number = EMPTY_STRING
        name = EMPTY_STRING
        if title:
            parts = title.split(' – ', maxsplit=ONE)
            if len(parts) == TWO:
                number = parts[ZERO].replace('PEP', EMPTY_STRING).strip()
                name = parts[ONE].strip()
            else:
                name = title.strip()

        status = response.css('dt:contains("Status") + dd abbr::text').get()

        yield PepParseItem({
            'number': number,
            'name': name,
            'status': status or 'Unknown'
        })
