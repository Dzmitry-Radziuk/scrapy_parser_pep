from scrapy import signals


class PepParseSpiderMiddleware:
    """Middleware для обработки входящих и исходящих данных паука."""

    @classmethod
    def from_crawler(cls, crawler):
        """Создаёт экземпляр и подключает сигнал открытия паука."""
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        """Обработка ответа перед передачей пауку. Возвращает None."""
        return None

    def process_spider_output(self, response, result, spider):
        """Обрабатывает результаты работы паука, пропуская их дальше."""
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        """Обработка исключений во время работы паука (пустой метод)."""
        pass

    def process_start_requests(self, start_requests, spider):
        """Обработка начальных запросов паука, пропускает их без изменений."""
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        """Логгирует событие открытия паука."""
        spider.logger.info(f'Spider opened: {spider.name}')


class PepParseDownloaderMiddleware:
    """Middleware для обработки запросов и ответов загрузчика."""

    @classmethod
    def from_crawler(cls, crawler):
        """Создаёт экземпляр и подключает сигнал открытия паука."""
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """Обработка запроса перед отправкой. Возвращает None."""
        return None

    def process_response(self, request, response, spider):
        """Обработка ответа перед передачей дальше. Возвращает ответ."""
        return response

    def process_exception(self, request, exception, spider):
        """Обработка исключений загрузчика (пустой метод)."""
        pass

    def spider_opened(self, spider):
        """Логгирует событие открытия паука."""
        spider.logger.info(f'Spider opened: {spider.name}')
