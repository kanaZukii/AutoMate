# clicker.py
import time
from PyQt6.QtCore import QThread, pyqtSignal
from pynput.mouse import Controller, Button


class ClickerThread(QThread):
    status = pyqtSignal(str)

    def __init__(self, interval_ms=100):
        super().__init__()
        self.interval = interval_ms / 1000.0
        self.running = False
        self.button = "left" 
        self.hold_btn = False

        self.mouse = Controller()

    def _get_button(self):
        if self.button == "right":
            return Button.right
        if self.button == "middle":
            return Button.middle

        return Button.left

    def run(self):
        self.running = True
        self.status.emit("Clicker ON")

        mouse_button = self._get_button()

        while self.running:
            self.mouse.press(mouse_button)
            if not self.hold_btn:
                self.mouse.release(mouse_button)

            time.sleep(self.interval)

        self.mouse.release(mouse_button)
        self.status.emit("Clicker OFF")

    def stop(self):
        self.running = False
