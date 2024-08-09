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

```bash
git clone https://github.com/yourusername/li-ion-cell-dashboard.git
cd li-ion-cell-dashboard
