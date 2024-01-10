import sys
import random
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer, Qt

class LotteryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.number_pool = list(range(1, 70))
        self.selected_numbers = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Lottery Game")
        self.setGeometry(100, 100, 400, 200)

        # Main layout
        layout = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        # Status label
        self.status_label = QLabel("Press 'Start' to draw numbers")
        layout.addWidget(self.status_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # center the numbers inside the boxes
        layout.addStretch()
        self.number_labels = [QLabel("") for _ in range(6)]
        num_layout = QHBoxLayout()
        for label in self.number_labels:
            label.setFixedSize(40, 40)
            label.setStyleSheet("border: 1px solid black; text-align: center; padding-left: 8px;")
            num_layout.addWidget(label)
        layout.addLayout(num_layout)

        # add button layout to main layout
        layout.addStretch()
        layout.addLayout(buttonLayout)


        # Start button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.startDrawing)

        # clear button
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clearNumbers)

        # add buttons to button layout
        buttonLayout.addWidget(self.start_button)
        buttonLayout.addWidget(clear_button)
        
        # Set main layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def startDrawing(self):
        self.status_label.setText("Drawing numbers...")
        self.start_button.setDisabled(True)
        self.drawNumber()

    def clearNumbers(self):
        self.number_pool = list(range(1, 70))
        self.selected_numbers = []
        for label in self.number_labels:
            label.setText("")
            label.setStyleSheet("background-color: white;")

    def drawNumber(self):
        if len(self.selected_numbers) < 6:
            QTimer.singleShot(random.randint(3000, 6000), self.updateNumber)
        else:
            self.status_label.setText("Drawing complete!")
            self.start_button.setDisabled(False)

    def updateNumber(self):
        number = random.choice(self.number_pool)
        self.number_pool.remove(number)
        self.selected_numbers.append(number)
        self.number_labels[len(self.selected_numbers) - 1].setText(str(number))
        self.number_labels[len(self.selected_numbers) - 1].setStyleSheet("color: white; background-color: green; border: 1px solid black; text-align: center; padding-left: 5px;")
        self.drawNumber()

def main():
    app = QApplication(sys.argv)
    ex = LotteryApp()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
