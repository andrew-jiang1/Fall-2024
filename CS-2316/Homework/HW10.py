import sys, re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class UntitledRestaurantSimulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Untitled Restaurant Simulator")
        self.OrderingScreen()

    def OrderingScreen(self):
        ######################################
        #Insert Code Below
        self.welcome_Label = QLabel("WELCOME TO THE UNNAMED RESTAURANT")
        self.welcome_Label.setFont(QFont("Cambria",20))
        self.welcome_Label.setAlignment(Qt.AlignCenter)
        self.hungry_Label = QLabel("Hope you're hungry!")
        self.hungry_Label.setAlignment(Qt.AlignCenter)
        self.total_Label = QLabel("Total: $0.00")
        self.thanks_Label = QLabel("Thanks for your order!")
        self.thanks_Label.setFont(QFont("Cambria",20))
        self.thanks_Label.setAlignment(Qt.AlignCenter)
        self.start_Button = QPushButton("Start Order")
        self.start_Button.clicked.connect(self.startOrder)
        self.submit_Button = QPushButton("Submit Order")
        self.submit_Button.clicked.connect(self.submitOrder)
        self.reset_Button = QPushButton("Reset Ordering Service")
        self.reset_Button.clicked.connect(self.resetOrderingService)
        self.spicy_Tonkotsu_Radio = QRadioButton("Spicy Tonkotsu: $15.99")
        self.spicy_Tonkotsu_Radio.clicked.connect(self.updateTotal)
        self.shoyu_Radio = QRadioButton("Shoyu: $14.99")
        self.shoyu_Radio.clicked.connect(self.updateTotal)
        self.japanese_Curry_Radio = QRadioButton("Japanese Curry: $16.99")
        self.japanese_Curry_Radio.clicked.connect(self.updateTotal)
        self.miso_Radio = QRadioButton("Miso: $13.99")
        self.miso_Radio.clicked.connect(self.updateTotal)
        self.spice_Level_1_Radio = QRadioButton("No Spice")
        self.spice_Level_2_Radio = QRadioButton("Medium")
        self.spice_Level_3_Radio = QRadioButton("Hot")
        self.spice_Level_4_Radio = QRadioButton("Extra Hot")
        self.udon_Radio = QRadioButton("Udon")
        self.ramen_Radio = QRadioButton("Ramen")
        self.first_Name_Edit = QLineEdit()
        self.last_Name_Edit = QLineEdit()
        self.phone_Edit = QLineEdit()
        self.address_Edit = QLineEdit()

        self.welcome_Layout = QVBoxLayout()
        self.welcome_Layout.addWidget(self.welcome_Label)
        self.welcome_Layout.addWidget(self.hungry_Label)
        self.welcome_Layout.addWidget(self.start_Button)

        self.personal_Info_Layout = QHBoxLayout()
        Fname = QLabel("First Name")
        self.personal_Info_Layout.addWidget(Fname)
        self.personal_Info_Layout.addWidget(self.first_Name_Edit)
        Lname = QLabel("Last Name")
        self.personal_Info_Layout.addWidget(Lname)
        self.personal_Info_Layout.addWidget(self.last_Name_Edit)
        phone = QLabel("Phone Number")
        self.personal_Info_Layout.addWidget(phone)
        self.personal_Info_Layout.addWidget(self.phone_Edit)
        addy = QLabel("Delivery Address")
        self.personal_Info_Layout.addWidget(addy)
        self.personal_Info_Layout.addWidget(self.address_Edit)

        self.soup_Selection_Group_Layout = QVBoxLayout()
        self.soup_Selection_Group_Layout.addWidget(self.spicy_Tonkotsu_Radio)
        self.soup_Selection_Group_Layout.addWidget(self.shoyu_Radio)
        self.soup_Selection_Group_Layout.addWidget(self.japanese_Curry_Radio)
        self.soup_Selection_Group_Layout.addWidget(self.miso_Radio)

        self.soup_Selection_Layout = QHBoxLayout()
        self.soup_Selection_Group = QGroupBox("Soup Base")
        self.soup_Selection_Group.setLayout(self.soup_Selection_Group_Layout)
        self.soup_Selection_Layout.addWidget(self.soup_Selection_Group)

        self.spice_Level_Group_Layout = QVBoxLayout()
        self.spice_Level_Group_Layout.addWidget(self.spice_Level_1_Radio)
        self.spice_Level_Group_Layout.addWidget(self.spice_Level_2_Radio)
        self.spice_Level_Group_Layout.addWidget(self.spice_Level_3_Radio)
        self.spice_Level_Group_Layout.addWidget(self.spice_Level_4_Radio)

        self.spice_Level_Layout = QHBoxLayout()
        self.spice_Level_Group = QGroupBox("Spice Level")
        self.spice_Level_Group.setLayout(self.spice_Level_Group_Layout)
        self.spice_Level_Layout.addWidget(self.spice_Level_Group)

        self.noodle_Type_Group_Layout = QVBoxLayout()
        self.noodle_Type_Group_Layout.addWidget(self.udon_Radio)
        self.noodle_Type_Group_Layout.addWidget(self.ramen_Radio)

        self.noodle_Type_Layout = QHBoxLayout()
        self.noodle_Type_Group = QGroupBox("Noodle Type")
        self.noodle_Type_Group.setLayout(self.noodle_Type_Group_Layout)
        self.noodle_Type_Layout.addWidget(self.noodle_Type_Group)

        self.button_Layout = QHBoxLayout()
        self.button_Layout.addWidget(self.submit_Button)
        self.button_Layout.addWidget(self.reset_Button)

        self.thanks_Layout = QVBoxLayout()
        self.thanks_Layout.addWidget(self.thanks_Label)
        
        self.order_Layout = QVBoxLayout()
        self.order_Layout.addLayout(self.personal_Info_Layout)
        self.order_Layout.addLayout(self.soup_Selection_Layout)
        self.order_Layout.addLayout(self.spice_Level_Layout)
        self.order_Layout.addLayout(self.noodle_Type_Layout)
        self.order_Layout.addLayout(self.button_Layout)
        self.order_Layout.addWidget(self.total_Label)

        self.welcome_Widget = QWidget()
        self.welcome_Widget.setLayout(self.welcome_Layout)
        self.setCentralWidget(self.welcome_Widget)

        self.order_Widget = QWidget()
        self.order_Widget.setLayout(self.order_Layout)
        self.order_Widget.setHidden(True)

        self.thanks_Widget = QWidget()
        self.thanks_Widget.setLayout(self.thanks_Layout)
        self.thanks_Widget.setHidden(True)



        ######################################

    def startOrder(self):
        ######################################
        #Insert Code Below
        self.welcome_Widget.setHidden(True)
        self.thanks_Widget.setHidden(True)
        self.order_Widget.setHidden(False)
        self.setCentralWidget(self.order_Widget)
        ######################################

    def resetOrderingService(self):
        ######################################
        #Insert Code Below
        self.OrderingScreen()
        self.order_Widget.setHidden(True)
        self.welcome_Widget.setHidden(False)
        self.setCentralWidget(self.welcome_Widget)

        ######################################

    def updateTotal(self):
        ######################################
        #Insert Code Below
        base_price = 0.0
        if self.spicy_Tonkotsu_Radio.isChecked():
            base_price = 15.99
        elif self.shoyu_Radio.isChecked():
            base_price = 14.99
        elif self.japanese_Curry_Radio.isChecked():
            base_price = 16.99
        elif self.miso_Radio.isChecked():
            base_price = 13.99
        
        self.total_Label.setText(f"Total: ${base_price}")
        ######################################

    def submitOrder(self):
        ######################################
        #Insert Code Below
        self.order_Widget.setHidden(True)
        self.thanks_Widget.setHidden(False)
        self.setCentralWidget(self.thanks_Widget)
        ######################################
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    simulator = UntitledRestaurantSimulator()
    simulator.show()
    sys.exit(app.exec_())
