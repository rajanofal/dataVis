import plotly.offline as plt
import plotly.graph_objs as go
import pandas.plotting
import matplotlib.pyplot as mplt
import pandas as pd

df = pd.read_csv('DataWeierstrass.csv', delimiter=';')


# Task(a) plotting the Scatter Matrix

proff = df['professor']
lect = df['lecture']

p = []
l = []

for i in range(len(proff)):
    x1 = proff[i]
    x2 = lect[i]
    p.append(float(x1[-2:]))
    l.append(float(x2[-3:]))

df['professor'] = p
df['lecture'] = l


fig = {
    'data': [
          {
          'x': df.lecture,
            'y': df.participants,
            'mode': 'markers',
            'name': 'Famous Lecture'},
    ],
    'layout': {
        'xaxis': {'title': "Lectures"},
        'yaxis': {'title': "No. of Participants"}
    }
}

plt.plot(fig, filename='my-graph.html')
# Parallel Coordinate was plotted with the help of the following website: https://plot.ly/python/parallel-coordinates-plot/

# Task(b) plotting the Parallel Coordinates
data = [
    go.Parcoords(
        line = dict(color = df['professor'],
                    showscale = True),

        dimensions = list([
            dict(range = [0,44],
                label = 'Professors', values = df['professor']),
            dict(range = [0,101],
                label = 'Lectures', values = df['lecture']),
            dict(range = [0,326],
                label = 'Participants', values = df['participants']),
            dict(range = [0,5],
                label = 'professional expertise', values = df['professional expertise']),
            dict(range = [0,5],
                label = 'motivation', values = df['motivation']),
            dict(range = [0,5],
                label = 'clear presentation', values = df['clear presentation']),
            dict(range = [0,5],
                label = 'overall impression', values = df['overall impression'])
        ])
    )
]


plt.plot(data, filename='Assignment4.html')
