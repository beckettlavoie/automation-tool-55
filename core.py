import time
import threading
from typing import Callable

class ClickEngine:
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self.running = False
        self._thread = None

    def _execute(self, action: Callable[[], None]) -> None:
        last_time = time.perf_counter()
        while self.running:
            action()
            next_time = last_time + self.interval
            sleep_time = next_time - time.perf_counter()
            if sleep_time > 0:
                time.sleep(sleep_time)
            last_time = time.perf_counter()

    def start(self, action: Callable[[], None]) -> None:
        if not self.running:
            self.running = True
            self._thread = threading.Thread(target=self._execute, args=(action,), daemon=True)
            self._thread.start()

    def stop(self) -> None:
        self.running = False
        if self._thread:
            self._thread.join()
            self._thread = None