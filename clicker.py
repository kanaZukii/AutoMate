# clicker.py
import time
import pyautogui
from PyQt6.QtCore import QThread, pyqtSignal

class ClickerThread(QThread):
    status = pyqtSignal(str)

    def __init__(self, interval_ms=100):
        super().__init__()
        self.interval = interval_ms / 1000.0
        self.running = False
        self.button = "left"

    def run(self):
        self.running = True
        self.status.emit("Clicker ON")

        while self.running:
            pyautogui.click(button=self.button)
            time.sleep(self.interval)

        self.status.emit("Clicker OFF")

    def stop(self):
        self.running = False
