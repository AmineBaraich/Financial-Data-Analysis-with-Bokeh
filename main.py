from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import Button

from ui_elements import stock1_text, stock2_text, date_picker_from, date_picker_to, indicator_choice
from callbacks import on_button_click

load_button = Button(label="Load Data", button_type="success")
load_button.on_click(lambda: on_button_click(stock1_text.value, stock2_text.value, date_picker_from.value, date_picker_to.value, indicator_choice.value))

layout = column(stock1_text, stock2_text, date_picker_from, date_picker_to, indicator_choice, load_button)

curdoc().clear()
curdoc().add_root(layout)
