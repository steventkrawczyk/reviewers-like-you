'''
This class exposes high level web scraping functionality to the scraper driver.
'''
from tools.scraper.data_submission_client import DataSubmissionClient
from tools.scraper.web_scraper_engine import WebScraperEngine


class WebScraper:
    def __init__(self, data_submission_client: DataSubmissionClient, web_scraper_engine: WebScraperEngine):
        self.data_submission_client = data_submission_client
        self.web_scraper_engine = web_scraper_engine

    '''
    Attempts to scrape a single entry. If successful, returns True.
    '''
    def scrapeSingleEntry(self) -> bool:
        pass

    '''
    Attempts to scrape max_entries number of entries. Returns the true
    number of entries scraped.
    '''
    def scrapeManyEntires(self, max_entries: int) -> int:
        pass


