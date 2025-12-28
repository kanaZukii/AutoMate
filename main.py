# main.py
import sys
from PyQt6.QtWidgets import QApplication
from ui import GUI
from clicker import ClickerThread
from keyboard import HotkeyListener
from PyQt6.QtCore import QObject, pyqtSignal

class HotkeyBridge(QObject):
    toggle = pyqtSignal()


def main():
    app = QApplication(sys.argv)
    window = GUI()
    clicker = None

    def start_clicking():
        nonlocal clicker, running

        if running:
            return

        interval = window.interval_box.value()
        clicker = ClickerThread(interval)
        clicker.status.connect(window.status_label.setText)
        clicker.start()

        running = True

        window.start_btn.setEnabled(False)
        window.stop_btn.setEnabled(True)

    def stop_clicking():
        nonlocal running

        if not running or not clicker:
            return

        if clicker:
            clicker.stop()
            clicker.wait()
        
        running = False

        window.start_btn.setEnabled(True)
        window.stop_btn.setEnabled(False)

    def toggle_clicker():
        nonlocal running, clicker

        if running:
            stop_clicking()
        else:
            start_clicking()

    running = False

    window.start_btn.clicked.connect(start_clicking)
    window.stop_btn.clicked.connect(stop_clicking)

    bridge = HotkeyBridge()
    bridge.toggle.connect(toggle_clicker)

    hotkeys = HotkeyListener(bridge)
    hotkeys.start()

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
