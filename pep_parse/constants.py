# Числовые константы (индексы и счетчики)
ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4

# Форматы и шаблоны строк
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
PEPS_FILENAME_PATTERN = 'pep_%(time)s.csv'
PREFIX_STATUS_SUMMARY = 'status_summary_'
FORMAT_CSV = 'csv'
EMPTY_STRING = ''

# Режимы открытия файлов
MODE_WRITE = 'w'
MODE_READ = 'r'
ENCODING_FORMAT = 'utf-8'
NEW_LINE = ''

# Заголовки и финальные строки CSV
FIRST_LINES = ['Статус', 'Количество']
FINAL_LINE = 'Total'

# Настройки для работы с файлами и директориями
FEEDS_NAME = 'FEEDS'
RESULTS_DIR = 'results'

# Конфигурация пайплайна Scrapy
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
