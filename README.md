# Li-ion-cell-Battery-Health

This project is a FastAPI application that serves a dashboard to visualize the State of Health (SoH) and degradation of Li-ion cells using Plotly charts.

## Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- MySQL Server
- Pip (Python package installer)

## Installation

1. **Clone the Repository:**

   ```git clone https://github.com/itmerk/Li-ion-cell-Battery-Health.git```
   
   ```cd your-repository```
   
2. **Create and Activate a Virtual Environment:**

      ```python -m venv venv```
   
      ```source venv/bin/activate``` # On Windows use `venv\Scripts\activate`

3. **Install Dependencies:**

   Install the required Python packages:

   ```pip install -r requirements.txt```

   You may need to create a requirements.txt file if it does not exist. Here’s an example of what it should include:

   ```fastapi```
   ```uvicorn```
   ```mysql-connector-python```
   ```pandas```
   ```plotly```
   ```jinja2```

4. Set Up MySQL Database:
   Ensure you have MySQL Server running and a database named li_ion_cells created. Update the get_db_connection function in the main.py file if your database credentials or configurations are different.
   
5. Run the FastAPI Application:

   Start the FastAPI server using Uvicorn:

    ```bash
   uvicorn main:app --reload --port 8080 ```




