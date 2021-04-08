from dearpygui.core import *
from dearpygui.simple import *
from math import sin, cos

def save_callback(sender, data):
    print("保存点击")

def print_me(sender, data):
    print("Menu Item: " + sender)


def plot_callback(sender, data):
    clear_plot("Plot")
    data1 = []
    xx=[]
    for i in range(0, 100):
        xx.append(3.14 * i / 180)
        data1.append(cos(3 * 3.14 * i / 180))
    data2 = []
    for i in range(0, 100):
        data2.append(sin(2 * 3.14 * i / 180))
    add_line_series("Plot", "Cos", x=xx, y=data1, weight=2, color=[0, 0, 255, 100])
    # add_shade_series("Plot", "Cos", x=xx, y=data1, weight=2, fill=[255, 0, 0, 100])
    add_scatter_series("Plot", "Sin", x=xx, y=data2)

with window("Plot Window"):
    add_same_line()
    add_text("Metabolic Cost")

    add_spacing()
    add_button("Save Figure", callback=save_callback)

    add_same_line()
    add_button("Plot data", callback=plot_callback)

    add_same_line()
    add_plot("Plot", height=-1)
    
# show_documentation()
start_dearpygui()



# with window("Tutorial"):
#     add_button("Apply")
#     add_same_line(spacing=30)
#     add_button("Apply1")
#     add_same_line(spacing=30, name="sameline1")
#     add_button("Apply2")
#     add_spacing(count=10, name="spacing1")
#     add_button("Apply3")
#     add_spacing(count=10, name="spacing2")
#     add_button("Apply4")
# 

# start_dearpygui()
# show_documentation()
