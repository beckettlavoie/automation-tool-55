import time
import random

class ClickerError(Exception):
    pass

class Clicker:
    def __init__(self, click_interval=1.0):
        self.click_interval = click_interval
        if self.click_interval <= 0:
            raise ClickerError('Click interval must be greater than zero.')

    def click(self):
        try:
            # Simulating a click action
            print('Click!')
        except Exception as e:
            raise ClickerError(f'Failed to click: {e}') from e

    def start_clicking(self, num_clicks):
        if not isinstance(num_clicks, int) or num_clicks <= 0:
            raise ClickerError('Number of clicks must be a positive integer.')
        for _ in range(num_clicks):
            self.click()
            time.sleep(self.click_interval)

if __name__ == '__main__':
    clicker = Clicker(click_interval=0.5)
    try:
        clicker.start_clicking(5)
    except ClickerError as ce:
        print(f'Error: {ce}')