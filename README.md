# 🏪 Inventory Management System (Python)

A **console-based Inventory Management System** built using Python.
The system supports **Admin** and **Normal Users**, inventory control, selling items, low-stock alerts, and user management.
All data is stored using **JSON files** for simplicity and persistence.

---

## ⚙️ Features

### 🔐 Authentication

* Secure login for **Admin** and **Normal Users**
* Password input hidden using `getpass`

### 👤 User Roles

#### Admin

* Add, update, or delete inventory items
* Search items by name, company, or quantity
* Sell items and calculate totals
* View full inventory
* View low-stock items (≤ 5 quantity)
* Manage users (add / delete / view users and admins)

#### Normal User

* Search inventory (by name or company)
* Sell items
* View low-stock alerts during selling

---

## 📦 Inventory Management

* Add new items with:

  * Name
  * Price
  * Quantity
  * Company
* Update existing items:

  * Change price
  * Add quantity
  * Change company
  * Delete item
* Automatic **low-stock warning** when quantity ≤ 5

---

## 📁 Data Storage (JSON Files)

The system uses the following files:

| File Name          | Description            |
| ------------------ | ---------------------- |
| `Storage.json`     | Stores inventory items |
| `Users.json`       | Stores normal users    |
| `Admin_Users.json` | Stores admin users     |

All changes are saved automatically on exit.

---

## ▶️ How to Run the Project

### Requirements

* Python **3.8+**

### Steps

```bash
python main.py
```

*(Replace `main.py` with your actual file name if different)*

---

## 🧠 Technologies Used

* Python
* JSON (data storage)
* `getpass` (secure password input)
* `os.system('cls')` for console UI (Windows)

---

## 📌 Notes

* This project is **console-based**
* Designed for **educational purposes**
* Works best on **Windows** (due to `cls` command)

---

## 🚀 Future Improvements

* Encrypt passwords
* Cross-platform screen clearing
* GUI or Web version
* Reports & sales history
* Database integration (MySQL / SQLite)

---

## ✅ Project Status

✔ Core features implemented
✔ Fully functional
✔ Ready for submission
