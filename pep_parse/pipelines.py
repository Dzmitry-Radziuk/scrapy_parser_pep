import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from constants import (DATETIME_FORMAT, ENCODING_FORMAT, FEEDS_NAME,
                       FINAL_LINE, FIRST_LINES, FORMAT_CSV, MODE_WRITE,
                       NEW_LINE, ONE, PREFIX_STATUS_SUMMARY, RESULTS_DIR, ZERO)
from itemadapter import ItemAdapter


class PepParsePipeline:
    """Pipeline для подсчёта и сохранения статистики по статусам PEP."""

    def __init__(self, results_dir=RESULTS_DIR):
        """Инициализация счётчика и папки для результатов."""
        self.status_counter = defaultdict(int)
        self.output_dir = Path(results_dir)
        self.output_dir.mkdir(exist_ok=True)

    @classmethod
    def from_crawler(cls, crawler):
        """Получение пути к директории из настроек Scrapy."""
        feeds = crawler.settings.get(FEEDS_NAME)
        feed_path = list(feeds.keys())[ZERO]
        output_dir = Path(feed_path).parent
        return cls(output_dir)

    def open_spider(self, spider):
        """Вызывается при старте паука (пустой, т.к. не нужен)."""
        pass

    def process_item(self, item, spider):
        """Обрабатывает каждый item, увеличивая счётчик статусов."""
        status = ItemAdapter(item).get('status')
        self.status_counter[status] += ONE
        return item

    def close_spider(self, spider):
        """Вызывается при закрытии паука, записывает сводку в CSV файл."""
        total = sum(self.status_counter.values())
        timestamp = datetime.now().strftime(DATETIME_FORMAT)
        filename = self.output_dir / (
            PREFIX_STATUS_SUMMARY + timestamp + FORMAT_CSV
        )

        with open(
            filename,
            mode=MODE_WRITE,
            encoding=ENCODING_FORMAT,
            newline=NEW_LINE
        ) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(FIRST_LINES)
            for status, count in self.status_counter.items():
                writer.writerow([status, count])
            writer.writerow([FINAL_LINE, total])
