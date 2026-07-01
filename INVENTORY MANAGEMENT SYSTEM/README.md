# Inventory Management System (Beginner Project)

A very simple desktop app built with **Python**, **PyQt5**, and **Qt Designer**.
Perfect for learning GUI programming in PyCharm.

## What This Project Does

- View all inventory items in a table
- Add new products (name, quantity, price)
- Update or delete existing items
- Search products by name
- Save data automatically to a JSON file

## Project Structure

```
INVENTORY MANAGEMENT SYSTEM/
├── main.py              # Start the app from here
├── inventory_gui.py     # GUI logic (button clicks, table updates)
├── inventory_data.py    # Save/load data from JSON
├── requirements.txt     # Python packages to install
├── ui/
│   └── main_window.ui   # Layout file (edit with Qt Designer)
└── data/
    └── inventory.json   # Your inventory data
```

## Step 1: Install Python Packages

Open the terminal in PyCharm (**View → Tool Windows → Terminal**) and run:

```bash
pip install -r requirements.txt
```

## Step 2: Run the App

In PyCharm, open `main.py`, then:

- Right-click → **Run 'main'**

Or from terminal:

```bash
python main.py
```

## Step 3: Edit the UI with Qt Designer (Optional)

The window layout is stored in `ui/main_window.ui`.

### Install Qt Designer

Qt Designer comes with PyQt5 tools. After installing PyQt5, run:

```bash
pip install pyqt5-tools
```

Then open Designer (path may vary on your PC):

```bash
designer
```

Or find **designer.exe** inside your Python `Scripts` folder.

### Open the UI File

1. Open Qt Designer
2. **File → Open** → select `ui/main_window.ui`
3. Drag and drop widgets to change the layout
4. **File → Save**
5. Run `main.py` again — your changes appear automatically!

> **Tip:** Do not rename widgets in the `.ui` file unless you also update
> `inventory_gui.py` (for example `addButton`, `nameInput`, `inventoryTable`).

## How the Code Works (Simple Explanation)

1. **`main_window.ui`** — Defines how the window looks (buttons, labels, table).
2. **`inventory_gui.py`** — Loads the `.ui` file and connects buttons to functions.
3. **`inventory_data.py`** — Reads and writes `data/inventory.json`.
4. **`main.py`** — Creates the app and shows the window.

## Try These Beginner Tasks

1. Change the window title in Qt Designer.
2. Add a new column to the table (e.g. "Category").
3. Change sample data in `data/inventory.json`.
4. Add a "Total Value" label that shows quantity × price for all items.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: PyQt5` | Run `pip install -r requirements.txt` |
| UI file not found | Make sure `ui/main_window.ui` exists |
| Designer not found | Run `pip install pyqt5-tools` |

Happy coding!
