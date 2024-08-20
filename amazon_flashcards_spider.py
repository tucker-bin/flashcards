import scrapy

class AmazonFlashcardsSpider(scrapy.Spider):
    name = "amazon_flashcards"
    start_urls = [
        'https://en.certificationanswers.com/amazon-sponsored-ads-certification-assessment-answers/'
    ]

    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            if 'amazon' in link:
                yield response.follow(link, self.parse_page)

    def parse_page(self, response):
        for qa in response.css('div.qa'):
            question = qa.css('div.question::text').get()
            answer = qa.css('div.answer::text').get()
            yield {
                'question': question,
                'answer': answer
            }
