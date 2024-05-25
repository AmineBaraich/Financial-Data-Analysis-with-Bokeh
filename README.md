# Stock Data Visualization

This project is a web-based application for visualizing stock data using Bokeh. The application allows users to compare two stocks over a specified date range and apply various technical indicators to the data.

## Features

- Load stock data for two different stocks from yfinance
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
- Example : comparison between Tesla and Apple.
  
<img width="699" alt="image" src="https://github.com/AmineBaraich/Financial-Data-viz-with-Bokeh/assets/130483250/9a0ff3cb-25fc-4be7-93cc-f71531e1bdd4">

Then, select the start and end dates for the data.

<img width="699" alt="image" src="https://github.com/AmineBaraich/Financial-Data-viz-with-Bokeh/assets/130483250/b006e6a2-3efa-46be-86ad-a6f41d38e1b5">


Choose the technical indicators you want to apply.

<img width="695" alt="image" src="https://github.com/AmineBaraich/Financial-Data-viz-with-Bokeh/assets/130483250/bb07d6a8-365f-4060-93f1-29625cfd8641">


Finally, click the "Load Data" button to visualize the stock data.

<img width="602" alt="image" src="https://github.com/AmineBaraich/Financial-Data-viz-with-Bokeh/assets/130483250/0337cedb-1a22-4fbc-b6f4-be724cdcbc47">


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
