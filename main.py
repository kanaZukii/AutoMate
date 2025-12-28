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

    running = False

    selected_btn = 0
    mouseBtn = ["left", "right", "middle"]

    def start_clicking():
        nonlocal clicker, running

        if running:
            return

        interval = window.interval_box.value()
        clicker = ClickerThread(interval)
        clicker.status.connect(window.status_label.setText)
        clicker.button = mouseBtn[selected_btn]
        clicker.start()

        running = True

        window.start_btn.setEnabled(False)
        window.stop_btn.setEnabled(True)
        window.mouse_btn.setEnabled(False)
        window.hotkey_btn.setEnabled(False)

    def stop_clicking():
        nonlocal running, clicker

        if not running or not clicker:
            return

        if clicker:
            clicker.stop()
            clicker.wait()
        
        running = False

        window.start_btn.setEnabled(True)
        window.stop_btn.setEnabled(False)
        window.mouse_btn.setEnabled(True)
        window.hotkey_btn.setEnabled(True)

    def toggle_clicker():
        nonlocal running, clicker

        if running:
            stop_clicking()
        else:
            start_clicking()
    
    def toggle_mouseBtn():
        nonlocal selected_btn, mouseBtn, clicker

        if not running:
            selected_btn += 1

            if selected_btn >= len(mouseBtn):
                selected_btn = 0

            window.mouse_btn.setText(mouseBtn[selected_btn].capitalize())

    window.start_btn.clicked.connect(start_clicking)
    window.stop_btn.clicked.connect(stop_clicking)
    window.mouse_btn.clicked.connect(toggle_mouseBtn)

    bridge = HotkeyBridge()
    bridge.toggle.connect(toggle_clicker)

    hotkeys = HotkeyListener(bridge.toggle.emit)
    hotkeys.start()

    window.hotkey_btn.clicked.connect(hotkeys.begin_rebind)

    hotkeys.hotkey_changed.connect(
        lambda text: window.hotkey_btn.setText(f"{text}")
    )

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
