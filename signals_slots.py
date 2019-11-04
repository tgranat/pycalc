"""Signals and slots example."""

import sys
#import functools

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

def greeting():
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello World!")

def greeting1(who):
    """Slot function."""
    if msg.text():
        msg.setText('')
    else:
        msg.setText(f'Hello {who}')

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
# connect the button's clicked signal to greeting()
btn.clicked.connect(greeting)  
btn1 = QPushButton('Greet1')
use_this_string = 'Gurka!'
# Version 1: use functools.partials()
#btn1.clicked.connect(functools.partial(greeting1, use_this_string))
# Version 2: use lambda.
btn1.clicked.connect((lambda:greeting1(use_this_string)))

layout.addWidget(btn)
layout.addWidget(btn1)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()

sys.exit(app.exec_())