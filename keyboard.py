from pynput import keyboard

class HotkeyListener:
    def __init__(self, callback):
        self.callback = callback

    def start(self):
        def on_press(key):
            try:
                if key == keyboard.Key.f6:
                    self.callback.toggle.emit()
            except:
                pass

        listener = keyboard.Listener(on_press=on_press)
        listener.daemon = True
        listener.start()