import time
import threading

class Core:
    def __init__(self, rate=20):
        self.rate = rate
        self.interval = 1.0 / rate
        self.running = False
        self.thread = None
        self.clicks = 0

    def start(self, duration=None):
        if self.running:
            return
        self.running = True
        self.clicks = 0
        self.thread = threading.Thread(target=self._run, args=(duration,), daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
            self.thread = None

    def _run(self, duration):
        start_time = time.perf_counter()
        next_time = start_time
        if duration is not None:
            end_time = start_time + duration
        else:
            end_time = None

        while self.running:
            self._click()
            self.clicks += 1
            next_time += self.interval
            current_time = time.perf_counter()
            if end_time is not None and current_time >= end_time:
                break
            delay = next_time - current_time
            if delay > 0.001:
                time.sleep(delay)
            else:
                while time.perf_counter() < next_time:
                    pass

    def _click(self):
        pass