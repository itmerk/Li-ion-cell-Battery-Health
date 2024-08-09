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

1: **Clone the Repository**

      ```git clone https://github.com/yourusername/li-ion-cell-dashboard.git```

      ```cd li-ion-cell-dashboard```
      
2. **Create and Activate a Virtual Environment:**

      ```python -m venv venv```
   
      ```source venv/bin/activate``` # On Windows use ```venv\Scripts\activate```

4. **Install Dependencies:**

   Install the required Python packages:

   ```pip install -r requirements.txt```

   You may need to create a requirements.txt file if it does not exist. Here’s an example of what it should include:

5. Set Up the MySQL Database

   * Install and set up MySQL Server if not already installed.
   * Create a database named li_ion_cells.
   * Import your dataset into MySQL. Ensure the tables are named cells, data_5308, and data_5329.
   
6. Run the FastAPI Application:

   Start the FastAPI server using Uvicorn:

   ```uvicorn main:app --reload --port 8080 ```

   * main refers to the name of your Python file (without the .py extension).
   * app is the FastAPI instance within the file.
   * --reload enables auto-reloading during development.
   * --port 8080 sets the port to 8080.
  
7. Access the Dashboard:

   Open a web browser and navigate to http://localhost:8080 to view the dashboard.

Endpoints
Overview Page: /

Provides navigation links to various parts of the dashboard.
Cell Data Page: /cell

Fetches and processes cell data from the database.
Displays a pie chart of the State of Health and degradation for the specified cell ID.




