from pep_parse.constants import (ENCODING_FORMAT, FORMAT_CSV, ITEM_PIPELINES,
                                 PEPS_FILENAME_PATTERN, RESULTS_DIR)

BOT_NAME = 'pep_parse'
SPIDER_PATH = f'{BOT_NAME}.spiders'

SPIDER_MODULES = [SPIDER_PATH]
NEWSPIDER_MODULE = SPIDER_PATH

ROBOTSTXT_OBEY = True

FEEDS = {
    f'{RESULTS_DIR}/{PEPS_FILENAME_PATTERN}': {
        'format': FORMAT_CSV,
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
        'encoding': ENCODING_FORMAT,
    }
}

ITEM_PIPELINES = ITEM_PIPELINES
