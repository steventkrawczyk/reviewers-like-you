'''
This class is used to emit metrics about the scraper performance.
'''
import os
import time


class ScraperMetricsHelper:
    def __init__(self, filepath=f'data/scraper_metrics.csv'):
        self.filepath = filepath
        self.start = 0
        self.time_in_ns = 0

    def emit_metric(self, number_of_entries: int, entries_attempted: int, time_in_ns: int) -> None:
        if not os.path.isfile(self.filepath):
            with open(self.filepath,'a+') as f:
                f.write(["number_of_entries", "entries_attempted", "time_in_ns"])
        with open(self.filepath,'a') as f:
            f.write([number_of_entries, entries_attempted, time_in_ns])

    def start_timer(self) -> None:
        self.start = time.perf_counter_ns()
        self.time_in_ns = 0
        
    def end_timer(self) -> None:
        self.time_in_ns = self.start - time.perf_counter_ns()
        if self.start == 0:
            self.time_in_ns = 0
            raise RuntimeError("Cannot call end_timer before calling start_timer")
        self.start = 0

    def emit_metric(self, number_of_entries: int, entries_attempted: int) -> None:
        if self.time_in_ns == 0:
            raise RuntimeError("Cannot call emit_metric without running timer or passing in time_in_ns")
        self.emit_metric(number_of_entries, entries_attempted, self.time_in_ns)
