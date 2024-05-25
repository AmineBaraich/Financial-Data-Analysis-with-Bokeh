# Stock Data Visualization

This project is a web-based application for visualizing stock data using Bokeh. The application allows users to compare two stocks over a specified date range and apply various technical indicators to the data.

## Features

- Load stock data for two different stocks
- Compare stock data over a specified date range
- Apply technical indicators such as 30 Day SMA, 100 Day SMA, and Linear Regression Line
- Interactive plot with zoom, pan, and reset functionalities

## Project Structure

The project is organized into the following modules:

- `main.py` - Main script to run the application
- `data_loader.py` - Module to handle data loading
- `plotter.py` - Module to handle plotting
- `callbacks.py` - Module to handle callbacks and events
- `ui_elements.py` - Module to define UI elements

## Usage

Open the application in your web browser. The Bokeh server will automatically open it. to do that you need to run in your terminale this command :

-`bokeh serve --show main.py` : make sure you are on the same directory as your project folder

After you run the command successfully, you will surely get into an interface just like that :

<img width="703" alt="image" src="https://github.com/AmineBaraich/Financial-Data-Analysis-with-Bokeh/assets/130483250/837ddeca-3760-4e56-82ec-ab81db0596f7">



Enter the ticker symbols for the main stock and the comparison stock.

Select the start and end dates for the data.

Choose the technical indicators you want to apply.

Click the "Load Data" button to visualize the stock data.

## Dependencies

- `Bokeh`
- `yfinance`

These dependencies can be installed using pip.

## File Descriptions

- `main.py`: The main script that sets up the Bokeh server and defines the layout.
- `data_loader.py`: Contains the load_data function that fetches stock data from Yahoo Finance.
- `plotter.py`: Contains the update_plot function that creates and updates the plot.
- `callbacks.py`: Contains the on_button_click function that handles the button click event.
- `ui_elements.py`: Defines the user interface elements such as text inputs, date pickers, and multi-choice options.
