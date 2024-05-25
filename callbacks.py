from bokeh.io import curdoc
from bokeh.layouts import row

from data_loader import load_data
from plotter import update_plot

def on_button_click(main_stock, comparison_stock, start, end, indicators):
    source1, source2 = load_data(main_stock, comparison_stock, start, end)
    p = update_plot(source1, indicators)
    p2 = update_plot(source2, indicators, sync_axis=p.x_range)
    curdoc().clear()
    curdoc().add_root(row(p, p2))
