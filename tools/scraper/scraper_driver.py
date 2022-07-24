'''
This will be the module used to drive the scraper process.
'''
import logging
import sys
from tools.scraper.data_submission_client import DataSubmissionClient
from tools.scraper.scraper_metrics_helper import ScraperMetricsHelper
from tools.scraper.web_scraper import WebScraper
from tools.scraper.web_scraper_engine import WebScraperEngine

BATCH_SIZE = 25

def main():
    logging.info("Initializing...")
    data_submission_client = DataSubmissionClient()
    web_scraper_engine = WebScraperEngine()
    web_scraper = WebScraper(data_submission_client, web_scraper_engine)
    metrics_helper = ScraperMetricsHelper()

    total_entries = int(sys.argv[1:][0])
    logging.info("Attempting to scrape " + str(total_entries) + " entries overall.")

    while total_entries > 0:
        entries_to_scrape = min(BATCH_SIZE, total_entries)
        logging.info("Attempting to scrape a batch of " + str(entries_to_scrape) + " entries...")
        metrics_helper.start_timer()
        scraped = web_scraper.scrape_many_entires(entries_to_scrape)
        metrics_helper.end_timer()
        metrics_helper.emit_metric(scraped, entries_to_scrape)
        logging.info("Scraped " + str(scraped) + " entries!")
        total_entries -= scraped
    
    logging.info("Done scraping.")


if __name__ == "__main__":
    main()
