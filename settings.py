# settings.py

BOT_NAME = 'amazon_flashcards'

SPIDER_MODULES = ['amazon_flashcards.spiders']
NEWSPIDER_MODULE = 'amazon_flashcards.spiders'

FEEDS = {
    'amazon_flashcards.csv': {
        'format': 'csv',
        'encoding': 'utf8',
        'store_empty': False,
        'fields': ['question', 'answer'],
        'indent': 4,
    },
}
