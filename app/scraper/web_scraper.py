from app.scraper.data_submission_client import DataSubmissionClient
from app.scraper.web_scraper_engine import WebScraperEngine


class WebScraper:
    '''
    This class exposes high level web scraping functionality to the scraper driver.
    '''

    def __init__(self, data_submission_client: DataSubmissionClient, web_scraper_engine: WebScraperEngine):
        self.data_submission_client = data_submission_client
        self.web_scraper_engine = web_scraper_engine

    def scrape_single_entry(self) -> bool:
        '''
        Attempts to scrape a single entry. If successful, returns True.
        '''
        pass

    def scrape_many_entires(self, max_entries: int) -> int:
        '''
        Attempts to scrape max_entries number of entries. Returns the true
        number of entries scraped.
        '''
        pass
