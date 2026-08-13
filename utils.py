import time
import random

def autoclick(interval: float, clicks: int) -> None:
    for _ in range(clicks):
        time.sleep(interval)
        perform_click()


def perform_click() -> None:
    # Simulate a mouse click
    print("Mouse clicked!")


def random_interval(min_interval: float, max_interval: float) -> float:
    return random.uniform(min_interval, max_interval)


def main() -> None:
    interval = random_interval(0.1, 0.5)
    clicks = 10
    autoclick(interval, clicks)

if __name__ == '__main__':
    main()