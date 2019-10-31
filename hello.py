# Beginner notes from me: 
# 1) There are differences between PyQt4 and PyQt5 (PyQt4 using QtGui.QApplication instead
# of QtWidgets.QApplication for example etc). Just a heads up when looking at "old" code

# 2) Not using PEP8 naming style here since PyQy naming style is based on C++ (camelCase). Looks better
# that way.

# Code and some text from from: https://realpython.com/python-pyqt-gui-calculator/
# In PyQt5, you can use any widget (a subclass of QWidget) as a top-level window, or even a button or a label. 
# The only condition is that you pass no parent to it. When you use a widget like this, PyQt5 automatically 
# gives it a title bar and turns it into a normal window.
# The parent-child relationship is used for two complementary purposes:
#    A widget that doesn't have a parent is a main window or a top-level window.
#    A widget that has a parent (which is always another widget) is contained (or shown) within its parent.
# This relationship also defines ownership, with parents owning their children. The PyQt5 ownership model 
# ensures that if you delete a parent (for example, a top-level window), then all of its children (widgets) 
# are automatically deleted as well.
# To avoid memory leaks, you should always make sure that any QWidget object has a parent, with the 
# exception of top-level windows.


import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 test app')
# QWidget.setGeometry(xpos, ypos, width, height)
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

window.show()

sys.exit(app.exec_())