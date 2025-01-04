import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSlider
from PyQt5.QtCore import Qt

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.my_slider = QSlider(Qt.Horizontal, self)
        self.my_slider.setGeometry(30, 40, 200, 30)# x,y,width,height
        self.my_slider.valueChanged.connect(self.changeValue)

        self.setWindowTitle("Slider Example")

    def changeValue(self):
        print(self.my_slider.value())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())