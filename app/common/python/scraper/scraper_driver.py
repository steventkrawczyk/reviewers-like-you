import logging
from app.common.python.scraper.data_submission_client import DataSubmissionClient
from app.common.python.scraper.web_scraper import WebScraper
from app.common.python.scraper.web_scraper_engine import WebScraperEngine

MAX_BATCH_SIZE = 25


class ScraperDriver:
    '''
    This will be the class used to drive the scraper process.
    '''

    def __init__(self, data_submission_client: DataSubmissionClient,
                 web_scraper_engine: WebScraperEngine):
        self.web_scraper = WebScraper(
            data_submission_client, web_scraper_engine)

    def run(self, entries_to_scrape: int):
        while entries_to_scrape > 0:
            batch_size = min(MAX_BATCH_SIZE, entries_to_scrape)
            logging.debug("Attempting to scrape a batch of " +
                          str(batch_size) + " entries...")
            scraped = self.web_scraper.scrape_many_entires(batch_size)
            logging.debug("Scraped " + str(scraped) + " entries!")
            entries_to_scrape -= scraped
