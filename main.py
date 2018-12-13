import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
from Graphicka import Ui_Dialog
from logic import MathExecutor
 

class GreatCalculator(QMainWindow,Ui_Dialog):
    def __init__(self):
        self.colors = {"button_txt": "rgb(48, 42, 102)",
                       "operands_txt": "rgb(67, 42, 102)",
                       "operator_txt": "rgb(95, 0, 227)",
                       "answer_txt": "rgb(18, 36, 0)"}
        self.is_degree = True

        super().__init__()
        self.setupUi(self)
        
        self.degree.setChecked(True)

        self.pi.setText("\u03C0")
        self.e.setText("\u0190")
        self.anti_cube.setText("3"+"\u221A"+"x")
        self.anti_square.setText("2"+"\u221A"+"x")
        
        self.buttonGroup_2.buttonClicked.connect(self.change_units)
        for button in self.buttonGroup.buttons():
            self.change_color(self.colors["button_txt"], button)
            if button.__class__ == QPushButton:
                button.clicked.connect(self.set_answer)
        pass
    
    def change_color(self, color, element):
        element.setStyleSheet("color: {}".format(color))
    
    def change_units(self, unit):
        if unit.text() == "RADIANS":
            self.is_degree = False
        else:
            self.is_degree = True
    
    def set_answer(self):
        first = self.first.text()
        second = self.second.text()
        operator = self.sender().text()        
        operators = {"C": self.clr,
                     "CE": self.clr_all} 
        if operator in operators:
            operators[operator]()
        else:
            executor = MathExecutor(first, operator, second, self.is_degree)
            answer = executor.execute()
            #print("A:",answer)
            self.answer.setText(answer)
    
    def clr(self):
        self.answer.setText("")
    
    def clr_all(self):
        self.first.setText("")
        self.second.setText("")
        self.answer.setText("")
        
    def load_config(self):
        with open("colors.cnf") as file:
            try:
                config = json.loads(file.read())
                if type(config) != dict:
                    raise TypeError("Неправильный формат файла")
                return config
            except BaseException as err:
                return err
        pass
    
    def dump_config(self):
        config = json.dumps(self.colors)
        with open("colors.cnf", "w") as file:
            file.write(config)
        return True
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GreatCalculator()
    ex.show()
    sys.exit(app.exec())  