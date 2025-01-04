import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit)

class MainWindow (QWidget):
    def __init__(self):
        super().__init__()  
        self.setWindowTitle("Fun With Buttons!")
        vbox = QVBoxLayout()

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

        hbox3 = QHBoxLayout()
        self.b5 = QPushButton("Compute!")
        self.b5.clicked.connect(self.on_b5_clicked)
        hbox3.addWidget(self.b5)

        self.b6 = QPushButton("Calcular!")
        self.b6.clicked.connect(self.on_b6_clicked)
        hbox3.addWidget(self.b6)


        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.word_entry = QLineEdit()
        vbox.addWidget(self.word_entry)
        self.word_entry.textEdited.connect(self.on_word_entered)


        self.setLayout(vbox)


    def on_b1_clicked(self):
        print("Hello!")

    def on_b2_clicked(self):
        self.setWindowTitle("PyQt!")

    def on_b3_clicked(self):
        print("You clicked the button at the bottom left")
        self.b3.setText("Goodbye!")
    def on_b4_clicked(self):
        current_text = self.b4.text()
        self.b4.setText(current_text * 2)
    def on_b5_clicked(self):
        print("Project Due Tonight!")
    def on_b6_clicked(self):
        current_title = self.windowTitle()
        self.setWindowTitle(current_title + "!")
    def on_word_entered(self):
        self.setWindowTitle(self.word_entry.text())
        self.b1.setEnabled(True)
        self.b2.setEnabled(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())

