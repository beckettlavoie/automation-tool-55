class AutoClickerError(Exception):
    pass

class InvalidConfigurationError(AutoClickerError):
    def __init__(self, message):
        super().__init__(message)

class ClickIntervalError(AutoClickerError):
    def __init__(self, interval):
        message = f'Invalid click interval: {interval}'
        super().__init__(message)

class ClickLimitExceededError(AutoClickerError):
    def __init__(self, limit):
        message = f'Click limit exceeded: {limit}'
        super().__init__(message)