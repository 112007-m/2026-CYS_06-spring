

from pathlib import Path

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import uic

import inventory_data


UI_FILE = Path(__file__).parent / "ui" / "main_window.ui"


class InventoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        uic.loadUi(str(UI_FILE), self)

        self.items = inventory_data.load_items()
        self.selected_id = None

        self.setup_table()
        self.connect_signals()
        self.refresh_table()
        self.statusbar.showMessage("Ready. Add your first item!")

    def setup_table(self):

        self.inventoryTable.setColumnWidth(0, 50)
        self.inventoryTable.setColumnWidth(1, 200)
        self.inventoryTable.setColumnWidth(2, 100)
        self.inventoryTable.setColumnWidth(3, 100)

    def connect_signals(self):

        self.addButton.clicked.connect(self.add_item)
        self.updateButton.clicked.connect(self.update_item)
        self.deleteButton.clicked.connect(self.delete_item)
        self.clearButton.clicked.connect(self.clear_form)
        self.searchInput.textChanged.connect(self.refresh_table)
        self.inventoryTable.itemSelectionChanged.connect(self.on_row_selected)

    def refresh_table(self):

        search_text = self.searchInput.text().strip().lower()

        if search_text:
            visible_items = [
                item for item in self.items
                if search_text in item["name"].lower()
            ]
        else:
            visible_items = self.items

        self.inventoryTable.setRowCount(len(visible_items))

        for row, item in enumerate(visible_items):
            self.inventoryTable.setItem(row, 0, QTableWidgetItem(str(item["id"])))
            self.inventoryTable.setItem(row, 1, QTableWidgetItem(item["name"]))
            self.inventoryTable.setItem(row, 2, QTableWidgetItem(str(item["quantity"])))
            self.inventoryTable.setItem(row, 3, QTableWidgetItem(f"{item['price']:.2f}"))

    def get_form_data(self):

        name = self.nameInput.text().strip()
        quantity = self.quantityInput.value()
        price = self.priceInput.value()
        return name, quantity, price

    def add_item(self):

        name, quantity, price = self.get_form_data()

        if not name:
            QMessageBox.warning(self, "Missing Name", "Please enter a product name.")
            return

        new_item = {
            "id": inventory_data.get_next_id(self.items),
            "name": name,
            "quantity": quantity,
            "price": price,
        }
        self.items.append(new_item)
        inventory_data.save_items(self.items)

        self.clear_form()
        self.refresh_table()
        self.statusbar.showMessage(f"Added: {name}")

    def update_item(self):

        if self.selected_id is None:
            QMessageBox.information(self, "No Selection", "Select an item from the table first.")
            return

        name, quantity, price = self.get_form_data()

        if not name:
            QMessageBox.warning(self, "Missing Name", "Please enter a product name.")
            return

        for item in self.items:
            if item["id"] == self.selected_id:
                item["name"] = name
                item["quantity"] = quantity
                item["price"] = price
                break

        inventory_data.save_items(self.items)
        self.refresh_table()
        self.statusbar.showMessage(f"Updated: {name}")

    def delete_item(self):

        if self.selected_id is None:
            QMessageBox.information(self, "No Selection", "Select an item from the table first.")
            return

        answer = QMessageBox.question(
            self,
            "Confirm Delete",
            "Are you sure you want to delete this item?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if answer != QMessageBox.Yes:
            return

        self.items = [item for item in self.items if item["id"] != self.selected_id]
        inventory_data.save_items(self.items)

        self.clear_form()
        self.refresh_table()
        self.statusbar.showMessage("Item deleted.")

    def clear_form(self):

        self.selected_id = None
        self.nameInput.clear()
        self.quantityInput.setValue(0)
        self.priceInput.setValue(0.0)
        self.inventoryTable.clearSelection()

    def on_row_selected(self):

        selected_rows = self.inventoryTable.selectionModel().selectedRows()
        if not selected_rows:
            return

        row = selected_rows[0].row()
        item_id = int(self.inventoryTable.item(row, 0).text())

        for item in self.items:
            if item["id"] == item_id:
                self.selected_id = item_id
                self.nameInput.setText(item["name"])
                self.quantityInput.setValue(item["quantity"])
                self.priceInput.setValue(item["price"])
                self.statusbar.showMessage(f"Editing item #{item_id}")
                break
