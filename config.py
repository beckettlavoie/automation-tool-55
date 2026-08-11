import os

class Config:
    def __init__(self):
        self.default_click_interval = 0.05
        self.click_count = 100
        self.click_button = 'left'
        self.auto_start = True
        self.log_file = 'click_log.txt'

    def load_env_variables(self):
        self.default_click_interval = float(os.getenv('CLICK_INTERVAL', self.default_click_interval))
        self.click_count = int(os.getenv('CLICK_COUNT', self.click_count))
        self.click_button = os.getenv('CLICK_BUTTON', self.click_button)
        self.auto_start = os.getenv('AUTO_START', str(self.auto_start)).lower() == 'true'

    def save_to_file(self):
        with open(self.log_file, 'w') as f:
            f.write(f'Click Interval: {self.default_click_interval}\n')
            f.write(f'Click Count: {self.click_count}\n')
            f.write(f'Click Button: {self.click_button}\n')
            f.write(f'Auto Start: {self.auto_start}\n')

config = Config()