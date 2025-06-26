ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
MODE_WRITE = 'w'
MODE_READ = 'r'
ENCODING_FORMAT = 'utf-8'
NEW_LINE = ''
FIRST_LINES = ['Статус', 'Количество']
FINAL_LINE = 'Total'
PREFIX_STATUS_SUMMARY = 'status_summary_'
FORMAT_CSV = 'csv'
FEEDS_NAME = 'FEEDS'
RESULTS_DIR = 'results'
PEPS_FILENAME_PATTERN = 'pep_%(time)s.csv'
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
