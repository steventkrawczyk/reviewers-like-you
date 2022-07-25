'''
This class exposes high level web scraping functionality to the scraper driver.
'''
from app.scraper.data_submission_client import DataSubmissionClient
from app.scraper.web_scraper_engine import WebScraperEngine


class WebScraper:
    def __init__(self, data_submission_client: DataSubmissionClient, web_scraper_engine: WebScraperEngine):
        self.data_submission_client = data_submission_client
        self.web_scraper_engine = web_scraper_engine

    '''
    Attempts to scrape a single entry. If successful, returns True.
    '''
    def scrape_single_entry(self) -> bool:
        pass

    '''
    Attempts to scrape max_entries number of entries. Returns the true
    number of entries scraped.
    '''
    def scrape_many_entires(self, max_entries: int) -> int:
        pass
