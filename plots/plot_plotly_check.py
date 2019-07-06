import plotly
import plotly.graph_objs as obj

x = [i for i in range(11)]
#y = mx + b --- equation of straight line
y = []
for a in x:
    y.append((2 * a) + 2)

trace = obj.Scatter(
    x=x,
    y=y
)

data = [trace]
plotly.offline.plot(data, auto_open=True)
