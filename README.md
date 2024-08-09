# Li-ion Cell Battery Health

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

```https://github.com/itmerk/Li-ion-cell-Battery-Health.git```

```cd Li-ion-cell-Battery-Health```

### Step 2: Create and Activate a Virtual Environment

```python3 -m venv venv```

```source venv/bin/activate```  # On Windows: venv\Scripts\activate

### Step 3: Install Required Python Packages

```pip install -r requirements.txt```

### Step 4: Set Up the MySQL Database

  1. Install and set up MySQL Server if not already installed.
  2. Create a database named li_ion_cells.
  3. Import your dataset into MySQL. Ensure the tables are named cells, data_5308, and data_5329.
  4. For Data Visualize and step by step process check Data Extract.ipynb file.

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
  return connection
```
### Step 6: Run the Application
  
  ```uvicorn main:app --reload --port 8080```
  
  This will start the FastAPI server on http://127.0.0.1:8080.

### Step 7: Access the Dashboard

* Open your web browser and navigate to http://127.0.0.1:8000.
* Explore the different routes:
    * / - Overview Page
    * /cell - Cell Dashboard with SoH and Degradation pie charts.
    * /data_5308 - Detailed visualization for cell 5308.
    * /data_5329 - Detailed visualization for cell 5329.


