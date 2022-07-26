import logging
import os

from app.metrics.timed_metrics_helper import TimedMetricsHelper


class ScraperMetricsHelper(TimedMetricsHelper):
    '''
    This class is used to emit metrics about the scraper performance.
    '''

    def __init__(self, scraper_type: str = "default",
                 filepath: str = f'data/scraper_metrics.csv'):
        self.scraper_type = scraper_type
        self.filepath = filepath

    def record_scraper_performance(self, number_of_entries: int, entries_attempted: int, time_in_ns: int) -> None:
        if not os.path.isfile(self.filepath):
            with open(self.filepath, 'a+') as f:
                f.write(["scraper_type", "number_of_entries",
                        "entries_attempted", "time_in_ns"])
        with open(self.filepath, 'a') as f:
            f.write([self.scraper_type, number_of_entries,
                    entries_attempted, time_in_ns])

    def record_scraper_performance(self, number_of_entries: int, entries_attempted: int) -> None:
        if self.time_in_ns == 0:
            logging.error(
                "You should not call record_scraper_performance without running timer or passing in time_in_ns")
        self.record_scraper_performance(
            number_of_entries, entries_attempted, self.time_in_ns)
