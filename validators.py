import re

class InputValidationError(Exception):
    pass

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise InputValidationError('Input must be a string')
    if not re.match('^[a-zA-Z0-9_]+$', user_input):
        raise InputValidationError('Input must be alphanumeric')
    if len(user_input) < 3 or len(user_input) > 20:
        raise InputValidationError('Input length must be between 3 and 20 characters')

# Example usage within the main processing loop:
# try:
#     validate_input(user_input)
# except InputValidationError as e:
#     print(f'Input validation failed: {e}')