import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
    QHBoxLayout,QLineEdit,QSlider,QLabel)
from PyQt5.QtCore import Qt


class MainWindow (QWidget):
    def __init__(self):
        super().__init__()  
        self.setWindowTitle("Fun with Buttons!")
        vbox = QVBoxLayout()
        self.my_slider = QSlider(Qt.Horizontal, self)
        self.my_slider.valueChanged.connect(self.changeValue)
        vbox.addWidget(self.my_slider)

        self.slider2 = QSlider(Qt.Horizontal, self)
        self.slider2.sliderMoved.connect(self.connect1)
        vbox.addWidget(self.slider2)

        self.my_value = QLabel("0")
        vbox.addWidget(self.my_value)
        self.my_winner = QLabel("WINNER!!!!")
        vbox.addWidget(self.my_winner)
        self.my_winner.setHidden(True)


        hbox1 = QHBoxLayout()
        self.b1 = QPushButton("Hello!")
        self.b1.clicked.connect(self.on_b1_clicked)
        self.b1.setEnabled(False)
        hbox1.addWidget(self.b1)
    
        self.b2 = QPushButton("Hola!")
        self.b2.clicked.connect(self.on_b2_clicked)
        self.b2.setEnabled(False)
        hbox1.addWidget(self.b2)


        hbox2 = QHBoxLayout()
        self.b3 = QPushButton("Bye!")
        self.b3.clicked.connect(self.on_b3_clicked)
        hbox2.addWidget(self.b3)
        self.b4 = QPushButton("Chao!")
        self.b4.clicked.connect(self.on_b4_clicked)

        hbox2.addWidget(self.b4)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.word_entry = QLineEdit()
        vbox.addWidget(self.word_entry)
        self.word_entry.textEdited.connect(self.on_word_entered)


        self.setLayout(vbox)


    def changeValue(self):
        current_value = self.my_slider.value()
        self.my_value.setText(str(current_value))
        if current_value > 50:
            self.my_winner.setHidden(False)
        else:
            self.my_winner.setHidden(True)

    def connect1(self):
        same_value = self.my_slider.value()
        self.slider2.setValue(same_value)


    def on_b1_clicked(self):
        print("Hello!")
    def on_b2_clicked(self):
        self.setWindowTitle("PyQt!")
    def on_b3_clicked(self):
        print("You clicked the button at the bottom left.")
        self.b3.setText("Goodbye!")
    def on_b4_clicked(self):
        current_text = self.b4.text()
        self.b4.setText(current_text * 2)
    def on_word_entered(self):
        self.setWindowTitle(self.word_entry.text())
        self.b1.setEnabled(True)
        self.b2.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
