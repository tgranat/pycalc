# Based on a tutorial by Leodanis Pozo Ramos
# https://realpython.com/python-pyqt-gui-calculator

import sys

from PyQt5.QtWidgets import QApplication
from pycalc.qt_controller import PyCalcCtrl, ERROR_MSG
from pycalc.qt_view import PyCalcUi

"""PyCalc is a simple calculator built using Python and PyQt5."""

# Create a Model to handle the calculator's operation

# The try...except block doesn't catch any specific exception.
# The function is based on the use of eval(), which can lead to some serious security issues.
# The general advice is to only use eval() on trusted input.

def evaluateExpression(expression):
    """Evaluate an expression."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result

def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Create instances of the model and the controller
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view)

    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == "__main__":
    main()