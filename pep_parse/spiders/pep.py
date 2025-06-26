import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        # Бежим по таблице PEP Zero (основной список)
        for row in response.css('table.pep-zero-table tbody tr'):
            link = row.css('td:nth-child(3) a::attr(href)').get()
            if link:
                yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        # Извлекаем заголовок, например: "PEP 8 – Style Guide for Python Code"
        title = response.css('h1.page-title::text').get()
        number = ''
        if title:
            number = title.split()[1].strip()

        status = response.css('dt:contains("Status") + dd abbr::text').get()

        yield PepParseItem({
            'number': number,
            'name': title,
            'status': status or 'Unknown'
        })
