# ui.py
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QLabel, QSpinBox
)

from PyQt6.QtCore import Qt

class GUI(QWidget):
    selected_mouseBtn = "Left"

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AutoMate Clicker")
        self.setFixedSize(300, 200)

        self.status_label = QLabel("Clicker OFF")
        self.status_label.setAlignment(
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter
        )
        self.status_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
            }
        """)

        self.interval_label = QLabel("Click Interval")
        self.interval_label.setAlignment(
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter
        )

        self.button_label = QLabel("Button:")
        self.button_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hotkey_label = QLabel("Hotkey:")
        self.hotkey_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mode_label = QLabel("Mode:")
        self.mode_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.interval_box = QSpinBox()
        self.interval_box.setRange(1, 10000)
        self.interval_box.setValue(100)
        self.interval_box.setSuffix(" ms")

        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")
        self.stop_btn.setEnabled(False)

        self.hotkey_btn = QPushButton("F6")
        self.mouse_btn = QPushButton("Left")
        self.mode_btn = QPushButton("Click")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)

        config_layout = QHBoxLayout()
        config_layout.addWidget(self.mode_label)
        config_layout.addWidget(self.mode_btn)
        config_layout.addWidget(self.button_label)
        config_layout.addWidget(self.mouse_btn)
        config_layout.addWidget(self.hotkey_label)
        config_layout.addWidget(self.hotkey_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.interval_label)
        layout.addWidget(self.interval_box)
        layout.addLayout(btn_layout)
        layout.addLayout(config_layout)

        self.setLayout(layout)
