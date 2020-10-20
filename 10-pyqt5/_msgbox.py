from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from _msgBoxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnExit.clicked.connect(self.showDialog)
    
    def showDialog(self):

        result = QMessageBox.question(self, 'Close Application', 'Are u sure?', QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore, QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print('Yes clicked.')
            QtWidgets.qApp.quit()
        else:
            print('No clicked.')
        # msg = QMessageBox()

        # msg.setWindowTitle('Close Application')
        # msg.setText('Are you sure?')
        # msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        # msg.setDefaultButton(QMessageBox.Ok)
        # msg.setDetailedText('Details..')
        # msg.buttonClicked.connect(self.popup_button)
        # x = msg.exec_()
    
    # def popup_button(self, i):
    #     if i.text() == 'OK':
    #         print('OKEY')
    #         QtWidgets.qApp.quit()
    #     elif i.text() == 'Cancel':
    #         print('Cancel..')
    #     else:
    #         print('Ignore')

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()