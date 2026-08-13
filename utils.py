from typing import Tuple, List


def calculate_clicks(duration: float, interval: float) -> int:
    """Calculate the number of clicks that can be performed in a given duration.

    Args:
        duration (float): The total time in seconds for which clicks are to be performed.
        interval (float): The time in seconds between each click.

    Returns:
        int: The total number of clicks that can be performed.
    """
    return int(duration // interval)


def generate_click_pattern(count: int, position: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Generate a list of click positions.

    Args:
        count (int): The number of clicks to generate.
        position (Tuple[int, int]): The (x, y) position for the clicks.

    Returns:
        List[Tuple[int, int]]: A list of positions for the clicks.
    """
    return [position] * count


def validate_position(position: Tuple[int, int]) -> bool:
    """Validate that the given position is within screen bounds.

    Args:
        position (Tuple[int, int]): The (x, y) position to validate.

    Returns:
        bool: True if the position is valid, False otherwise.
    """
    x, y = position
    return 0 <= x <= 1920 and 0 <= y <= 1080
