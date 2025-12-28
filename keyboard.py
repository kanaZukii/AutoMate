from pynput import keyboard
from PyQt6.QtCore import QObject, pyqtSignal

class HotkeyListener(QObject):

    triggered = pyqtSignal()
    hotkey_changed = pyqtSignal(str)

    def __init__(self, trigger, default_key=keyboard.Key.f6):
        super().__init__()
        self.trigger = trigger
        self.hotkey = default_key
        self.hotkey_str = self._key_to_string(default_key)
        self.listening_for_rebind = False

        # connect old-style trigger
        self.triggered.connect(self.trigger)

    def _key_to_string(self, key):
        if isinstance(key, keyboard.Key):
            return key.name.upper()
        elif isinstance(key, keyboard.KeyCode):
            return key.char.upper() if key.char else "UNKNOWN"
        return "UNKNOWN"

    def start(self):
        def on_press(key):
            if self.listening_for_rebind:
                self.hotkey = key
                self.hotkey_str = self._key_to_string(key)
                self.listening_for_rebind = False
                self.hotkey_changed.emit(self.hotkey_str)
                return

            if key == self.hotkey:
                self.triggered.emit()

        listener = keyboard.Listener(on_press=on_press)
        listener.daemon = True
        listener.start()

    def begin_rebind(self):
        self.listening_for_rebind = True
