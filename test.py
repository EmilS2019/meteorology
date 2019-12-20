import sys
sys.path.append('E:\\npm\python_modules')

from bokeh.plotting import figure, output_file, show
print(figure)

x = [1,2,3,4,5]
y = [4,5,6,1,2]

output_file('index.html')

p = figure(
    title="finally it works holyt motherfuck0",
    x_axis_label="XAXIS",
    y_axis_label="hi"
)

p.line(x, y, legend="hiiiiiiiiiiiii", line_width=2)

show(p)