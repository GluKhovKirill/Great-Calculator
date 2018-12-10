import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from UI_data import Ui_MainWindow
 
 
class GreatCalculator(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('Калькулятор с напоминалками')       
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GreatCalculator()
    ex.show()
    sys.exit(app.exec())  