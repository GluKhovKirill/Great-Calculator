from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 391)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 90, 261, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.three = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.three.setObjectName("three")
        self.gridLayout.addWidget(self.three, 4, 5, 1, 1)
        self.swimmingpoint = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.swimmingpoint.setObjectName("swimmingpoint")
        self.gridLayout.addWidget(self.swimmingpoint, 5, 5, 1, 1)
        self.two = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.two.setObjectName("two")
        self.gridLayout.addWidget(self.two, 4, 4, 1, 1)
        self.six = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.six.setObjectName("six")
        self.gridLayout.addWidget(self.six, 2, 5, 1, 1)
        self.plusminus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.plusminus.setObjectName("plusminus")
        self.gridLayout.addWidget(self.plusminus, 5, 3, 1, 1)
        self.minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.minus.setObjectName("minus")
        self.gridLayout.addWidget(self.minus, 2, 6, 1, 1)
        self.five = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.five.setObjectName("five")
        self.gridLayout.addWidget(self.five, 2, 4, 1, 1)
        self.four = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.four.setObjectName("four")
        self.gridLayout.addWidget(self.four, 2, 3, 1, 1)
        self.one = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.one.setObjectName("one")
        self.gridLayout.addWidget(self.one, 4, 3, 1, 1)
        self.zero = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.zero.setObjectName("zero")
        self.gridLayout.addWidget(self.zero, 5, 4, 1, 1)
        self.seven = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.seven.setObjectName("seven")
        self.gridLayout.addWidget(self.seven, 1, 3, 1, 1)
        self.clearitall = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clearitall.setObjectName("clearitall")
        self.gridLayout.addWidget(self.clearitall, 0, 3, 1, 1)
        self.backspace = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.backspace.setObjectName("backspace")
        self.gridLayout.addWidget(self.backspace, 0, 5, 1, 1)
        self.tangens = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.tangens.setObjectName("tangens")
        self.gridLayout.addWidget(self.tangens, 0, 0, 1, 1)
        self.cube = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cube.setObjectName("cube")
        self.gridLayout.addWidget(self.cube, 1, 1, 1, 1)
        self.nine = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.nine.setObjectName("nine")
        self.gridLayout.addWidget(self.nine, 1, 5, 1, 1)
        self.multiplication = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.multiplication.setObjectName("multiplication")
        self.gridLayout.addWidget(self.multiplication, 1, 6, 1, 1)
        self.cosinus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cosinus.setObjectName("cosinus")
        self.gridLayout.addWidget(self.cosinus, 0, 1, 1, 1)
        self.division = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.division.setObjectName("division")
        self.gridLayout.addWidget(self.division, 0, 6, 1, 1)
        self.antisquare = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.antisquare.setObjectName("antisquare")
        self.gridLayout.addWidget(self.antisquare, 2, 2, 1, 1)
        self.onedivision = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.onedivision.setObjectName("onedivision")
        self.gridLayout.addWidget(self.onedivision, 4, 0, 1, 1)
        self.antindegree = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.antindegree.setObjectName("antindegree")
        self.gridLayout.addWidget(self.antindegree, 2, 0, 1, 1)
        self.anticube = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.anticube.setObjectName("anticube")
        self.gridLayout.addWidget(self.anticube, 2, 1, 1, 1)
        self.square = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.square.setObjectName("square")
        self.gridLayout.addWidget(self.square, 1, 2, 1, 1)
        self.doubledegree = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.doubledegree.setObjectName("doubledegree")
        self.gridLayout.addWidget(self.doubledegree, 4, 1, 1, 1)
        self.tendegree = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.tendegree.setObjectName("tendegree")
        self.gridLayout.addWidget(self.tendegree, 4, 2, 1, 1)
        self.result = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 5, 6, 1, 1)
        self.plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.plus.setObjectName("plus")
        self.gridLayout.addWidget(self.plus, 4, 6, 1, 1)
        self.eight = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.eight.setObjectName("eight")
        self.gridLayout.addWidget(self.eight, 1, 4, 1, 1)
        self.clearit = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clearit.setObjectName("clearit")
        self.gridLayout.addWidget(self.clearit, 0, 4, 1, 1)
        self.ndegree = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ndegree.setObjectName("ndegree")
        self.gridLayout.addWidget(self.ndegree, 1, 0, 1, 1)
        self.sinus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sinus.setObjectName("sinus")
        self.gridLayout.addWidget(self.sinus, 0, 2, 1, 1)
        self.factorial = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.factorial.setObjectName("factorial")
        self.gridLayout.addWidget(self.factorial, 5, 2, 1, 1)
        self.pi = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pi.setObjectName("pi")
        self.gridLayout.addWidget(self.pi, 5, 1, 1, 1)
        self.logorifm = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.logorifm.setObjectName("logorifm")
        self.gridLayout.addWidget(self.logorifm, 5, 0, 1, 1)
 
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
 
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.three.setText(_translate("Dialog", "3"))
        self.swimmingpoint.setText(_translate("Dialog", ","))
        self.two.setText(_translate("Dialog", "2"))
        self.six.setText(_translate("Dialog", "6"))
        self.plusminus.setText(_translate("Dialog", "+-"))
        self.minus.setText(_translate("Dialog", "-"))
        self.five.setText(_translate("Dialog", "5"))
        self.four.setText(_translate("Dialog", "4"))
        self.one.setText(_translate("Dialog", "1"))
        self.zero.setText(_translate("Dialog", "0"))
        self.seven.setText(_translate("Dialog", "7"))
        self.clearitall.setText(_translate("Dialog", "CE"))
        self.backspace.setText(_translate("Dialog", "<---"))
        self.tangens.setText(_translate("Dialog", "tan"))
        self.cube.setText(_translate("Dialog", "x**3"))
        self.nine.setText(_translate("Dialog", "9"))
        self.multiplication.setText(_translate("Dialog", "*"))
        self.cosinus.setText(_translate("Dialog", "cos"))
        self.division.setText(_translate("Dialog", ":"))
        self.antisquare.setText(_translate("Dialog", "2Vx"))
        self.onedivision.setText(_translate("Dialog", "1/x"))
        self.antindegree.setText(_translate("Dialog", "nVx"))
        self.anticube.setText(_translate("Dialog", "3Vx"))
        self.square.setText(_translate("Dialog", "x**2"))
        self.doubledegree.setText(_translate("Dialog", "2**x"))
        self.tendegree.setText(_translate("Dialog", "10**x"))
        self.result.setText(_translate("Dialog", "="))
        self.plus.setText(_translate("Dialog", "+"))
        self.eight.setText(_translate("Dialog", "8"))
        self.clearit.setText(_translate("Dialog", "C"))
        self.ndegree.setText(_translate("Dialog", "x**n"))
        self.sinus.setText(_translate("Dialog", "sin"))
        self.factorial.setText(_translate("Dialog", "n!"))
        self.pi.setText(_translate("Dialog", "TT"))
        self.logorifm.setText(_translate("Dialog", "log"))