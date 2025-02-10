import sys 

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton

from PySide6.QtCore import QEvent,Signal
from random import randint

class noPushButton(QPushButton):
    sMouseEnter = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
    
    def event(self, ev):
        if ev.type() == QEvent.Type.Enter:
            self.sMouseEnter.emit()
        return super().event(ev)

class mainWin(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle("¿Quieres ser mi novia?")
        self.setFixedSize(700,400)

        stylesheet = """
QMainWindow {
    background-color: #FFFACD; /* Amarillo pastel */
}

QLabel {
    font-size: 20px;
    font-weight: bold;
    color: #ffffff; /* Texto blanco */
    background-color: #FF5733; /* Naranja vibrante */
    border-radius: 10px;
    padding: 10px;
}

QPushButton {
    font-size: 18px;
    font-weight: bold;
    color: white;
    background-color: #33C3FF; /* Azul vibrante */
    border: 2px solid #1A8FFF;
    border-radius: 10px;
    padding: 8px 15px;
    margin: 2px;
}

QPushButton:hover {
    background-color: #1A8FFF; /* Azul más intenso al pasar el mouse */
}

QPushButton:pressed {
    background-color: #125B99; /* Azul oscuro cuando se presiona */
}

"""

        self.setStyleSheet(stylesheet)

        self.cWidget = QWidget()
        self.setCentralWidget(self.cWidget)
        

        self.lQuestion = QLabel("¿Quieres ser mi novia?",parent=self.cWidget)

        self.pbYes = QPushButton(self.cWidget)
        self.pbYes.setText("SI")
        self.pbYes.clicked.connect(self.on_yes_clicked)

        self.pbNo = noPushButton(self.cWidget)
        self.pbNo.setText("NO")
        self.pbNo.sMouseEnter.connect(self.updateNoPosition)

    def setWidgets(self):
        self._wQuestion = self.lQuestion.width()
        self._hQuestion = self.lQuestion.height()
        self._wWindow = self.cWidget.width()
        self._hWindow = self.cWidget.height()

        
        self._wNo = self.pbNo.width()
        self._hNo = self.pbNo.height()

        self._wYes = self.pbYes.width()
        self._hYes = self.pbYes.height()

        dw = self._wWindow/3
        dh = self._hWindow/3

        self.lQuestion.move((self._wWindow - self._wQuestion)/2,dh)
        self.pbNo.move(dw-self._wNo/2,2*dh)
        self.pbYes.move(2*dw-self._wYes/2,2*dh)
        
    def updateNoPosition(self):
        x = self.pbNo.x()
        y = self.pbNo.y()
        newX = randint(0,self._wWindow - self._wNo)
        newY = randint(0,self._hWindow - self._hNo)
        
        # obtenemos el nuevo x
        while ( not ( ( newX+2 < (x - self._wNo) ) or ( newX-2 > (x + self._wNo) ) ) ):
            newX = randint(0,self._wWindow - self._wNo)
        
        while ( not ( ( newY+2 < (y - self._hNo) ) or ( newY-2 > (y + self._hNo) ) ) ):
            newY = randint(0,self._hWindow - self._hNo)
        
        self.pbNo.move(newX,newY)
        

    def on_yes_clicked(self):
        self.lQuestion.setText("¡Sabía que dirías que sí! ❤️")
        self.pbNo.hide()
        self.pbYes.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = mainWin()
    win.show()
    win.setWidgets()

    app.exec()