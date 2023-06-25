import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

def button_click():
    print("Button clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create a main window
    window = QMainWindow()
    window.setWindowTitle("PyQt Sample")
    window.setGeometry(100, 100, 300, 200)

    # Create a button
    button = QPushButton("Click Me", window)
    button.setGeometry(100, 50, 100, 30)
    button.clicked.connect(button_click)

    # Show the main window
    window.show()

    # Start the event loop
    sys.exit(app.exec_())
