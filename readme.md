# AutoMate AutoClicker

A simple, lightweight autoclicker built with **Python** and **PyQt6**.

---

## Features

* Set custom click interval (milliseconds)
* Start/Stop buttons
* Global hotkey toggle (F6 in default)
* Can switch between mouse buttons

---

## Requirements

* Python 3.10+
* Packages:

  ```bash
  pip install pyqt6 pyautogui pynput
  ```

  or install with the provided requirements.txt:

  ```bash
  pip install -r requirements.txt
  ```

> ⚠️ On Linux, if using Wayland, global mouse/keyboard control may not work. X11 sessions are recommended.

---

## Usage

```bash
python main.py
```

* Adjust the interval with the spinbox
* Click **Start** to begin autoclicking
* Click **Stop** to stop, or press a **Hotkey** to toggle

---

## Building an Executable

Using PyInstaller:

```bash
pyinstaller --onefile --windowed --name AutoMate --hidden-import PyQt6.sip main.py
```

This generates a standalone executable in the `dist/` folder. Currently, the `dist/` folder contains a build for windows.

---
