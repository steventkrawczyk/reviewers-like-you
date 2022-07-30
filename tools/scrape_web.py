'''
This will be the module used to drive the scraper process.

This tool takes one command line argument, a number of entries to
scrape. To run it, try something like this:
    `python -m tools.scrape_web 25`
'''
import logging
import sys
from app.scraper.data_submission_client import DataSubmissionClient
from app.scraper.scraper_driver import ScraperDriver
from app.metrics.scraper_metrics_helper import ScraperMetricsHelper
from app.scraper.web_scraper_engine import WebScraperEngine


def main():
    print("Initializing...")
    data_submission_client = DataSubmissionClient()
    web_scraper_engine = WebScraperEngine()
    metrics_helper = ScraperMetricsHelper()

    scraper_driver = ScraperDriver(
        data_submission_client, web_scraper_engine, metrics_helper)

    total_entries = int(sys.argv[1:][0])

    print("Attempting to scrape " +
                 str(total_entries) + " entries overall.")
    scraper_driver.run(total_entries)
    print("Done scraping.")


if __name__ == "__main__":
    main()
