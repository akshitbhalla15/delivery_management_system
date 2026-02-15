# Delivery Management System (DMS)

A robust system designed to optimize delivery operations, enhance real-time visibility, and streamline inventory management. This project implements core logistics functionalities including route optimization using the Nearest Neighbor strategy and automated package tracking.

## 🚀 Features

* **Route Optimization:** Implements the **Nearest Neighbor Strategy** to calculate the most efficient delivery paths.
* **Real-time Tracking:** Updates delivery status dynamically as drivers scan packages.
* **Data Management:** Handles route and inventory data using **CSV and JSON** formats for flexibility.
* **Role-Based Access:** Distinct modules for Drivers (Mobile App interface), Inventory Managers, and System Administrators.
* **Security:** Ensures secure data handling for customer and delivery information.

## 🛠️ System Architecture

The system is composed of the following key components:
1.  **Mobile Application:** Interface for drivers to scan packages and view routes.
2.  **DMS Backend:** Processes logic for route optimization and status updates.
3.  **Database:** Stores persistent data for routes, inventory, and user logs.
4.  **Inventory Manager:** Tools for overseeing stock levels and package entry.

## 📂 Project Structure

```text
delivery_management_system/
├── data/                  # CSV and JSON files for Route Database
├── src/                   # Source code for the application
│   ├── algorithms/        # Optimization logic (e.g., Nearest Neighbor)
│   ├── models/            # Data models (Driver, Package, Route)
│   └── utils/             # Helper functions for file I/O
├── docs/                  # Documentation and diagrams (GRL models, etc.)
└── README.md
```

🔧 Installation & Setup
Clone the repository

```bash
git clone [https://github.com/akshitbhalla15/delivery_management_system.git](https://github.com/akshitbhalla15/delivery_management_system.git)
cd delivery_management_system
```

Prerequisites

[Insert Language, e.g., Python 3.8+ or Java 17]

[Insert Frameworks, e.g., Pandas, NumPy, or Spring Boot]

Install Dependencies

Bash
# Example for Python
pip install -r requirements.txt
💻 Usage
Load Data: Ensure your routes.csv or inventory.json files are placed in the data/ directory.

Run the System:

Bash
# Command to start the application
python main.py
Run Optimization: Select the "Optimize Route" option in the CLI/GUI to generate the delivery path.

🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.

👥 Authors
Akshit Bhalla - Initial work & Architecture

[Riley Muir] - Collaborator
