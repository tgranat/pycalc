import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

# 
# Modal dialogs: block input to any other visible windows in the same application. 
# You can display a modal dialog by calling .exec_().
#
# Modeless dialogs: operate independently of other windows in the same application. 
# You can display a modeless dialog by using .show().

class Dialog(QDialog):

    """Dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        # When '?' button (on Windows) is clicked and WhatsThisMode is triggered, 
        # the elements of the dialog are supposed to give info about themselves.  
        self.setWhatsThis("Help on widget")
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Name:', QLineEdit())
        formLayout.addRow('Age:', QLineEdit())
        formLayout.addRow('Job:', QLineEdit())
        formLayout.addRow('Hobbies:', QLineEdit())
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
# Standard buttons to be displayed. Each button is associated with
#QMessageBox.Ok 0x00000400
#QMessageBox.Open 0x00002000
#QMessageBox.Save 0x00000800
#QMessageBox.Cancel 0x00400000
#QMessageBox.Close 0x00200000
#QMessageBox.Yes 0x00004000
#QMessageBox.No 0x00010000
#QMessageBox.Abort 0x00040000
#QMessageBox.Retry 0x00080000
#QMessageBox.Ignore 0x00100000
# so you can use 'bitwise OR' to specify several buttons 
# Commonly used
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())