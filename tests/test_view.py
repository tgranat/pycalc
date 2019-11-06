from PyQt5.QtCore import Qt
from pycalc.qt_view import PyCalcUi
from pycalc.qt_controller import PyCalcCtrl
from pycalc.__main__ import evaluateExpression

def test_button(qtbot):
    # Setup
    window = PyCalcUi()
    #window.show()
    model = evaluateExpression
    PyCalcCtrl(model=model, view=window)
    qtbot.addWidget(window)

    qtbot.mouseClick(window.buttons['5'], Qt.LeftButton)
    assert window.display.text() == '5'

def test_calc(qtbot):
    # Setup
    window = PyCalcUi()
    window.show()
    model = evaluateExpression
    PyCalcCtrl(model=model, view=window)
    qtbot.addWidget(window)
    
    qtbot.mouseClick(window.buttons['5'], Qt.LeftButton)
    qtbot.mouseClick(window.buttons['+'], Qt.LeftButton)
    qtbot.mouseClick(window.buttons['6'], Qt.LeftButton)
    qtbot.mouseClick(window.buttons['='], Qt.LeftButton)
    assert window.display.text() == '11'

