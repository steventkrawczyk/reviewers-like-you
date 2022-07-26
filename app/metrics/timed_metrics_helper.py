import logging
import time


class TimedMetricsHelper:
    def __init__(self):
        self.start = 0
        self.time_in_ns = 0

    def start_timer(self) -> None:
        '''
        Starts the timer at the current timestamp. If the timer was already running, restarts it.
        '''
        self.start = time.perf_counter_ns()
        self.time_in_ns = 0

    def end_timer(self) -> None:
        '''
        Ends the timer and stores the time so that it can be recorded.
        '''
        self.time_in_ns = self.start - time.perf_counter_ns()
        if self.start == 0:
            self.time_in_ns = 0
            logging.error(
                "You should not call end_timer before calling start_timer")
        self.start = 0
