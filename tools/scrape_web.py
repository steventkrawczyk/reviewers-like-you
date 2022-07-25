'''
This will be the module used to drive the scraper process.

This tool takes one command line argument, a number of entries to
scrape. To run it, try something like this:
    `python -m tools.scrape_web 25`
'''
import logging
import sys
from app.scraper.scraper_driver import ScraperDriver

BATCH_SIZE = 25

def main():
    logging.info("Initializing...")
    total_entries = int(sys.argv[1:][0])
    scraper_driver = ScraperDriver()

    logging.info("Attempting to scrape " + str(total_entries) + " entries overall.")
    scraper_driver.run(total_entries)
    logging.info("Done scraping.")


if __name__ == "__main__":
    main()
