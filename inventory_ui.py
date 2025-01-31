import sys
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel

class InventoryUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inventory Management")
        self.setGeometry(100, 100, 600, 400)

        # Layout
        self.layout = QVBoxLayout()

        # Inventory Table
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Item Name", "Quantity"])
        self.layout.addWidget(self.table)

        # Add Item Inputs
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Item Name")
        self.layout.addWidget(self.name_input)

        self.quantity_input = QLineEdit(self)
        self.quantity_input.setPlaceholderText("Quantity")
        self.layout.addWidget(self.quantity_input)

        # Buttons
        self.add_button = QPushButton("Add Item", self)
        self.add_button.clicked.connect(self.add_item)
        self.layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove Item", self)
        self.remove_button.clicked.connect(self.remove_item)
        self.layout.addWidget(self.remove_button)

        self.update_button = QPushButton("Update Quantity", self)
        self.update_button.clicked.connect(self.update_quantity)
        self.layout.addWidget(self.update_button)

        self.setLayout(self.layout)

        # Load Inventory
        self.load_inventory()

    def load_inventory(self):
        response = requests.get("http://localhost:8000/")
        inventory = response.json().get("inventory", [])
        self.table.setRowCount(len(inventory))
        for row, item in enumerate(inventory):
            self.table.setItem(row, 0, QTableWidgetItem(item["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(str(item["quantity"])))

    def add_item(self):
        name = self.name_input.text()
        quantity = int(self.quantity_input.text())

        # Call the API to add the item
        requests.post("http://localhost:8000/add-item", json={"name": name, "quantity": quantity})

        # Reload the inventory
        self.load_inventory()

    def remove_item(self):
        name = self.name_input.text()

        # Call the API to remove the item
        requests.post("http://localhost:8000/remove-item", json={"name": name})

        # Reload the inventory
        self.load_inventory()

    def update_quantity(self):
        name = self.name_input.text()
        quantity = int(self.quantity_input.text())

        # Call the API to update the quantity
        requests.post("http://localhost:8000/update-quantity", json={"name": name, "quantity": quantity})

        # Reload the inventory
        self.load_inventory()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryUI()
    window.show()
    sys.exit(app.exec_())
