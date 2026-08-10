import json
from validators import validate_input

class Processor:
    def __init__(self, data):
        self.data = data

    def process(self):
        for item in self.data:
            if not validate_input(item):
                continue
            self.handle_item(item)

    def handle_item(self, item):
        # Processing logic here
        print(f'Processing: {item}')

if __name__ == '__main__':
    raw_data = ['valid_data1', 'invalid_data', 'valid_data2']
    processor = Processor(raw_data)
    processor.process()
