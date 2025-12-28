# ui.py
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QLabel, QSpinBox
)

from PyQt6.QtCore import Qt

class GUI(QWidget):
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

        self.hotkey_label = QLabel("Toggle Hotkey:")
        self.hotkey_label.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.interval_box = QSpinBox()
        self.interval_box.setRange(1, 10000)
        self.interval_box.setValue(100)
        self.interval_box.setSuffix(" ms")

        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")
        self.stop_btn.setEnabled(False)

        self.hotkey_btn = QPushButton("F6")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)

        hotkey_layout = QHBoxLayout()
        hotkey_layout.addWidget(self.hotkey_label)
        hotkey_layout.addWidget(self.hotkey_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.interval_label)
        layout.addWidget(self.interval_box)
        layout.addLayout(btn_layout)
        layout.addLayout(hotkey_layout)

        self.setLayout(layout)
