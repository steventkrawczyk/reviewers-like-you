'''
This will be the module used to drive the scraper process.
'''
from tools.scraper.data_submission_client import DataSubmissionClient
from tools.scraper.web_scraper import WebScraper
from tools.scraper.web_scraper_engine import WebScraperEngine


def main():
    data_submission_client = DataSubmissionClient()
    web_scraper_engine = WebScraperEngine()
    web_scraper = WebScraper(data_submission_client, web_scraper_engine)

    # TODO Logic to kick off web scraper jobs, track and store results
    # Things to track and store:
    #   * Number of entires scraped successfully
    #   * Number of entries not scraped successfully
    #   * Time take to execute scraping job on X number of entires (time per entry)

if __name__ == "__main__":
    main()