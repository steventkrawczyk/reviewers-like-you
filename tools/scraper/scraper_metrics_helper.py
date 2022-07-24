'''
This class is used to emit metrics about the scraper performance.
'''
import os


class ScraperMetricsHelper:
    def __init__(self, filepath=f'data/scraper_metrics.csv'):
        self.filepath = filepath

    def emit_metric(self, number_of_entries: int, entries_attempted: int, time_in_ms: int):
        if not os.path.isfile(self.filepath):
            with open(self.filepath,'a+') as f:
                f.write(["number_of_entries", "entries_attempted", "time_in_ms"])
        with open(self.filepath,'a') as f:
            f.write([number_of_entries, entries_attempted, time_in_ms])
        
