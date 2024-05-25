import math
import numpy as np
from bokeh.plotting import figure

def update_plot(data, indicators, sync_axis=None):
    df = data
    gain = df.Close > df.Open
    loss = df.Open > df.Close
    width = 12 * 60 * 60 * 1000  # half day in ms

    if sync_axis is not None:
        p = figure(x_axis_type="datetime", tools="pan,wheel_zoom,box_zoom,reset,save", width=1000, x_range=sync_axis)
    else:
        p = figure(x_axis_type="datetime", tools="pan,wheel_zoom,box_zoom,reset,save", width=1000)

    p.xaxis.major_label_orientation = math.pi / 4
    p.grid.grid_line_alpha = 0.3

    p.segment(df.index, df.High, df.index, df.Low, color="black")
    p.vbar(df.index[gain], width, df.Open[gain], df.Close[gain], fill_color="#00ff00", line_color="#00ff00")
    p.vbar(df.index[loss], width, df.Open[loss], df.Close[loss], fill_color="#ff0000", line_color="#ff0000")

    for indicator in indicators:
        print(indicator)
        if indicator == "30 Day SMA":
            df['SMA30'] = df['Close'].rolling(30).mean()
            p.line(df.index, df.SMA30, color="purple", legend_label="30 Day SMA")
        elif indicator == "100 Day SMA":
            df['SMA100'] = df['Close'].rolling(100).mean()
            p.line(df.index, df.SMA100, color="blue", legend_label="100 Day SMA")
        elif indicator == "Linear Regression Line":
            par = np.polyfit(range(len(df.index.values)), df.Close.values, 1, full=True)
            slope = par[0][0]
            intercept = par[0][1]
            y_predicted = [slope * i + intercept for i in range(len(df.index.values))]
            p.segment(df.index[0], y_predicted[0], df.index[-1], y_predicted[-1], legend_label="Linear Regression", color="red")

    p.legend.location = "top_left"
    p.legend.click_policy = "hide"

    return p
