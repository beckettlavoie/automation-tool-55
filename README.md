[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# automation-tool-55

A Python-based autoclicker designed to handle repetitive mouse clicking tasks efficiently. It offers fine-grained control over automation parameters for both casual and professional use cases.

## Features
- Millisecond-accurate intervals for click timing
- Custom hotkeys to start, stop, and adjust settings on the fly
- Options for different click types including single and double clicks
- Session duration limits and click count targets

## Installation

Clone the repository and set up the environment:

```bash
git clone https://github.com/Developer/automation-tool-55.git
cd automation-tool-55
pip install -r requirements.txt
```

## Basic Usage

Run the tool via command line with specified parameters:

```bash
python main.py --interval 0.05 --button left --duration 300
```

This command sets a 50ms interval between left clicks and runs for 5 minutes.

To integrate in your own scripts:

```python
from automation_tool_55 import AutoClicker

clicker = AutoClicker(interval=0.1, button="left")
clicker.start()
```