

import sys

from PyQt5.QtWidgets import QApplication

from inventory_gui import InventoryWindow


def main():
    app = QApplication(sys.argv)
    window = InventoryWindow()
    window.show()
    app.exec_()
    # sys.exit(app.exec_())


if __name__ == "__main__":
    main()
