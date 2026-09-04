import time
import pyautogui
from typing import Tuple

def get_mouse_position() -> Tuple[int, int]:
    return pyautogui.position()

def safe_click(x: int, y: int, interval: float = 0.1) -> None:
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(interval)

def perform_drag(start: Tuple[int, int], end: Tuple[int, int], duration: float = 0.5) -> None:
    pyautogui.moveTo(start[0], start[1])
    pyautogui.dragTo(end[0], end[1], duration=duration, button='left')

def type_text(text: str, interval: float = 0.05) -> None:
    pyautogui.write(text, interval=interval)

def perform_double_click(x: int, y: int) -> None:
    pyautogui.doubleClick(x, y)

def screen_resolution() -> Tuple[int, int]:
    return pyautogui.size()

def is_on_screen(x: int, y: int) -> bool:
    width, height = screen_resolution()
    return 0 <= x <= width and 0 <= y <= height