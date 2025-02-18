import sys
import random
import time
import threading
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
import keyboard

class AutoClicker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.running = False

    def initUI(self):
        self.setWindowTitle("Lineage 2 Auto Clicker")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Введите клавишу (например, '1'):")
        layout.addWidget(self.label)

        self.key_input = QLineEdit()
        layout.addWidget(self.key_input)

        self.interval_label = QLabel("Интервал (минимум-максимум) в секундах:")
        layout.addWidget(self.interval_label)

        self.min_interval = QLineEdit("0.1")
        self.min_interval.setPlaceholderText("Мин.")
        layout.addWidget(self.min_interval)

        self.max_interval = QLineEdit("0.3")
        self.max_interval.setPlaceholderText("Макс.")
        layout.addWidget(self.max_interval)

        self.start_button = QPushButton("Старт")
        self.start_button.clicked.connect(self.start_clicking)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Стоп")
        self.stop_button.clicked.connect(self.stop_clicking)
        layout.addWidget(self.stop_button)

        self.status_label = QLabel("Статус: Ожидание")
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def clicker(self):
        key = self.key_input.text().strip()
        try:
            min_delay = float(self.min_interval.text())
            max_delay = float(self.max_interval.text())
        except ValueError:
            self.status_label.setText("Ошибка: Введите корректные числа!")
            return

        self.status_label.setText("Статус: Работает")
        while self.running:
            keyboard.press_and_release(key)
            time.sleep(random.uniform(min_delay, max_delay))
        self.status_label.setText("Статус: Остановлено")

    def start_clicking(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.clicker, daemon=True)
            self.thread.start()

    def stop_clicking(self):
        self.running = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AutoClicker()
    window.show()
    sys.exit(app.exec())
