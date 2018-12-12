import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
from Graphicka import Ui_Dialog
 

class GreatCalculator(QMainWindow,Ui_Dialog):
    def __init__(self):
        self.colors = {"button_txt": QColor("302a66"),
                       "operands_txt": QColor("F00"),
                       "operator_txt": QColor("432a66"),
                       "answer_txt": QColor("122400")}

        super().__init__()
        self.setupUi(self)
        #self.sinus.setStyleSheet("color: {}".format(QColor("FF0000").name()))
        self.change_color(self.colors["operands_txt"], self.first)
        pass
    
    def change_color(self, color, element):
        
        rgb = color.rgb()
        rgb = QColor(rgb).getRgb()[::-1]
        print(rgb)
        element.setStyleSheet("color: rgba{}".format(rgb))
    
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