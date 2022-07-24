'''
This will be the module used to drive the scraper process.
'''
from tools.scraper.data_submission_client import DataSubmissionClient
from tools.scraper.scraper_metrics_helper import ScraperMetricsHelper
from tools.scraper.web_scraper import WebScraper
from tools.scraper.web_scraper_engine import WebScraperEngine

BATCH_SIZE = 25

def main():
    data_submission_client = DataSubmissionClient()
    web_scraper_engine = WebScraperEngine()
    web_scraper = WebScraper(data_submission_client, web_scraper_engine)
    metrics_helper = ScraperMetricsHelper()

    metrics_helper.start_timer()
    scraped = web_scraper.scrape_many_entires(BATCH_SIZE)
    metrics_helper.end_timer()
    metrics_helper.emit_metric(scraped, BATCH_SIZE)


if __name__ == "__main__":
    main()
