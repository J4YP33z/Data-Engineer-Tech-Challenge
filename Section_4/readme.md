## Section 4: Charts & APIs

The Python script retrieves COVID-19 data for Singapore from the [covid19api.com](https://covid19api.com/) API and generates a bar chart of monthly new cases and a line graph of total cases so far each month.

## Requirements

To run the script, you will need:

- Python 3
- requests
- pandas
- matplotlib

You can install these packages using pip:

Copy code

`pip install requests pandas matplotlib`

## Usage

To generate the plot, run the `section_4.py` script in a Jupyter notebook.

The script will retrieve COVID-19 data for Singapore from the `covid19api.com` API, filter it to keep only the first entry of each month, and calculate monthly new cases and total cases so far each month. It will then generate a bar chart of monthly new cases and a line graph of total cases so far each month using the `matplotlib` library.
