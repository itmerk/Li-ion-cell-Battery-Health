# Li-ion Cell Dashboard

This project is a FastAPI application that visualizes the State of Health (SoH) and various metrics for Li-ion cells. The data is fetched from a MySQL database and displayed using Plotly visualizations.

## Features
- **Overview Page:** Introduction and navigation links.
- **Cell Dashboard:** Dropdown to select and visualize the State of Health for specific cell IDs.
- **Detailed Data Visualization:** Subplot grids for selected cell data, including voltage, current, temperature gap, and capacity over time.

## Requirements

- Python 3.8+
- MySQL Server
- Required Python packages (listed in `requirements.txt`)

## Installation and Setup

### Step 1: Clone the Repository

```git clone https://github.com/yourusername/li-ion-cell-dashboard.git```

```cd li-ion-cell-dashboard```

### Step 2: Create and Activate a Virtual Environment

```python3 -m venv venv```

```source venv/bin/activate```  # On Windows: venv\Scripts\activate

### Step 3: Install Required Python Packages

```pip install -r requirements.txt```

### Step 4: Set Up the MySQL Database

  1. Install and set up MySQL Server if not already installed.
  2. Create a database named li_ion_cells.
  3. Import your dataset into MySQL. Ensure the tables are named cells, data_5308, and data_5329.

### Step 5: Update Database Configuration
  Edit the get_db_connection() function in main.py with your MySQL connection details (host, user, password, and database).
  

  ```
  def get_db_connection():
            connection = mysql.connector.connect(
              host='localhost',
              user='root',
              password='your_password',
              database='li_ion_cells'
          )
  return connection```

