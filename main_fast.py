from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import HTMLResponse
import mysql.connector
import plotly.express as px
import pandas as pd
from jinja2 import Template
from datetime import datetime
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio
import secrets

app = FastAPI()

security = HTTPBasic()

# Function to verify user credentials
def verify_credentials(credentials: HTTPBasicCredentials):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "12345")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials

@app.get("/user")
def read_current_user(credentials:Annotated[HTTPBasicCredentials,Depends(security)]):
    return {"Username": credentials.username, "Password": credentials.password}

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='li_ion_cells'
    )
    return connection

# Template for the dropdown menu page
dropdown_template = Template("""
<!DOCTYPE html>
<html>
<head>
    <title>Cell Dashboard</title>
</head>
<body>
    <h1>Cell Dashboard</h1>
    <form action="/charts" method="get">
        <label for="cell_id">Select Cell ID:</label>
        <select id="cell_id" name="cell_id">
            {% for cell in cell_ids %}
            <option value="{{ cell }}">{{ cell }}</option>
            {% endfor %}
        </select>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
""")

# Overview Page
@app.get("/", response_class=HTMLResponse)
def overview(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    verify_credentials(credentials)
    return HTMLResponse(content="""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Overview</title>
    </head>
    <body>
        <h1>Dashboard</h1>
        <p>Welcome to the Li-ion Cell Dashboard. Use the links below to navigate.</p>
        <ul>
            <li><a href="/cell">Cell_ID</a></li>
            <li><a href="/data_5308">5308</a></li>
            <li><a href="/data_5329">5329</a></li>
        </ul>
    </body>
    </html>
    """)

# Route to fetch data from MySQL
@app.get("/cell")
def fetch_data():
    
    connection = mysql.connector.connect(host='localhost',user='root',password='12345',database='li_ion_cells')
    mycursor = connection.cursor()

    query = "select * from cells"
    mycursor.execute(query)

    columns = [desc[0] for desc in mycursor.description]
    result = mycursor.fetchall()
    cells= pd.DataFrame(result, columns=columns)

    # Calculate State of Health (SoH) and Degradation
    cells['SoH'] = (cells['discharge_capacity'] / cells['nominal_capacity']) * 100
    cells['Degradation'] = abs(100 - cells['SoH'])

    # Extract data for pie charts
    labels = ["SoH", "Degradation"]
    cell_5308_values = cells.loc[cells['cell_id'] == 5308, ['SoH', 'Degradation']].mean().tolist()
    cell_5329_values = cells.loc[cells['cell_id'] == 5329, ['SoH', 'Degradation']].mean().tolist()

    # Create subplots with 'domain' type for pie charts
    fig = make_subplots(rows=1, cols=2, 
                        specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=("5308", "5329"))

    # Add the pie charts
    fig.add_trace(go.Pie(
        labels=labels, 
        values=cell_5308_values, 
        textinfo='label+percent',
        marker=dict(colors=['#66b3ff', '#ff9999']),
        hole=.3
    ), row=1, col=1)

    fig.add_trace(go.Pie(
        labels=labels, 
        values=cell_5329_values, 
        textinfo='label+percent',
        marker=dict(colors=['#66b3ff', '#ff9999']),
        hole=.3
    ), row=1, col=2)

    # Update layout
    fig.update_layout(title_text="State of Health", showlegend=False)

    # Convert the figure to HTML
    chart_html = pio.to_html(fig, full_html=False)

    return HTMLResponse(content=chart_html)
    
# Custom function to handle datetime objects
def convert_datetime(item):
    if isinstance(item, datetime):
        return item.strftime('%Y-%m-%d %H:%M:%S')
    return item
    
# Route to fetch data from MySQL
@app.get("/data_5308")
def fetch_data_5308():
    connection = mysql.connector.connect(host='localhost',user='root',password='12345',database='li_ion_cells')
    mycursor = connection.cursor()

    query = "select * from data_5308"
    mycursor.execute(query)

    columns = [desc[0] for desc in mycursor.description]
    result = mycursor.fetchall()
    data_5308= pd.DataFrame(result, columns=columns)

    # Convert 'Absolute Time' to datetime
    data_5308['Absolute Time'] = pd.to_datetime(data_5308['Absolute Time'])

    # Create a 2x2 subplot grid
    fig = make_subplots(rows=2, cols=2, 
                        subplot_titles=('Voltage vs Time', 'Current vs Time', 
                                        'Gap of Temperature vs Time', 'CapaCity(mAh) vs Time'))

    # Plot 1: Voltage vs Time
    fig.add_trace(
        go.Scatter(x=data_5308['Absolute Time'], y=data_5308['Voltage(V)'], mode='lines+markers', name='Voltage (V)'),
        row=1, col=1
    )

    # Plot 2: Current vs Time
    fig.add_trace(
        go.Scatter(x=data_5308['Absolute Time'], y=data_5308['Cur(mA)'], mode='lines+markers', name='Current (mA)'),
        row=1, col=2
    )

    # Plot 3: Gap of Temperature vs Time
    fig.add_trace(
        go.Scatter(x=data_5308['Absolute Time'], y=data_5308['Gap of Temperature'], mode='lines+markers', name='Gap of Temperature'),
        row=2, col=1
    )

    # Plot 4: CapaCity(mAh) vs Time
    fig.add_trace(
        go.Scatter(x=data_5308['Absolute Time'], y=data_5308['CapaCity(mAh)'], mode='lines+markers', name='CapaCity (mAh)'),
        row=2, col=2
    )

    # Update layout for better appearance
    fig.update_layout(height=800, width=1400, title_text="5308", showlegend=False)

    # Convert the figure to HTML
    chart_html = pio.to_html(fig, full_html=False)

    return HTMLResponse(content=chart_html)
        
# Route to fetch data from MySQL
@app.get("/data_5329")
def fetch_data_5329():

    connection = mysql.connector.connect(host='localhost',user='root',password='12345',database='li_ion_cells')
    mycursor = connection.cursor()

    query = "select * from data_5329"
    mycursor.execute(query)

    columns = [desc[0] for desc in mycursor.description]
    result = mycursor.fetchall()
    data_5329= pd.DataFrame(result, columns=columns)

    # Convert 'Absolute Time' to datetime
    data_5329['Absolute Time'] = pd.to_datetime(data_5329['Absolute Time'])

    # Create a 2x2 subplot grid
    fig = make_subplots(rows=2, cols=2, 
                        subplot_titles=('Voltage vs Time', 'Current vs Time', 
                                        'Gap of Temperature vs Time', 'CapaCity(mAh) vs Time'))

    # Plot 1: Voltage vs Time
    fig.add_trace(
        go.Scatter(x=data_5329['Absolute Time'], y=data_5329['Voltage(V)'], mode='lines+markers', name='Voltage (V)'),
        row=1, col=1
    )

    # Plot 2: Current vs Time
    fig.add_trace(
        go.Scatter(x=data_5329['Absolute Time'], y=data_5329['Cur(mA)'], mode='lines+markers', name='Current (mA)'),
        row=1, col=2
    )

    # Plot 3: Gap of Temperature vs Time
    fig.add_trace(
        go.Scatter(x=data_5329['Absolute Time'], y=data_5329['Gap of Temperature'], mode='lines+markers', name='Gap of Temperature'),
        row=2, col=1
    )

    # Plot 4: CapaCity(mAh) vs Time
    fig.add_trace(
        go.Scatter(x=data_5329['Absolute Time'], y=data_5329['CapaCity(mAh)'], mode='lines+markers', name='CapaCity (mAh)'),
        row=2, col=2
    )

    # Update layout for better appearance
    fig.update_layout(height=800, width=1400, title_text="5329", showlegend=False)

    # Convert the figure to HTML
    chart_html = pio.to_html(fig, full_html=False)

    return HTMLResponse(content=chart_html)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
