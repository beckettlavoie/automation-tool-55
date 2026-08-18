import time
import random

class AutoClicker:
    def __init__(self, click_interval: float, max_clicks: int):
        self.click_interval = click_interval
        self.max_clicks = max_clicks
        self.click_count = 0

    def validate_inputs(self):
        if not (0 < self.click_interval < 5):
            raise ValueError('Click interval must be between 0 and 5 seconds.')
        if not (1 <= self.max_clicks <= 1000):
            raise ValueError('Max clicks must be between 1 and 1000.')

    def run(self):
        self.validate_inputs()
        while self.click_count < self.max_clicks:
            time.sleep(self.click_interval)
            self.perform_click()

    def perform_click(self):
        print('Click!')
        self.click_count += 1

# Example usage:
if __name__ == '__main__':
    clicker = AutoClicker(click_interval=1, max_clicks=10)
    clicker.run()