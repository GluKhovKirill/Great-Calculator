import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.Core import QTimer
from UI_data import Ui_MainWindow
 
 
class GreatCalculator(QMainWindow,Ui_MainWindow):
    def __init__(self):
        self.colors = {}
        self.notes = {} # <QTimer object> : "note"
        super().__init__()
        self.setupUi(self)
        pass
    
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
    
    def add_timer(self, time, note):
        # Создание новой заметки
        # Время передается в секуднах
        if note in self.notes:
            raise NameError("Напоминалка с такой заметкой уже существует!")
        timer = Qtimer(self)
        timer.singleShot(time*1000, self.ring)
        self.notes[timer] = note
    
    def remove_timer(self, timer):
        # Удаление заметки
        try:
            return self.notes.pop[timer]
        except KeyError:
            # TODO: Если такого таймера не существует, то...
            # TODO: Обсудить реальность такой ситуации
            pass
        pass
    
    def ring(self):
        # TODO: Написать функцию, которая будет показывать уведомление, что время истекло (Текст заметки можно взять из remove_timer)
        pass
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GreatCalculator()
    ex.show()
    sys.exit(app.exec())  