class ValidationError(Exception):
    pass

def validate_input(input_value):
    if not isinstance(input_value, int) or input_value < 0:
        raise ValidationError("Input must be a non-negative integer.")


def process_inputs(input_list):
    for value in input_list:
        validate_input(value)
        # Proceed with processing the value
        # Placeholder for actual processing logic
        print(f"Processing: {value}")
