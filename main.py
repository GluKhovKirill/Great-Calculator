import sys
import json
from time import strftime
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QPushButton, QColorDialog
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
from Graphicka import Ui_Dialog
from logic import MathExecutor


class GreatCalculator(QMainWindow,Ui_Dialog):
    def __init__(self):
        self.colors = {"button_txt": "rgb(48, 42, 102)",
                       "operands_txt": "rgb(67, 42, 102)",
                       "answer_txt": "rgb(18, 36, 0)"}
        self.is_degree = True

        super().__init__()
        self.setupUi(self)

        self.degree.setChecked(True)
        self.pi.setText("\u03C0")
        self.e.setText("\u0190")
        self.anti_cube.setText("3"+"\u221A"+"x")
        self.anti_square.setText("2"+"\u221A"+"x")

        self.change_color(self.colors['operands_txt'], self.first)
        self.change_color(self.colors['operands_txt'], self.second)
        self.change_color(self.colors['answer_txt'], self.answer)
        self.change_color(self.colors['button_txt'], self.degree)
        self.change_color(self.colors['button_txt'], self.radians)
        self.change_color(self.colors['button_txt'], self.info_1)
        self.change_color(self.colors['button_txt'], self.info_2)
        self.change_color(self.colors['button_txt'], self.info_3)
        self.buttonGroup_2.buttonClicked.connect(self.change_units)
        for button in self.buttonGroup.buttons():
            self.change_color(self.colors["button_txt"], button)
            button.clicked.connect(self.set_answer)
        pass

    def change_color(self, color, element):
        element.setStyleSheet("color: {}".format(color))

    def repaint_all(self):
        try:
            self.change_color(self.colors['operands_txt'], self.first)
            self.change_color(self.colors['operands_txt'], self.second)
            self.change_color(self.colors['answer_txt'], self.answer)
            self.change_color(self.colors['button_txt'], self.degree)
            self.change_color(self.colors['button_txt'], self.radians)
            self.change_color(self.colors['button_txt'], self.info_1)
            self.change_color(self.colors['button_txt'], self.info_2)
            self.change_color(self.colors['button_txt'], self.info_3)            
            for button in self.buttonGroup.buttons():
                self.change_color(self.colors["button_txt"], button)     
            return (True, "Перекрашено.")
        except BaseException as err:
            return (False, err)

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
                     "CE": self.clr_all,
                     "Изменить цвета (и сохранить в файл)": self.change_all_colors,
                     "Загрузить цвета": self.load_colors,
                     "Сохранить цвета в файл (config.cnf)": self.dump_colors,
                     "Сохранить результат в answer.txt": self.save_result} 
        if operator in operators:
            operators[operator]()
        else:
            #print([operator])
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

    def load_colors(self):
        self.cos.setStyleSheet("color: red")
        try:
            with open("colors.cnf") as file:
                config = json.loads(file.read())
                if type(config) != dict:
                    raise TypeError("Неправильный формат файла")
                else:
                    self.colors = config
                self.answer.setText(self.repaint_all()[1])
        except BaseException as err:
            self.answer.setText(str(err))

    def dump_colors(self):
        try:
            config = json.dumps(self.colors)
            with open("colors.cnf", "w") as file:
                file.write(config)
            self.answer.setText("Сохранено.")
            return (True, "Сохранено.")
        except BaseException as err:
            self.answer.setText(str(err))
            return (False, err)

    def change_all_colors(self):
        button_color = QColorDialog.getColor(title="Выберите цвет для текста на кнопках")
        while not button_color.isValid():
            button_color = QColorDialog.getColor(title="Такой цвет невозможен. Выберите иной.")
        self.colors["button_txt"] = button_color.name()

        operands_color = QColorDialog.getColor(title="Выберите цвет для текста в полях ввода операндов")
        while not operands_color.isValid():
            operands_color = QColorDialog.getColor(title="Такой цвет невозможен. Выберите иной.")
        self.colors["operands_txt"] = operands_color.name()

        answer_color = QColorDialog.getColor(title="Выберите цвет для текста в поле ответа")
        while not answer_color.isValid():
            answer_color = QColorDialog.getColor(title="Такой цвет невозможен. Выберите иной.")
        self.colors["answer_txt"] = answer_color.name()
        # print(self.colors)
        self.repaint_all()

    def save_result(self):
        try:
            result = self.answer.text()
            with open("answer.txt", "a") as file:
                file.write("\n"+("*"*15)+"\n")
                file.write("Результат за "+strftime("%d.%m.%y %X") + ":\n")
                file.write(result)                
        except BaseException as err:
            return (False, err)
    pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GreatCalculator()
    ex.show()
    sys.exit(app.exec())  